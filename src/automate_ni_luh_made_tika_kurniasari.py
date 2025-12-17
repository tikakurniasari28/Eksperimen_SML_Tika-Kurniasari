import kagglehub

path = kagglehub.dataset_download("imdevskp/corona-virus-report")
print(path)
!ls $path

!mkdir -p data/raw
!cp $path/day_wise.csv data/raw/
    
     %%writefile src/automate_Ni-Luh-Made-Tika-Kurniasari.py
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
         scaled_data = scaler.fit_transform(df)
     
         df_processed = pd.DataFrame(scaled_data, columns=df.columns)
     
         output_path.parent.mkdir(parents=True, exist_ok=True)
     
         df_processed.to_csv(output_path, index=False)
     
         return df_processed
     
     if __name__ == "__main__":
         preprocess_data()

!python src/automate_Ni-Luh-Made-Tika-Kurniasari.py

!ls data/processed
