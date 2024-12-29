"""
**`data_to_translate_csv.py`**: This script is used to generate a CSV file that contains the data required for translation. The resulting CSV file is designed for contributors who prefer working with spreadsheets (such as Excel or Google Docs) to handle the translation process.

The CSV file will include: **Arabic words** and corresponding **translation fields**. Any additional properties needed specifically for translation purposes.

Parameters:

- **Input file**: The input data file contains all the necessary words, labels, and components used for Yaziji phrase generation.

  The used part is  **"data"** which set (components and their values) that can be utilized in the user interface for translation work.

- **Output file**: Specifies the file path for the resulting CSV file, formatted for translation purposes.
"""
import pandas as pd
import json
from collections import defaultdict
import argparse
import random
def fillna(df):
    # apply on na values
    return df.apply(lambda col: col.fillna('') if col.dtypes == 'object' else col.fillna(0))

# This script generate CSV file for any langauge
# to translate within excel
# generate empty file

def extract_data(input_file):
    try:
        # Read the Excel file
        # to be used for translation

        transtable = {}
        for sheet in [ "words", "features","labels"]:
            df = pd.read_excel(input_file, sheet_name=sheet)
            df = fillna(df)
            transtable[sheet]  = df[["class", "category", "arabic"]]

        # translation join
        result = pd.concat(transtable, axis=0)
        # add translation column
        result["translation"] = result["arabic"]
        return result


    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Convert Excel to JSON.")
    parser.add_argument("input", help="Path to the input Excel file.")
    parser.add_argument("output", help="Path to the output JSON file.")

    # Parse arguments
    args = parser.parse_args()

    # Convert Excel to JSON
    result = extract_data(args.input)
    if result is not None:
        result.to_csv(args.output, sep="\t", encoding="utf-8", index=False)

        print(f"Successfully converted '{args.input}' to '{args.output}'.")
