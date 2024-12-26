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
import os.path
import sys
sys.path.append(os.path.join("../yaziji"))

import phrase_generator
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
        self.phraser = phrase_generator.PhraseGenerator()

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

    def build_phrase(self, options):
        """
        Generate phrase
        """
        components = options
        result_dict = self.phraser.build(components)
        # phrase = result_dict.get("phrase")
        return result_dict

    def build_sample(self, options):
        """
        Generate samples
        """
        return repr(options).replace(",", ",\n")

    def report(self, options):
        """
        Report bugs
        """
        return "REPORT; " + repr(options).replace(",", ",\n")

    def rating(self, options):
        """
        Report rating
        """
        return "RATING; " + repr(options).replace(",", ",\n")

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
