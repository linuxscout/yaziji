from libqutrub.verb_const import TenseImperative,  TensePast, TensePassivePast, TenseFuture
from libqutrub.verb_const import  ImperativePronouns, PronounsTable


# Local libraries

from yaziji_const import VERBAL_PHRASE, NOMINAL_PHRASE
from yaziji_const import ACTIVE_VOICE, PASSIVE_VOICE, AFFIRMATIVE, NEGATIVE
import os
import json
import logging
import random

class WordDictionary:
    """
    A class to generator
    """
    def __init__(self, dict_path=""):
        #load default word_dictionary
        if not dict_path:
            dict_path = os.path.join(os.path.dirname(__file__), "./data/data.json")
        self.dict_path = dict_path
        self.small_dictionary = self.load_dictionary(dict_path)

    def load_dictionary(self, file_path):
        """
        load word dictionary
        :return:
        """
        data = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            logging.info(f"Success: Small dictionary loaded from {file_path}")
        except:
            logging.info(f"ERROR: Can't Open small dictionary file {file_path}")
            return None
        return data

    def add_features(self, data):
        """
        Extract Data for each option.
        Convert the dict (key, value} into {key, dict}
        :param options:
        :return:
        """
        mydict = self.small_dictionary.get("wordindex",{})
        # mydict = self.small_dictionary
        featured = {value: mydict.get(value,{}) for value in data.values()
                     if mydict.get(value,{})}

        return featured

    def sample(self):
        """
        randomize data from a dict of list
        :param data:
        :return:
        """

        if not self.small_dictionary:
            return {}
        data = self.small_dictionary.get("data",{})
        return {key: random.choice(value) for key, value in data.items()}

