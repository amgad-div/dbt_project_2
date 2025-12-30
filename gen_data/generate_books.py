import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
Faker.seed(42)

ROWS = 3_000_000
CHUNK_SIZE = 500_000  

categories = [
    "Technology", "History", "Science", "Business",
    "Fiction", "Health", "Education"
]

print("Generating books data...")

for i in range(0, ROWS, CHUNK_SIZE):
    df = pd.DataFrame({
        "book_id": range(i+1, min(i+CHUNK_SIZE, ROWS)+1),
        "title": [fake.sentence(nb_words=4) for _ in range(min(CHUNK_SIZE, ROWS-i))],
        "author": [fake.name() for _ in range(min(CHUNK_SIZE, ROWS-i))],
        "category": np.random.choice(categories, min(CHUNK_SIZE, ROWS-i)),
        "price": np.random.uniform(10, 500, min(CHUNK_SIZE, ROWS-i)).round(2),
        "rating": np.random.randint(1, 6, min(CHUNK_SIZE, ROWS-i)),
        "created_at": pd.Timestamp("2023-01-01"),
        "updated_at": pd.Timestamp("2024-01-01")
    })
    
    filename = f"books_part_{i//CHUNK_SIZE + 1}.csv"
    df.to_csv(filename, index=False)
    print(f"{filename} generated")

print("All CSV files generated successfully")