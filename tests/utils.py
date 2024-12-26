import os, sys
import pandas as pd
def open_file(file_path):
    """
    Opens a file based on its extension and loads it into a pandas DataFrame.

    Supported file types:
    - Excel (.xlsx, .xls)
    - OpenDocument Spreadsheet (.ods)
    - CSV (.csv)
    - JSON (.json)

    :param file_path: Path to the file
    :return: pandas.DataFrame
    """
    # Get file extension
    _, file_extension = os.path.splitext(file_path)

    try:
        if file_extension in [".xlsx", ".xls"]:
            # Excel files
            df = pd.read_excel(file_path)
        elif file_extension == ".ods":
            # OpenDocument Spreadsheet files
            df = pd.read_excel(file_path, engine="odf")
        elif file_extension == ".csv":
            # CSV files
            df = pd.read_csv(file_path, encoding="utf8", delimiter="\t", index_col=0)
        elif file_extension == ".json":
            # JSON files
            df = pd.read_json(file_path)
        else:
            raise ValueError(f"Unsupported file extension: {file_extension}")

        print(f"File loaded successfully: {file_path}")
        # df.fillna('', inplace=True)
        df = df.apply(lambda col: col.fillna('') if col.dtypes == 'object' else col.fillna(0))

        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None