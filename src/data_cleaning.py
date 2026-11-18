import pandas as pd
from config.settings import RAW_DATA_PATH
from config.settings import PROCESSED_DATA_PATH

def clean_data():
    df = pd.read_csv(RAW_DATA_PATH)

    m = df["land_size_acres"].mean()
    df["land_size_acres"] = df["land_size_acres"].fillna(m)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    
    return df