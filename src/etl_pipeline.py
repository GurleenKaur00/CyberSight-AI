"""
etl_pipeline.py
---------------

Main ETL pipeline for CyberSight AI.

Pipeline Flow:
    Extract
        ↓
    Transform
        ↓
    Load

Run:
    python src/etl_pipeline.py
"""

from extract import extract_data
from transform import transform_data
from load import load_data


# ==========================================================
# Main ETL Pipeline
# ==========================================================

def main():
    """
    Execute the complete ETL pipeline.
    """

    print("\n" + "=" * 60)
    print("CYBERSIGHT AI - ETL PIPELINE")
    print("=" * 60)

    # ------------------------------------------------------
    # Extract
    # ------------------------------------------------------
    print("\n[1/3] EXTRACT")
    df = extract_data()

    # ------------------------------------------------------
    # Transform
    # ------------------------------------------------------
    print("\n[2/3] TRANSFORM")
    df = transform_data(df)

    # ------------------------------------------------------
    # Load
    # ------------------------------------------------------
    print("\n[3/3] LOAD")
    load_data(df)

    print("\n" + "=" * 60)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()