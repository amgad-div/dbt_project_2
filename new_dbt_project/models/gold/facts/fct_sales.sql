{{ config(materialized='table') }}

select
    s.sale_id,
    s.sale_date,
    d.year,
    d.month,
    s.book_id,
    b.category,
    s.quantity,
    s.unit_price,
    s.total_amount
from {{ ref('silver_sales_base') }} s
join {{ ref('dim_books') }} b
  on s.book_id = b.book_id
join {{ ref('dim_date') }} d
  on s.sale_date = d.date_day

