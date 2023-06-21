#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  components_set.py
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
import random


import libqutrub.verb_const as vconst
import yaziji_const

class componentsSet:
    """
    A class to generate random data
    """
    def __init__(self,):
        self.subjects = [u"", u"أَحْمَد", u"وَلَدٌ"] + list(vconst.PronounsTable)
        self.objects = [u"", u"حَلِيبٌ", u"بَابٌ"] + list(vconst.PronounsTable) 
        self.verbs = [ u"", u"شَرِبَ",
            u"ضَرَبَ",
            u"ذَهَبَ",
            u"جَلَسَ",
        ]
        self.times = [u""] + list(yaziji_const.TENSES.keys()) 
        self.places = [u"", u"بيت", u"سوق", u"مدرسة"]
        self.tenses = [vconst.TensePast,
                        vconst.TenseFuture, 
                        vconst.TenseImperative,      
        ]
        self.voices = [u"معلوم", u"مبني للمجهول"]
        self.auxiliaries = [u"", u"اِسْتَطَاعَ",
        u"أَرَادَ",
        u"كَادَ",
        ]
        self.negative = [u"مثبت", u"منفي"]        
        self.comp={
            "subject":self.subjects,
            "object":self.objects,
            "verb":self.verbs,
            "time":self.times,
            "place":self.places,
            "tense":self.tenses,
            "voice":self.voices,
            "auxiliary":self.auxiliaries,
            "negative":self.negative,
            "phrase_type":[u"جملة فعلية", u"جملة اسمية",
            ],
            
        }   
        # order of displaying keys
        self.comp_keys_order = [
            "phrase_type",
            "separator",            
            "subject",
            "separator",            
            "auxiliary",
            "verb",
            "tense",
            "voice",
            "negative",
            "separator",
            "object",
            "time",
            "place",
        ]
    def load(self,filename):
        """
        load data from file
        """
        pass
    def get_translation(self, word):
        """
        get translation for word
        """
        return yaziji_const.TRANSLATION.get(word, word)
        
    def get_random(self, limit=1):
        """ generate random phrase"""
        
        list_comp = []
        for i in range(limit):
            random_comp={}
            for key in self.comp:
                random_comp[key] = random.choice(self.comp[key])
            list_comp.append(random_comp)
        return list_comp
    
    def generate_select(self,):
        """
         generation select options
        """
        text = ""     
        for key in self.comp_keys_order:
            if key == "separator":
                text += "<br/>"
            else:
                text += u"%s: "%self.get_translation(key)
                text += u"<select id='%s'  class='form-inline' name='%s'>\n"%(key, key)
                text += u"\n".join(["\t<option>%s</option>"%x for x in self.comp[key]])
                text += u"\n</select>\n"
        return text
def main(args):
    dataset = componentsSet()
    text = dataset.generate_select()
    #print(text)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))        
