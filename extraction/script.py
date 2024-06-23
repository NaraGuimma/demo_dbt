import requests
import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
import os
from dotenv import load_dotenv

load_dotenv()

class JobicyAPI:
    def __init__(self, base_url: str, industry: str, count: int):
        self.base_url = base_url
        self.industry = industry
        self.count = count
        self.data = None

    def fetch_data(self):
        url = f"{self.base_url}?count={self.count}&industry={self.industry}"
        response = requests.get(url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            response.raise_for_status()

    def get_jobs_data(self):
        if self.data and 'jobs' in self.data:
            return pd.DataFrame(self.data['jobs'])
        else:
            return pd.DataFrame()

class Snowflake:
    def __init__(self, account: str, user: str, password: str, database: str, schema: str, warehouse: str):
        self.engine = create_engine(URL(
            account=account,
            user=user,
            password=password,
            database=database,
            schema=schema,
            warehouse=warehouse
        ))

    def save_to_snowflake(self, df: pd.DataFrame, table_name: str):
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)

def flatten_nested_columns(df):
    if 'jobIndustry' in df.columns:
        df['jobIndustry'] = df['jobIndustry'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    if 'jobType' in df.columns:
        df['jobType'] = df['jobType'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    return df

def main():
    api = JobicyAPI(
        base_url="https://jobicy.com/api/v2/remote-jobs",
        industry="data-science",
        count=5
    )
    api.fetch_data()

    jobs_df = api.get_jobs_data()

    expected_columns = [
        'id', 'url', 'jobSlug', 'jobTitle', 'companyName', 'companyLogo',
        'jobIndustry', 'jobType', 'jobGeo', 'jobLevel', 'jobExcerpt',
        'jobDescription', 'pubDate', 'annualSalaryMin', 'annualSalaryMax',
        'salaryCurrency'
    ]

    for col in expected_columns:
        if col not in jobs_df.columns:
            jobs_df[col] = None

    jobs_df = flatten_nested_columns(jobs_df)

    jobs_df = jobs_df[expected_columns]

    if not jobs_df.empty:
        saver = Snowflake(
            account=os.getenv('SNOWFLAKE_ACCOUNT'),
            user=os.getenv('SNOWFLAKE_USER'),
            password=os.getenv('SNOWFLAKE_PASSWORD'),
            database=os.getenv('SNOWFLAKE_DATABASE'),
            schema=os.getenv('SNOWFLAKE_SCHEMA'),
            warehouse=os.getenv('SNOWFLAKE_DATAWAREHOUSE')
        )

        saver.save_to_snowflake(jobs_df, table_name='lista_trabalhos')
        print('Dados salvos com sucesso')
    else:
        print("Não existem dados para salvar no Snowflake")

if __name__ == '__main__':
    main()
