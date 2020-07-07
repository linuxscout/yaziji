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
import pyarabic.araby as araby
import alyahmor.verb_affixer

import yaziji_const
import stream_pattern
class PhrasePattern:
    """
    A class to generator
    """
    def __init__(self):
        
        self.stream = stream_pattern.streamPattern(["subject", 
        "verb",
        "object",
        "time",
        "place",
        ])
        self.verbaffixer = alyahmor.verb_affixer.verb_affixer()
    
    def add_subject(self, subject):
        """
        Add a subject to phrase
        """
        self.subject = subject

    def add_predicate(self, an_object):
        """
        Add a object to phrase
        """
        self.predicate = an_object

    def add_auxiliary(self, auxiliary):
        """
        Add a auxiliary to phrase
        """
        self.auxiliary = auxiliary

    def add_place_circumstance(self, circumstance):
        """
        Add a place circumstance to phrase
        """
        self.place_circumstance = circumstance

    def add_time_circumstance(self, circumstance):
        """
        Add a time circumstance to phrase
        """
        self.time_circumstance = circumstance

    def add_verb(self, verb):
        """
        Add a verb to phrase
        """
        self.verb = verb
    def add_components(self, components):
        """
        Add components
        """
        self.add_subject(components.get("subject",""))
        self.add_predicate(components.get("object",""))
        self.add_verb(components.get("verb",""))
        self.add_time_circumstance(components.get("time",""))
        self.add_place_circumstance(components.get("place",""))
    
    def prepare(self,):
        """
        extract more data from components
        """
        #prepare the verb
        # extract tense
        tense = self.get_tense(self.time_circumstance)
        # extract pronoun
        pronoun = self.get_pronoun(self.subject)
        transitive = True
        future_type = araby.FATHA
        vbc = libqutrub.classverb.VerbClass(self.verb, transitive,future_type) 
        self.verb_conjugated = vbc.conjugate_tense_for_pronoun(tense, pronoun)
        
        # if the subject is a pronoun, it will be omitted
        if self.is_pronoun(self.subject):
            self.stream.remove("subject")
            
        # if the object is a pronoun
        if self.is_pronoun(self.predicate):
            v_enclitic = self.get_enclitic(self.predicate)
            #~ self.verb_conjugated += "-" + v_enclitic
            forms = self.verbaffixer.vocalize(self.verb_conjugated, proclitic="", enclitic=v_enclitic)
            self.verb_conjugated = forms[0][0]
            self.stream.remove("object")
    def get_enclitic(self, pronoun):
        """
        Extract enclitic
        """
        return yaziji_const.ENCLITICS.get(pronoun,"")
        
    def get_tense(self, time_word):
        """
        Extract tense from time circomstance
        """
        return yaziji_const.TENSES.get(time_word,"")        
        
    def get_pronoun(self, word):
        """
        get the pronoun of the word
        """
        if word in vconst.PronounsTable:
            return word
        else:
            return vconst.Pronoun_Huwa
    def is_pronoun(self, word):
        """
        get if is pronoun
        """
        return word in vconst.PronounsTable

    def get_component(self, key):
        """
        Select a component by name
        """
        if key == "subject":
            return self.subject
        elif key == "object":
            return self.predicate
        elif key == "verb":
            return self.verb_conjugated
        elif key == "time":
            return self.time_circumstance
        elif key == "place":
            return self.place_circumstance
        return ""

            
        
    def build(self,):
        """
        build a phrase
        """
        # build phrase according to stream
        phrase = []
        for key in self.stream.__list__():
            phrase.append(self.get_component(key))
        phrase = u" ".join(phrase)
        return phrase
        

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
