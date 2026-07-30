"""
load.py
-------

This module is responsible for loading the transformed dataset
into the SQLite database.

Functions:
    create_database()
    load_data()
"""

from pathlib import Path
import sqlite3
import pandas as pd


# ==========================================================
# Database Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "database" / "cybersight.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


# ==========================================================
# Create Database
# ==========================================================

def create_database(connection):
    """
    Create database tables using schema.sql.
    """

    print("\nCreating database schema...")

    with open(SCHEMA_PATH, "r") as file:
        schema = file.read()

    connection.executescript(schema)

    print("Database schema created successfully.")


# ==========================================================
# Load Data
# ==========================================================

def load_data(df):
    """
    Load transformed data into SQLite database.
    """

    print("\nConnecting to SQLite database...")

    conn = sqlite3.connect(DATABASE_PATH)

    try:

        # -----------------------------------------------
        # Create Tables
        # -----------------------------------------------

        create_database(conn)

        print("\nLoading data into database...")
        print(f"Loading {len(df):,} records...")

        # record_id is created automatically
        df.to_sql(
            "network_logs",
            conn,
            if_exists="append",
            index=False
        )

        # -----------------------------------------------
        # Verification
        # -----------------------------------------------

        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM network_logs")

        total_rows = cursor.fetchone()[0]

        print("\n" + "=" * 50)
        print("LOAD SUMMARY")
        print("=" * 50)
        print(f"Rows Loaded          : {total_rows:,}")
        print(f"Database             : {DATABASE_PATH.name}")
        print(f"Table                : network_logs")
        print("=" * 50)

        conn.commit()

    except Exception as e:

        print(f"\nError while loading data:\n{e}")

        conn.rollback()

    finally:

        conn.close()

        print("\nDatabase connection closed.")