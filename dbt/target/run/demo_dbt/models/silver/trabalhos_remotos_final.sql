
  create or replace   view DEMO_DBT.PUBLIC.trabalhos_remotos_final
  
   as (
    with source as (
    select
        "jobTitle",
        "companyName",
        "jobType",
        "jobLevel",
        "annualSalaryMin",
        "annualSalaryMax",
        "salaryCurrency"
    from DEMO_DBT.PUBLIC.lista_trabalhos
    where "annualSalaryMin" is not null 
    and "annualSalaryMax" is not null
),
renamed as (
    select
        "jobTitle" as titulo_vaga,
        "companyName" as nome_empresa,
        "jobType" as tipo_trabalho,
        "jobLevel" as senioridade,
        TRY_CAST("annualSalaryMin" as float) as minimo_salario_anual ,
        TRY_CAST("annualSalaryMax" as float) as maximo_salario_anual,
        "salaryCurrency" as moeda
    from source
),
final as (
    select
        titulo_vaga,
        nome_empresa,
        tipo_trabalho,
        senioridade,
        minimo_salario_anual/12 as minimo_salario_mensal,
        minimo_salario_anual,
        maximo_salario_anual/12 as maximo_salario_mensal,
        maximo_salario_anual,
        moeda
    from renamed
)
select * from final
  );

