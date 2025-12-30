{{ config(materialized='table') }}

select
    book_id::int as book_id,
    trim(title) as title,
    lower(category) as category,
    price::numeric(10,2) as price,
    rating::numeric(3,2) as rating,
    updated_at::timestamp
from {{ ref('bronze_books') }}
where price > 0
