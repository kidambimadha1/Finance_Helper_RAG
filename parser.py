import pandas as pd
import os

def load_expenses(folder="data"):
    all_data = []
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder, file))
            for _, row in df.iterrows():
                row_text = f"{row['Date']} - {row['Description']} - {row['Category']} - Rs.{row['Amount']}"
                all_data.append(row_text)
    return all_data
