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
class streamPattern:
    """
    a class to handle pattern stream order
    """
    def __init__(self, stream_list):
        self.stream = stream_list
    
    def add(self, attribute, before="", after=""):
        """
        add an attribute after or before another attribute
        """
        pass
    def remove(self, name):
        """
        remove a component from stream
        """
        if name in self.stream:
            self.stream.remove(name)
    def __list__(self,):
        """
        list of content
        """
        return list(self.stream)

    def __str__(self,):
        """
        str of content
        """
        return (u"".join(["<%s>"%x for x in self.stream]))
        #~ return u" ".join(self.stream)
    
class PhrasePattern:
    """
    A class to generator
    """
    def __init__(self):
        
        self.stream = streamPattern(["subject", 
        "verb",
        "object",
        "time",
        "place",
        ])
    
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
        # extract tense
        tense = vconst.TensePast
        # extract pronoun
        pronoun = self.get_pronoun(self.subject)
        transitive = True
        future_type = araby.FATHA
        vbc = libqutrub.classverb.VerbClass(self.verb, transitive,future_type) 
        self.verb_conjugated = vbc.conjugate_tense_for_pronoun(tense, pronoun)

        if self.is_pronoun(self.subject):
            self.stream.remove("subject")

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
        #~ phrase = [self.subject, self.verb_conjugated, self.predicate, self.time_circumstance, self.place_circumstance]
        phrase = u" ".join(phrase)
        return phrase
        

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
