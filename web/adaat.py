#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  adaat.py
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
import json
import os.path
import sys
sys.path.append(os.path.join("../yaziji"))
import logging
import json
import phrase_generator
from db_manager.db_sqlite import RatingOptionsDatabaseSQLite
#
# def DoAction(text, action, options = {}):
#     """
#     do action by name
#     """
#     if action == "DoNothing":
#         return text
#     elif action == "phrase":
#         return build_phrase(options)
#     elif action == "sample":
#         return build_sample(options)
#     elif action == "report":
#         return report(options)
#     elif action == "rating":
#         return rating(options)
#     else:
#
#         return text
#
# def build_phrase(options):
#     phraser = phrase_generator.PhraseGenerator()
#     components = options
#     phrase = phraser.build(components)
#     #~ print(u"".join(["<%s>"%x for x in components.values()]))
#     #~ print(phraser.pattern.stream.__str__())
#     return phrase
#
# def build_sample(options):
#     """generate samples"""
#     return repr(options).replace(",", ",\n")
#
# def report(options):
#     """report bugs"""
#     return "REPORT; "+repr(options).replace(",", ",\n")
#
#
# def rating(options):
#     """report bugs"""
#     return "RATING; "+repr(options).replace(",", ",\n")

class Adaat:
    def __init__(self):
        # Constructor can be used to initialize any instance variables if needed

        dict_path = os.path.join(os.path.dirname(__file__), "./data/data.new.json")
        # dict_path = os.path.join(os.path.dirname(__file__), "./data/data.json")
        self.phraser = phrase_generator.PhraseGenerator(dict_path=dict_path)

        db_path = os.path.join(os.path.dirname(__file__), "./data/rating.db")
        self.db = RatingOptionsDatabaseSQLite(db_path)
        # self.small_dictionary = self.load_dictionary(dict_path)
        self.phraser.load_dictionary(dict_path)

    # def load_dictionary(self, file_path):
    #     """
    #     load word dictionary
    #     :return:
    #     """
    #     data = {}
    #     with open(file_path, 'r', encoding='utf-8') as json_file:
    #         data = json.load(json_file)
    #     return data

    def do_action(self, text, action, options={}):
        """
        Do action by name
        """
        if action == "DoNothing":
            return text
        elif action == "phrase":
            return self.build_phrase(options)
        elif action == "sample":
            return self.build_sample(options)
        elif action == "report":
            return self.report(options)
        elif action == "rating":
            return self.rating(options)
        else:
            return text
    # def add_features(self, data):
    #     """
    #     Extract Data for each option.
    #     Convert the dict (key, value} into {key, dict}
    #     :param options:
    #     :return:
    #     """
    #     converted = {value: self.small_dictionary.get(value,{}) for value in data.values()
    #                  if self.small_dictionary.get(value,{})}
    #     # clean data
    #
    #     return converted
    def build_phrase(self, options):
        """
        Generate phrase
        """
        components = options
        # featured_data = self.add_features(options)
        # logging.info(f"FEATURED:{featured_data}")
        # print(f"FEATURED:",featured_data)
        result_dict = self.phraser.build(components)
        # result_dict = self.phraser.build(components, featured_data)
        # phrase = result_dict.get("phrase")
        return result_dict

    def build_sample(self, options):
        """
        Generate samples
        """
        result = self.build_phrase(options)
        new_options  = options.copy()
        new_options.update(result)
        logging.info(f"{new_options},")
        return repr(new_options).replace(",", ",\n")

    def report(self, options):
        """
        Report bugs
        """
        rating = -1
        self.db.insert_record(rating, options)
        return "REPORT; " + repr(options).replace(",", ",\n")

    def rating(self, options):
        """
        Report rating
        """
        rating = options.get("rating",5)
        try:
            rating = int(rating)
        except:
            rating = 0
        self.db.insert_record(rating, options)
        return "RATING; " + repr(options).replace(",", ",\n")

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
