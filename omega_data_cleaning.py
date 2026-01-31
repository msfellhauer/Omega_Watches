# -*- coding: utf-8 -*-
"""
Omega Watch Data Cleaning
@author: markf
Created: 2026-01-02

Purpose:
    Clean and preprocess Omega watch dataset for analysis, including:
    - Dropping unnecessary columns
    - Truncating model names
    - Handling missing data
    - Converting price to numeric
    - Creating price tiers
    - Saving cleaned dataset
    - Summarizing price tiers and top models
"""

# -------------------------
# Library Imports
# -------------------------
import pandas as pd
import os

# -------------------------
# Define file paths
# -------------------------
BASE_DIR = os.path.join(os.path.expanduser("~"), "Documents", "PythonPractice", "Omega")
os.makedirs(BASE_DIR, exist_ok=True)

RAW_CSV = os.path.join(BASE_DIR, "OMEGa.csv")
CLEANED_CSV = os.path.join(BASE_DIR, "Omega_Cleaned.csv")
ML_MODEL_CSV = os.path.join(BASE_DIR, "Omega_ml_Model.csv")

# -------------------------
# Load raw data
# -------------------------
df = pd.read_csv(RAW_CSV)
print("Columns in raw data:", df.columns)
print("First 5 rows:\n", df.head())

# -------------------------
# Initial cleaning
# -------------------------
# Drop unnecessary column
df = df.drop(columns=['aaaaaaaaaaaaaaaaa-href'])

# Truncate model names
df['model_trunc'] = df['name'].str.replace(r'^Omega\s+', '', regex=True)

# Drop additional unwanted columns
df = df.drop(columns=[
    'web-scraper-order', 
    'web-scraper-start-url', 
    'model', 
    'brand', 
    'name', 
    'select-brands-href'
])

# -------------------------
# Handle missing data
# -------------------------
df = df.dropna()
df = df[df['price'] != 'Price on request']  # Remove placeholder prices

# -------------------------
# Process price column
# -------------------------
df['price'] = (
    df['price']
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# -------------------------
# Bucket prices into tiers
# -------------------------
bins = [0, 5000, 10000, 15000, 20000]
labels = ['Entry', 'Mid', 'High', 'Ultra High']
df['price_tier'] = pd.cut(df['price'], bins=bins, labels=labels)

# Drop any remaining missing data
df_ml_model = df.dropna()
print(f"Rows after cleaning: {len(df_ml_model)}")

# -------------------------
# Save cleaned data
# -------------------------
df_ml_model.to_csv(ML_MODEL_CSV, index=False)
print("Cleaned data saved to:", ML_MODEL_CSV)

# -------------------------
# Quick summary
# -------------------------
# Count how many watches fall into each price tier
price_summary = df_ml_model['price_tier'].value_counts().sort_index()
print("\nPrice tier counts:\n", price_summary)

# Top models by count
model_counts = df_ml_model['model_trunc'].value_counts().reset_index()
model_counts.columns = ['Model', 'Count']
print("\nTop 10 models:\n", model_counts.head(10))

# -------------------------
# Current working directory
# -------------------------
print("\nCurrent working directory:", os.getcwd())
