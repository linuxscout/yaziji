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
import random

import libqutrub.verb_const as vconst

import phrase_pattern
class PhraseGenerator:
    """
    A class to generator
    """
    def __init__(self):
        
        self.pattern = phrase_pattern.PhrasePattern()
    
    def build(self, table_compononts):
        """
        
        """
        self.pattern.add_components(table_compononts)
        self.pattern.prepare()
        phrase = self.pattern.build()
        return phrase
class componentsSet:
    """
    A class to generate random data
    """
    def __init__(self,):
        self.subjects = vconst.PronounsTable
        self.objects=[u"حليب"]
        self.verbs=[u"شَرِبَ"]
        self.times=[u"غدا"]
        self.places=[u"بيت"]
    
    def load(self,filename):
        """
        load data from file
        """
        pass
        
    def get_random(self,):
        """ generate random phrase"""
        comp={
            "subject":random.choice(self.subjects),
            "object":random.choice(self.objects),
            "verb":random.choice(self.verbs),
            "time":random.choice(self.times),
            "place":random.choice(self.places),
        }
        return comp
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    phraser = PhraseGenerator()
    dataset = componentsSet()
    components = dataset.get_random()
    phrase = phraser.build(components)
    print(u"".join(["<%s>"%x for x in components.values()]))
    print(phraser.pattern.stream.__str__())
    print(phrase)
    sys.exit(main(sys.argv))
