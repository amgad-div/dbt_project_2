{{ config(materialized='view') }}

select * from {{ ref('books_part_1') }}
union all
select * from {{ ref('books_part_2') }}
union all
select * from {{ ref('books_part_3') }}
union all
select * from {{ ref('books_part_4') }}
union all
select * from {{ ref('books_part_5') }}
union all
select * from {{ ref('books_part_6') }}
