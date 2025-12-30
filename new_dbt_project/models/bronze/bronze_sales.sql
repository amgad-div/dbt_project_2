{{ config(materialized='view') }}

select * from {{ ref('sales_2024_01') }}
union all
select * from {{ ref('sales_2024_02') }}

