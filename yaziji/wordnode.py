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
import libqutrub.verb_const as vconst
import libqutrub.classverb
import libqutrub.verb_db
import pyarabic.araby as araby
import alyahmor.verb_affixer
import alyahmor.noun_affixer
import arramooz.arabicdictionary
from  arramooz.nountuple import NounTuple
from  arramooz.verbtuple import VerbTuple

import yaziji_const
import stream_pattern
class wordNode:
    """
    a word node 
    """
    def __init__(self, name, value, gender="", number="", defined=False):
        """
        Init the word node with a categorical syntax such as verb, noun, adverb, and a value for this category to build a word node,
        inflect the word according to given features
        :param name: an attribute name such as 'Verb', 'auxiliary verb'
        :param value: the word string
        """
        # The word noun category, example (verb, subject,)
        self.name  = name
        # the value as a word string, e.g. "أكل"، "الولد"
        # the given word must be a lemma, not a inflected form
        # for verbs, it must be fully vocalized
        self.value = value
        # vocalized
        self.vocalized = value
        # gender attribute
        self.gender = gender  if gender else "مذكر"
        # number attribute
        self.number = number if number else 1
        # defined attribute
        self.defined = True if defined else False
        # the word form, initially use the lemma
        self.conjugated = value
        # affixes initially empty
        self.prefix = ""
        self.suffix = ""
        self.before = ""
        self.after = ""
        self.tense = ""
        # transitivity for verbs
        self.transitive = "NA"
        # future type
        self.future_type = "NA"

        # if the word will be hidden
        self.hidden = False

    def __str__(self):
        return f"name='{self.name}', value='{self.value}'"

    def set_null(self,):
        """
        Reset the word node
        :return:
        """
        self.value = ""
        self.conjugated = ""
    def hide(self,):
        """
        hide the word node in the output
        :return:
        """
        self.hidden = True
    def unhide(self,):
        """
        unhide the word node in the output
        :return:
        """
        self.hidden = False

    def set_gender(self, gender):
        self.gender = gender

    def set_number(self, number):
        self.number = number

    @property
    def feminin(self):
        return self.gender == "مؤنث"
    @property
    def word(self):
        return self.value

    def is_defined(self):
        return bool(self.defined)

    def update(self, dict_word_tuple):
        wd = dict_word_tuple;
        # general attributes

        # Noun specitic
        if isinstance(wd, NounTuple):
            self.vocalized = wd.get_vocalized()
            self.gender = wd.get_gender()
            self.defined = wd.is_defined()
            self.number = wd.get_number()
        elif isinstance(wd, VerbTuple):
            self.vocalized = wd.get_vocalized()
            self.transitive = wd.is_transitive()
            self.future_type = wd.get_future_type()
        elif isinstance(wd, dict):
            self.vocalized = wd.get("vocalized",self.value)
            self.gender = wd.get("gender","مذكر")
            self.defined = wd.get("defined",False)
            self.number = wd.get("number","مفرد" )
            self.transitive = wd.get("transitive", True)
            self.future_type = wd.get("future_type",araby.FATHA)

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
