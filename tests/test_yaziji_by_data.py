import unittest
from unittest.mock import MagicMock

from libqutrub.verb_const import TenseImperative,  TensePast, TensePassivePast, TenseFuture
from libqutrub.verb_const import  ImperativePronouns, PronounsTable

import sys, os
# Local libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "./lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../yaziji"))

from yaziji.yaziji_const import VERBAL_PHRASE, NOMINAL_PHRASE
from yaziji.yaziji_const import ACTIVE_VOICE, PASSIVE_VOICE, AFFIRMATIVE, NEGATIVE
import pandas as pd
import json
from yaziji.phrase_generator import PhraseGenerator

from utils import open_file

class TestPhraseGenerator(unittest.TestCase):
    def setUp(self):
        self.phrase_generator = PhraseGenerator()
        self.dataset = []
        # Path to your JSON file
        file_path = os.path.join(os.path.dirname(__file__), "samples/samples40.json")

        # Open and load the JSON file
        with open(file_path, "r") as file:
            self.dataset = json.load(file)

    def get_components(self,original_dict):
        """
        prepare a tuple to be used as components
        :param tuple:
        :return:
        """
        keys_to_exclude = ('phrase', 'inflection', 'errors', "valid")

        # Build a new dictionary without the excluded keys
        filtered_dict = {key: value for key, value in original_dict.items() if key not in keys_to_exclude}
        return filtered_dict

    # @unittest.skip("Test later")
    def test_build_error_success(self):
        # Arrange
        test_set = self.dataset
        for num, item in enumerate(test_set):
            components = self.get_components(item)
            result = self.phrase_generator.build(components)
            phrase = result.get("phrase",'')
            if  item["valid"]:
                self.assertEqual(phrase , item["phrase"],
                             msg=f"\nResult  :{result}\nExpected:{item['phrase']}")  # Should return True if preparation is successful
            if  not item["valid"]:
                self.assertNotEqual(phrase , item["phrase"],
                             msg=f"\nResult  :{result}\nExpected:{item['phrase']}")  # Should return True if preparation is successful

    # @unittest.skip("Test later")
    def build_dataframe(self, dataframe):
        # Arrange
        df = dataframe
        # treat data
        exclude_columns = ['phrase', 'inflection', 'errors', "valid"]

        # Select columns except the excluded ones
        columns_to_apply = df.columns.difference(exclude_columns)
        # print(columns_to_apply)
        # Apply an operation (e.g., multiply by 2) on the selected columns
        # df["output"] = df[columns_to_apply].apply(build_phrase, axis=1)
        # result = df[columns_to_apply].apply(lambda x: self.phrase_generator.build(dict(x)), axis=1)
        result = df[columns_to_apply].apply(self.phrase_generator.build, axis=1)
        # Convert the resulting Series of dicts into a DataFrame and concatenate
        expanded_columns = pd.DataFrame(result.tolist())
        # Add a prefix to column names
        expanded_columns = expanded_columns.add_prefix("out_")
        df = pd.concat([df, expanded_columns], axis=1)

        # test if the phrases are equal and valid is true,
        # if valid is false, phrases must not be equal
        df["eval"] = df.apply(lambda x: bool(x['phrase'] == x["out_phrase"])==x['valid'], axis=1)
        return df

    def test_build_data_samples(self,):
        # Arrange
        test_set = [
            {"filename":"samples/samples40.json",
             "outfile":"output/samples40.csv",
             },
            {"filename": "samples/samples40.xlsx",
             "outfile": "output/samples40.xlsx.csv",
             }
            ]
        for item in test_set:
            df = open_file(item['filename'])

            self.assertIsNotNone(df, msg=f"\nCan't Open file Data '{item['filename']}'")
            df_out = self.build_dataframe(df)
            df_out.to_csv(item['outfile'], encoding="utf8", sep="\t")
            # count a number of eval error
            error_count = (df_out["eval"] == False).sum()
            # assert if there are errors
            self.assertEqual(error_count,0,
                         msg=f"\nThere are errors in Data '{item['filename']}', Fetch output file '{item['outfile']}'")  # Should return True if preparation is successful

    @unittest.skip("Test later")
    def test_build_error_handling(self):
        # Arrange
        test_set=[]
        for item in test_set:
            result = self.phrase_generator.build(item["components"])
            phrase = result.get("phrase",'')
            errors = result.get("errors",'')
            self.assertEqual(phrase == item["phrase"], item["valid"],
                             msg=f"\nResult  :{result}\nExpected:{item['phrase']}")
            self.assertEqual(errors == item["error"], item["valid"],
                             msg=f"\nResult  :{errors}\nExpected:{item['error']}")

if __name__ == '__main__':
    unittest.main()
