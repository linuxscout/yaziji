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
def DoAction(text, action, options = {}):
    """
    do action by name
    """
    if action == "DoNothing":
        return text
    elif action == "phrase":
        return build_phrase(options)
        return phrase
    else:

        return text

def build_phrase(options):        
    phraser = phrase_generator.PhraseGenerator()
    #~ dataset = components_set.componentsSet()
    components = options
    #~ values = options.values()
    #~ phrase  = repr(options) #u"+".join(values)
    #~ return phrase
          
    phrase = phraser.build(components)
    print(u"".join(["<%s>"%x for x in components.values()]))
    print(phraser.pattern.stream.__str__())
    return phrase
    
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
