# Omega Watch Data Cleaning

This project demonstrates my ability to take messy CSV data, clean and preprocess it using Python and pandas, and produce a polished dataset ready for analysis or external consumption.  

This is a **data cleaning exercise in Python**. The initial data load came from a `.csv` dataset, imported into **Spyder** (where the cleaning occurred), then exported to an external stage where the cleaned data could be consumed.  

The goal is to take a raw Omega watch dataset and transform it into a clean, analyzable format, including handling missing data, truncating text columns, converting prices to numeric, and creating price tiers.

---

## Features

- Load raw CSV data using pandas
- Drop unnecessary columns and handle irrelevant data
- Truncate watch model names for consistency
- Handle missing or placeholder data (e.g., "Price on request")
- Convert `price` column from string to numeric
- Bucket prices into categories (`Entry`, `Mid`, `High`, `Ultra High`)
- Generate summary statistics:
  - Count of watches per price tier
  - Top models by frequency
- Save cleaned datasets for further analysis or external consumption

---

## Skills Demonstrated

- Python data manipulation with pandas
- Data cleaning and preprocessing
- String operations and text extraction
- Handling missing and inconsistent data
- Numeric conversions and binning
- Generating quick summary statistics
- Exporting cleaned data for downstream use
- Modular and reproducible code

---

