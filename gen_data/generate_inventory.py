import pandas as pd
import numpy as np
from datetime import datetime

ROWS = 3_000_000

print("Generating inventory data...")

df = pd.DataFrame({
    "book_id": range(1, ROWS + 1),
    "available_qty": np.random.randint(0, 500, ROWS),
    "updated_at": pd.Timestamp("2024-01-01")
})

df.to_csv("inventory.csv", index=False)
print("inventory.csv generated ")
