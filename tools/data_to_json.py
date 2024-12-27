import pandas as pd
import json
import argparse

def excel_to_json(input_file, output_file):
    try:
        # Read the Excel file
        df = pd.read_excel(input_file)

        df = df.set_index("arabic")
        # Convert the DataFrame to JSON
        json_data = df.to_json(orient="index", force_ascii=False, indent=4)

        # Write the JSON data to the output file
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)

        print(f"Successfully converted '{input_file}' to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Convert Excel to JSON.")
    parser.add_argument("input", help="Path to the input Excel file.")
    parser.add_argument("output", help="Path to the output JSON file.")

    # Parse arguments
    args = parser.parse_args()

    # Convert Excel to JSON
    excel_to_json(args.input, args.output)
