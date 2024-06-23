
    
    

select
    id as unique_field,
    count(*) as n_records

from DEMO_DBT.PUBLIC.lista_trabalhos
where id is not null
group by id
having count(*) > 1


