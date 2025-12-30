# dbt Project 2 — Medallion Architecture (Bronze → Silver → Gold)

##  Overview

This is a **dbt project**  a Medallion-style analytics pipeline using large seed CSV files.  
It includes Bronze ingestion, Silver cleaning/enrichment, and Gold analytics-ready models.

---

## Project Structure
new_dbt_project/

├── seeds/
│   
  ├── books/
│   
│   ├── books_part_1.csv

 │   ├── books_part_2.csv
│   
│   └── ... (multiple CSV partitions)
│   

├── sales/
│   
│   ├── sales_2024_01.csv
│   
│   ├── sales_2024_02.csv
│  
 │   └── ... (monthly CSVs)
│   
└── inventory.csv

│
├── models/

│     ├── bronze/
│   
│   ├── bronze_books.sql
│   
│   └── bronze_sales.sql
│   │
│ 
 
 ├── silver/
│ 
  
│ 
  ├── silver_books_base.sql
│  
 │   ├── silver_sales_base.sql
│  
 │   └── silver_inventory.sql
│   │
│   

└── gold/
│      
 ├── dimensions/
│      
 │   ├── dim_books.sql
│     
  │   └── dim_date.sql
│     
  │
│       
└── facts/
│       
    ├── fct_sales.sql
│        
   └── fct_inventory.sql
│

└── snapshots/
    
└── books_price_snapshot.sql





---

## Layers

###  Bronze
Raw seed data loaded from CSV files using `dbt seed`.

###  Silver
Staging models that:
- Clean and standardize raw data
- Perform type casting and basic logic
- Prepare data for analytics

###  Gold
Analytics-ready models:
- **Dimensions** (`dim_books`, `dim_date`)
- **Facts** (`fct_sales`, `fct_inventory`)
Designed for BI queries and reporting.

---

<img width="967" height="360" alt="image" src="https://github.com/user-attachments/assets/844dc969-078f-4c68-99f8-624ca30c4c49" />


