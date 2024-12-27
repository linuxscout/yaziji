import pandas as pd
import json
from collections import defaultdict
import argparse
import random
def fillna(df):
    # apply on na values
    return df.apply(lambda col: col.fillna('') if col.dtypes == 'object' else col.fillna(0))


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
