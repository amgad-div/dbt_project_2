{{ config(materialized='table') }}

select
    book_id,
    title,
    category,
    rating,
    price
from {{ ref('silver_books_base') }}
