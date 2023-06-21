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
import components_set
class PhraseGenerator:
    """
    A class to generator
    """
    def __init__(self):
        
        self.pattern = phrase_pattern.PhrasePattern()
    
    def build(self, table_compononts):
        """
        
        """
        # Try to add components to prepare the phrase,
        # if there are some errors, response will be negative
        # else : build phrase within phrase_pattern module
        response = self.pattern.add_components(table_compononts)
        if response < 0:
            phrase = self.error_message(response)
        else:
            self.pattern.prepare()
            phrase = self.pattern.build()
            phrase  += "[%s]"%self.pattern.phrase_type

        return phrase

    def error_message(self, error_no):
        if error_no == -1:
            return "Imperative Tense Incompatible with pronoun"
        else:
            return "Input Error"

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
