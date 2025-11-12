import pandas as pd
import os

def clean_results_data(results_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform the race results DataFrame.
    Keep only relevant columns and ensure consistent naming.
    """
    print("Transforming and cleaning race data...")

    # Select useful columns 
    cols_to_keep = [
        'DriverNumber', 'Abbreviation', 'FullName', 'TeamName',
        'Position', 'GridPosition', 'Status', 'Points'
    ]

    # Filter to keep only the columns that exist in the DataFrame
    available_cols = [col for col in cols_to_keep if col in results_df.columns]
    df_clean = results_df[available_cols].copy()

    # Rename columns to snake_case for consistency
    df_clean.rename(columns={
        'DriverNumber': 'driver_number',
        'Abbreviation': 'driver_code',
        'FullName': 'driver_name',
        'TeamName': 'team',
        'Position': 'final_position',
        'GridPosition': 'grid_position',
        'Status': 'status',
        'Points': 'points'
    }, inplace=True)

    # Sort by final position (ascending)
    df_clean.sort_values(by='final_position', inplace=True)

    # Reset index
    df_clean.reset_index(drop=True, inplace=True)

    # Create the processed folder if it doesn't exist
    os.makedirs("data/processed", exist_ok=True)

    # Save clean CSV file
    clean_path = "data/processed/clean_results.csv"
    df_clean.to_csv(clean_path, index=False)
    print(f"Clean data saved to {clean_path}")

    return df_clean
