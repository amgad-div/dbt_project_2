# dbt Project 2 — Medallion Architecture (Bronze → Silver → Gold)

##  Overview

This is a **dbt project**  a Medallion-style analytics pipeline using large seed CSV files.  
It includes Bronze ingestion, Silver cleaning/enrichment, and Gold analytics-ready models.

---

## Project Structure

new_dbt_project/
├── seeds/
│ ├── books/
│ │ ├── books_part_1.csv
│ │ └── ... (multiple CSV partitions)
│ ├── sales/
│ │ ├── sales_2024_01.csv
│ │ └── ... (monthly CSVs)
│ └── inventory.csv
│
├── models/
│ ├── bronze/
│ │ ├── bronze_books.sql
│ │ └── bronze_sales.sql
│ ├── silver/
│ │ ├── silver_books_base.sql
│ │ ├── silver_sales_base.sql
│ │ └── silver_inventory.sql
│ └── gold/
│ ├── dimensions/
│ │ ├── dim_books.sql
│ │ └── dim_date.sql
│ └── facts/
│ ├── fct_sales.sql
│ └── fct_inventory.sql
│
└── snapshots/
└── books_price_snapshot.sql
