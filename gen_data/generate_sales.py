import pandas as pd
import numpy as np

from datetime import datetime


ROWS_PER_FILE = 1_000_000
BOOKS_COUNT = 3_000_000

start_date = pd.to_datetime("2024-01-01")
months = pd.date_range(start=start_date, periods=10, freq="MS")

sale_id_counter = 1

print("Generating sales data...")

for month in months:
    rows = ROWS_PER_FILE

    df = pd.DataFrame({
        "sale_id": range(sale_id_counter, sale_id_counter + rows),
        "book_id": np.random.randint(1, BOOKS_COUNT + 1, rows),
        "quantity": np.random.randint(1, 6, rows),
        "unit_price": np.random.uniform(10, 500, rows).round(2),
        "sale_date": np.random.choice(
            pd.date_range(month, month + pd.offsets.MonthEnd(1)),
            rows
        )
    })

    df["total_amount"] = (df["quantity"] * df["unit_price"]).round(2)
    df["created_at"] = datetime.utcnow()

    file_name = f"sales_{month.strftime('%Y_%m')}.csv"
    df.to_csv(file_name, index=False)

    sale_id_counter += rows
    print(f"{file_name} generated")

print("All sales files generated")
