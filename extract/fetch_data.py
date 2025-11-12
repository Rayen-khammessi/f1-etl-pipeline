import fastf1
import pandas as pd
import os

def fetch_race_data(year: int, grand_prix: str):
    """
    Fetch race results and driver data for a given F1 event using FastF1.
    """
    print(f"Extracting Formula 1 data for {grand_prix} {year}...")

    fastf1.Cache.enable_cache('data/raw')  # enables local caching to avoid re-downloading

    # Load the session 
    session = fastf1.get_session(year, grand_prix, 'R')
    session.load()

    # Get the race results
    results_df = session.results

    os.makedirs("data/raw", exist_ok=True)
    results_df.to_csv(f"data/raw/{grand_prix.lower()}_{year}_results.csv", index=False)

    print(f"Race results saved to data/raw/{grand_prix.lower()}_{year}_results.csv")

    return results_df


