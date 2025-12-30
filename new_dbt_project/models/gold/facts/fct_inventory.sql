{{ config(materialized='table') }}

select
    i.book_id,
    b.category,
    i.available_qty,
    i.updated_at
from {{ ref('silver_inventory') }} i
join {{ ref('dim_books') }} b
  on i.book_id = b.book_id
