#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#  Copyright 2020 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
# import random

# import libqutrub.verb_const as vconst

import phrase_pattern
import components_set
import error_listener
import validator
import inflector
import worddictionary
import os
import random
import json
import logging
class PhraseGenerator:
    """
    A class to generator
    """
    def __init__(self, dict_path=""):
        # init error observer
        self.error_observer = error_listener.ErrorListener()
        # self.error_observer = None

        #load default word_dictionary
        # if not dict_path:
        #     dict_path = os.path.join(os.path.dirname(__file__), "./data/data.json")
        self.dict_path = dict_path
        # self.small_dictionary = self.load_dictionary(dict_path)
        self.small_dictionary = worddictionary.WordDictionary(dict_path)
        # the validator use dictionay to validate fields and features
        # the main task is to validate semantic relationship between words
        self.validator = validator.Validator(dictionary=self.small_dictionary,
                                             error_observer=self.error_observer)
        # add error observer to phrase pattern
        self.pattern = phrase_pattern.PhrasePattern(   validator=self.validator
                                            # error_observer=self.error_observer,
                                                )
        self.inflector = inflector.Inflector()

    #
    # def load_dictionary(self, file_path):
    #     """
    #     load word dictionary
    #     :return:
    #     """
    #     data = {}
    #     try:
    #         with open(file_path, 'r', encoding='utf-8') as json_file:
    #             data = json.load(json_file)
    #         logging.info(f"Success: Small dictionary loaded from {file_path}")
    #     except:
    #         logging.info(f"ERROR: Can't Open small dictionary file {file_path}")
    #         return None
    #     return data
    #
    # def add_features(self, data):
    #     """
    #     Extract Data for each option.
    #     Convert the dict (key, value} into {key, dict}
    #     :param options:
    #     :return:
    #     """
    #     mydict = self.small_dictionary.get("wordindex",{})
    #     # mydict = self.small_dictionary
    #     featured = {value: mydict.get(value,{}) for value in data.values()
    #                  if mydict.get(value,{})}
    #
    #     return featured
    #
    # def sample(self):
    #     """
    #     randomize data from a dict of list
    #     :param data:
    #     :return:
    #     """
    #
    #     if not self.small_dictionary:
    #         return {}
    #     data = self.small_dictionary.get("data",{})
    #     return {key: random.choice(value) for key, value in data.items()}


    def load_dictionary(self, file_path):
        """
        load word dictionary
        :return:
        """
        return self.small_dictionary.load_dictionary(file_path)

    def add_features(self, data):
        """
        Extract Data for each option.
        Convert the dict (key, value} into {key, dict}
        :param options:
        :return:
        """
        return self.small_dictionary.add_features(data)

    def sample(self):
        """
        randomize data from a dict of list
        :param data:
        :return:
        """

        return self.small_dictionary.sample()

    def build(self, table_compononts):
        """
        
        """
        # Try to add components to prepare the phrase,
        # if there are some errors, response will be negative
        # else : build phrase within phrase_pattern module
        self.error_observer.reset()
        if not isinstance(table_compononts, dict):
            table_compononts = dict(table_compononts)
        # add a small dictionary that contains words and attributes
        featured_data = self.add_features(table_compononts)
        logging.info(f"FEATURED:{featured_data}")
        # print(f"FEATURED:",featured_data)

        response = self.pattern.add_components(table_compononts, featured_data)
        # print(table_compononts.items)
        # print(type(table_compononts))
        # print(self.error_observer.show_errors_to_string())
        if response < 0:
            # phrase = self.error_message(response)
            #TODO: return an empty phrase with a list of possible errors separatly
            phrase = ""
            inflection =""
        else:
            self.pattern.prepare()
            phrase = self.pattern.build()
            infl_list = self.inflector.inflect_nodes(self.pattern.nodes, self.pattern.stream)
            inflection = self.inflector.to_string(infl_list, sep="<br/>")

        return {"phrase": phrase,
        "phrase_type":self.pattern.phrase_type,
        "inflection": inflection,
        "errors":self.error_observer.show_errors_to_string(sep="<br/>")
        }

    def error_message(self, error_no):

        return self.error_observer.error_message(error_no)
        # error_messages = {
        #     -1: "Imperative Tense Incompatible with pronoun.",
        #     -2: "A required name not found.",
        #     -3: "Unsupported component key.",
        #     -4: "ERROR: Required Phrase type is empty.",
        # }
        # return error_messages.get(error_no, "Input Error")


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    phraser = PhraseGenerator()
    dataset = components_set.componentsSet()
    components = dataset.get_random()
    for comp in components:
        phrase = phraser.build(comp)
        #print(u"".join(["<%s:%s>"%(x,comp[x]) for x in comp]))
        #print(phraser.pattern.stream.__str__())
        #print(phrase)
    sys.exit(main(sys.argv))
