"""Main entry point for the Python project."""

import pandas as pd
from pathlib import Path


def main():
    file_path = Path("Complete_GOAT_Dataset.xlsx")

    reg_season = pd.read_excel(file_path, sheet_name="reg")
    playoffs = pd.read_excel(file_path, sheet_name="post")

    print("Regular season:")
    print(reg_season.head())

    print("Playoffs:")
    print(playoffs.head())



if __name__ == "__main__":
    main()
