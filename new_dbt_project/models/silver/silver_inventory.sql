{{ config(materialized='table') }}

select
    book_id,
    available_qty::int,
    updated_at::timestamp
from {{ ref('inventory') }}
where available_qty >= 0
