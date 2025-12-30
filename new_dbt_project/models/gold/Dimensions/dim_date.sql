{{ config(materialized='table') }}

select distinct
    sale_date as date_day,
    extract(year from sale_date) as year,
    extract(month from sale_date) as month,
    extract(day from sale_date) as day,
    extract(week from sale_date) as week,
    extract(dow from sale_date) as day_of_week
from {{ ref('silver_sales_base') }}
