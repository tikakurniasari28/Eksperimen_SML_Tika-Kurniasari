from pathlib import Path
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

BASE_DIR = Path(__file__).resolve().parents[1]

def preprocess_data():
    input_path = BASE_DIR / "data/raw/day_wise.csv"
    output_path = BASE_DIR / "data/processed/day_wise_processed.csv"

    df = pd.read_csv(input_path)

    df = df.drop(columns=["Date"], errors="ignore")

    df = df.ffill()

    df = df.drop_duplicates()

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df)

    df_processed = pd.DataFrame(scaled, columns=df.columns)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df_processed.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data()
