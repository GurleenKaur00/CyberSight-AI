"""
transform.py
------------

This module is responsible for transforming the extracted data.

Functions:
    validate_data()
    clean_data()
    feature_engineering()
    save_processed_data()
    transform_data()
"""

from pathlib import Path
import pandas as pd


# ==========================================================
# Validate Data
# ==========================================================

def validate_data(df):
    """
    Validate the dataset before transformation.
    """

    print("\nValidating dataset...")

    print(f"Rows: {len(df):,}")
    print(f"Columns: {df.shape[1]}")

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    print(f"Missing Values : {missing}")
    print(f"Duplicate Rows : {duplicates}")

    return df


# ==========================================================
# Clean Data
# ==========================================================

def clean_data(df):
    """
    Perform data cleaning.
    """

    print("\nCleaning dataset...")

    # Remove duplicate rows if any
    df = df.drop_duplicates()

    # Reset index
    df = df.reset_index(drop=True)

    print("Cleaning completed.")

    return df


# ==========================================================
# Feature Engineering
# ==========================================================

def feature_engineering(df):
    """
    Create meaningful traffic-based features.
    """

    print("\nApplying feature engineering...")

    # ------------------------------------------------------
    # Total bytes transferred
    # ------------------------------------------------------
    df["total_bytes"] = df["sbytes"] + df["dbytes"]

    # ------------------------------------------------------
    # Total packets transferred
    # ------------------------------------------------------
    df["total_packets"] = df["spkts"] + df["dpkts"]

    # ------------------------------------------------------
    # Average bytes per packet
    # ------------------------------------------------------
    df["bytes_per_packet"] = (
        df["total_bytes"] /
        (df["total_packets"] + 1)
    )

    # ------------------------------------------------------
    # Traffic direction ratio
    # Source bytes / Destination bytes
    # ------------------------------------------------------
    df["traffic_direction_ratio"] = (
        df["sbytes"] /
        (df["dbytes"] + 1)
    )

    # ------------------------------------------------------
    # Packet direction ratio
    # Source packets / Destination packets
    # ------------------------------------------------------
    df["packet_direction_ratio"] = (
        df["spkts"] /
        (df["dpkts"] + 1)
    )

    print("Feature engineering completed.")
    print("New Features Added:")
    print("  • total_bytes")
    print("  • total_packets")
    print("  • bytes_per_packet")
    print("  • traffic_direction_ratio")
    print("  • packet_direction_ratio")

    return df


# ==========================================================
# Save Processed Dataset
# ==========================================================

def save_processed_data(df):
    """
    Save transformed dataset.
    """

    BASE_DIR = Path(__file__).resolve().parent.parent

    processed_dir = BASE_DIR / "data" / "processed"

    processed_dir.mkdir(parents=True, exist_ok=True)

    output_path = processed_dir / "cleaned_network_data.csv"

    df.to_csv(output_path, index=False)

    print(f"\nProcessed dataset saved to:\n{output_path}")


# ==========================================================
# Main Transform Function
# ==========================================================

def transform_data(df):
    """
    Complete transformation pipeline.
    """

    rows_before = len(df)

    df = validate_data(df)
    df = clean_data(df)
    df = feature_engineering(df)

    rows_after = len(df)

    save_processed_data(df)

    print("\n" + "="*50)
    print("TRANSFORMATION SUMMARY")
    print("="*50)
    print(f"Rows Before           : {rows_before:,}")
    print(f"Rows After            : {rows_after:,}")
    print(f"Rows Removed          : {rows_before - rows_after:,}")
    print(f"Missing Values        : {df.isnull().sum().sum()}")
    print(f"Duplicate Rows        : {df.duplicated().sum()}")
    print(f"Original Features     : 46")
    print(f"Engineered Features   : 5")
    print(f"Total Features        : {df.shape[1]}")
    print("="*50)

    return df