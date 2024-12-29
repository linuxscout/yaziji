"""
This script is used to build a JSON file containing a dictionary of data for the phrase generator. The resulting JSON file serves multiple purposes, including:

- Storing **word attributes**, **phrase components features**, and **fields** required for phrase generation.
- Generating a **"data" structure** (components and their values) that can be used in the user interface without directly modifying the core data.
- The output JSON file will be used by the **`PhraseGenerator`** class as a dictionary to facilitate phrase generation.
- It allows you to use the data in the **web API** or other interfaces, ensuring that the core data remains unaltered.

Parameters:

- **Input file**: The input data file contains all the necessary words, labels, and components used for Yaziji phrase generation.
- **Output file**: Specifies the file path for the resulting JSON file.
"""
import pandas as pd
import json
from collections import defaultdict
import argparse
import random
def fillna(df):
    # apply on na values
    return df.apply(lambda col: col.fillna('') if col.dtypes == 'object' else col.fillna(0))
def read_sheet(input_file, sheet):
    df = pd.read_excel(input_file, sheet_name=sheet)
    df = fillna(df)
    trans_data = df[["class", "category", "arabic"]]
    trans_data["translation"] = trans_data["arabic"]
    # Convert defaultdict to a regular dictionary (optional)
    grouped_data = defaultdict(list)
    for _, row in df.iterrows():
        grouped_data[row["category"]].append(row["arabic"])
    return dict(grouped_data)

def randomize(data):
    """
    randomize data from a dict of list
    :param data:
    :return:
    """
    return {key: random.choice(value) for key, value in data.items()}

def extract_data(input_file):
    try:
        # Read the Excel file
        datatable = {}
        df = pd.read_excel(input_file, sheet_name="words")
        df = fillna(df)

        # to be used for translation
        trans_data_words = df[["class","category", "arabic"]]
        df_words = df.set_index("arabic")
        # Convert the DataFrame to JSON
        # json_data['wordindex'] = df_words.to_json(orient="index", force_ascii=False, indent=4)
        datatable['wordindex'] = df_words.to_dict(orient="index")



        for sheet in [ "words", "features","labels"]:
            datatable[sheet] = read_sheet(input_file, sheet)

        # Rename the key
        datatable["data"] = datatable.pop("words")
        # update data
        for key, value in  datatable['features'].items():
            if not value:
                value = ['']
            if key in datatable['data']:
                datatable['data'][key].append(value[0])
            else:
                datatable['data'][key] = value
        # json_data['data'].update(dict(grouped_data))

        datatable['names'] = list(datatable["data"].keys())

        return datatable
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
    datatable = extract_data(args.input)
    if datatable:
        print(datatable)
        # Write the JSON data to the output file
        # Convert dictionary to JSON and save to a file
        with open(args.output, 'w', encoding='utf-8') as json_file:
            json.dump(datatable, json_file, ensure_ascii=False, indent=4)

        # randomized sample
        print("SAMPLE", randomize(datatable["data"]))
        print(f"Successfully converted '{args.input}' to '{args.output}'.")