{% snapshot books_price_snapshot %}

{{
    config(
      target_schema='snapshots',
      unique_key='book_id',
      strategy='timestamp',
      updated_at='updated_at'
    )
}}

select book_id, price, updated_at
from {{ ref('silver_books_base') }}

{% endsnapshot %}
