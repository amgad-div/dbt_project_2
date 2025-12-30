{{ config(
    materialized='incremental',
    unique_key='sale_id'
) }}

select
    sale_id,
    book_id,
    quantity::int,
    unit_price::numeric(10,2),
    total_amount::numeric(12,2),
    sale_date::date,
    created_at::timestamp
from {{ ref('bronze_sales') }}

{% if is_incremental() %}
  where created_at >
    (select max(created_at) from {{ this }})
{% endif %}
