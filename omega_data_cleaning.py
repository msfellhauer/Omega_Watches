import pandas as pd
import os

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Drop unnecessary columns
    df = df.drop(columns=[
        'aaaaaaaaaaaaaaaaa-href', 
        'web-scraper-order', 
        'web-scraper-start-url', 
        'model', 
        'brand', 
        'name', 
        'select-brands-href'
    ])
    # Truncate model names
    df['model_trunc'] = df['name'].str.replace(r'^Omega\s+', '', regex=True)
    # Drop missing or placeholder price
    df = df.dropna()
    df = df[df['price'] != 'Price on request']
    return df

def process_price(df):
    df['price'] = df['price'].str.replace('$', '', regex=False).str.replace(',', '', regex=False)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    # Create price tiers
    bins = [0, 5000, 10000, 15000, 20000]
    labels = ['Entry', 'Mid', 'High', 'Ultra High']
    df['price_tier'] = pd.cut(df['price'], bins=bins, labels=labels)
    df = df.dropna()
    return df

def summarize(df):
    price_summary = df['price_tier'].value_counts().sort_index()
    model_counts = df['model_trunc'].value_counts().reset_index()
    model_counts.columns = ['Model', 'Count']
    print("\nPrice tier counts:\n", price_summary)
    print("\nTop 10 models:\n", model_counts.head(10))

def save_data(df, path):
    df.to_csv(path, index=False)
    print("Cleaned data saved to:", path)

# -------------------------
# Main workflow
# -------------------------
if __name__ == "__main__":
    BASE_DIR = os.path.join(os.path.expanduser("~"), "Documents", "PythonPractice", "Omega")
    RAW_CSV = os.path.join(BASE_DIR, "data", "raw", "OMEGa.csv")
    PROCESSED_CSV = os.path.join(BASE_DIR, "data", "processed", "Omega_ml_Model.csv")

    df = load_data(RAW_CSV)
    df = clean_data(df)
    df = process_price(df)
    summarize(df)
    save_data(df, PROCESSED_CSV)
