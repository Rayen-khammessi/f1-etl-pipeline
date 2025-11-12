from extract.fetch_data import fetch_race_data
from transform.clean_data import clean_results_data
from load.save_to_db import save_results_to_db

def main():
    print("🏁 Launching Formula 1 ETL Pipeline...")
    
    # Extract
    raw_data = fetch_race_data(year=2023, grand_prix="Monaco")

    # Transform
    df_clean = clean_results_data(raw_data)
    
    # Load
    save_results_to_db(df_clean)

    print("ETL Pipeline completed successfully!")

if __name__ == "__main__":
    main()


