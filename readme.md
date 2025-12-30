# dbt Project 2 — Medallion Architecture (Bronze → Silver → Gold)

##  Overview

This is a **dbt project**  a Medallion-style analytics pipeline using large seed CSV files.  
It includes Bronze ingestion, Silver cleaning/enrichment, and Gold analytics-ready models.

---

## Project Structure
🧱 Project Structure

🔹 seeds/

Raw CSV files organized by domain:

books/

books_part_1.csv

books_part_2.csv

sales/

sales_2024_01.csv

sales_2024_02.csv

Additional:

inventory.csv

These files are loaded into the database using dbt seed, typically into the bronze schema.

🔸 models/

Organized into transformation layers:

bronze/

Initial staging models:

bronze_books.sql

bronze_sales.sql

silver/

Cleaned and standardized models:

silver_books_base.sql

silver_sales_base.sql

silver_inventory.sql

gold/

Final analytical models:

facts/

fct_sales.sql

fct_inventory.sql

dimensions/

dim_books.sql

dim_date.sql

snapshots/

books_price_snapshot.sql

🧪 snapshots/





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

