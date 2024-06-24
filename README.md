# Projeto ELT com dbt e Snowflake

![Arquitetura do Projeto](https://github.com/NaraGuimma/demo_dbt/blob/main/projeto_ELT.jpeg)

## Descrição do Projeto

Este repositório contém um projeto de ELT (Extract, Load, Transform) utilizando dbt (Data Build Tool) e Snowflake. Os dados serão extraídos de uma API pública [Jobicy](https://jobicy.com/jobs-rss-feed) usando um script em Python, carregados no Snowflake em tabelas, e transformados utilizando dbt, resultando na crição de views dentro do Snowflake.

## Tecnologias Utilizadas

### dbt (Data Build Tool)

dbt é uma ferramenta de transformação de dados que permite aos profissionais de dados transformar dados no data warehouse de maneira colaborativa e eficiente. O dbt facilita a criação de pipelines de transformação SQL utilizando uma abordagem baseada em código.

Saiba mais sobre o dbt:
- [Documentação do dbt](https://docs.getdbt.com/docs/introduction)

Instalação do dbt:
- [Com pip](https://docs.getdbt.com/docs/core/pip-install)
- [Clone do código fonte](https://docs.getdbt.com/docs/core/source-install)
- [Via docker](https://docs.getdbt.com/docs/core/docker-install)

### Snowflake

Snowflake é um data warehouse como serviço (DWaaS) que oferece uma solução de armazenamento de dados escalável e altamente performática. Ele permite a realização de consultas analíticas de forma rápida e eficiente.

Saiba mais sobre o Snowflake:
- [Documentação do Snowflake](https://docs.snowflake.com/en/)

### Processo ELT

ELT (Extract, Load, Transform) é uma variante do processo ETL (Extract, Transform, Load). No ELT, os dados são primeiro extraídos de suas fontes, carregados no data warehouse e depois transformados. Este processo é particularmente eficaz quando combinado com a potência e escalabilidade de um data warehouse moderno como o Snowflake.

Para saber mais:
- [Entendendo as Diferenças entre ETL e ELT: Qual é a Melhor Abordagem para Seus Dados?](https://medium.com/@nara.guimaraes/entendendo-as-diferen%C3%A7as-entre-etl-e-elt-qual-%C3%A9-a-melhor-abordagem-para-seus-dados-932ad45e8b23)

## Requisitos

- Python 3.x
- [Visual Studio Code](https://code.visualstudio.com/)
- [dbt Core](https://docs.getdbt.com/dbt-cli/install/overview)
- Conta trial do Snowflake: [Inscreva-se aqui](https://signup.snowflake.com/)


### Clonando o Repositório

```sh
git clone https://github.com/NaraGuimma/demo_dbt.git
cd demo_dbt
```

### Instalando as Bibliotecas Python
Instale as bibliotecas listadas no requirements.txt:

```sh
pip install -r extraction/requirements.txt 
```

### Configuração do Projeto
1 - Configure suas credenciais do Snowflake no arquivo `profiles.yml` do dbt que se encontra dentro da pasta `.dbt`:

```yaml
your_profile_name:
  target: dev
  outputs:
    dev:
      type: snowflake
      account: your_account
      user: your_username
      password: your_password
      role: your_role
      database: your_database
      warehouse: your_warehouse
      schema: your_schema
```
 2 - Execute o script Python para extrair os dados da API e carregá-los no Snowflake:

 ```sh
python extraction/script.py
```

3 - Testar a conexão do banco de dados e exibir informações para fins de depuração do dbt:

```sh
cd dbt
dbt debug
```

4 - Execute as transformações com o dbt:

```sh
cd dbt
dbt run
```

## Estrutura do Projeto

```markdown
- demo_dbt/
  - extraction/
    - script.py
    - requirements.py
  - dbt/
    - analyses/
    - logs/
    - macros/
    - models/
      - silver/
        - trabalhos_remotos_final.sql
      schema.yml
    - seeds/
    - snapshots/
    - target/
    - tests/
    - dbt_project.yml
  - .envexemplo
  - .gitignore
  - README.md
  - projeto_ELT.jpeg

```
