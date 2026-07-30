"""
extract.py
-----------

This module is responsible for extracting raw data from CSV files.

Functions:
    extract_data() -> Reads training and testing datasets,
                      adds dataset identifiers,
                      merges them,
                      and returns a pandas DataFrame.
"""

from pathlib import Path
import pandas as pd


def extract_data():
    """
    Extract data from raw CSV files.

    Returns
    -------
    pandas.DataFrame
        Combined training and testing dataset.
    """

    # Project root directory
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Raw data directory
    RAW_DATA_DIR = BASE_DIR / "data" / "raw"

    # File paths
    train_path = RAW_DATA_DIR / "UNSW_NB15_training-set.csv"
    test_path = RAW_DATA_DIR / "UNSW_NB15_testing-set.csv"

    # Read datasets
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)

    # Identify dataset source
    train["dataset"] = "train"
    test["dataset"] = "test"

    # Merge datasets
    df = pd.concat([train, test], ignore_index=True)

    print("=" * 50)
    print("DATA EXTRACTION COMPLETED")
    print("=" * 50)
    print(f"Training Records : {len(train):,}")
    print(f"Testing Records  : {len(test):,}")
    print(f"Total Records    : {len(df):,}")
    print(f"Total Features   : {df.shape[1]}")
    print("=" * 50)

    return df


if __name__ == "__main__":
    dataframe = extract_data()

    print("\nFirst Five Rows")
    print(dataframe.head())