#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
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
#~ sys.path.append(os.path.join("../"))

import phrase_generator

def build_phrase(options):        
    phraser = phrase_generator.PhraseGenerator()
    components = options
    phrase = phraser.build(components)
    print(u"".join(["<%s>"%x for x in components.values()]))
    print(phraser.pattern.stream.__str__())
    return phrase
def main(args):
    dataset =[
    {
    'place': 'السوق', 'negative': 'منفي', 'voice': 'مبني للمجهول', 'subject': 'أنت', 'auxiliary': '', 'tense': 'المضارع المعلوم', 'verb': 'ضَرِبَ', 'action': 'sample', 'object': 'بَابٌ', 'text': 'أنت', 'time': 'كل يوم'
    },
    
    
    {'verb': 'شَرِبَ', 'time': 'دائما', 'subject': 'هو', 'text': 'هو', 'auxiliary': 'َاِسْتَطَاع', 'tense': 'المضارع المعلوم', 'voice': 'معلوم', 'object': 'حَلِيبٌ', 'action': 'sample', 'place': 'بيت', 'negative': 'مثبت'},
    ]
    for data in dataset:
        p = build_phrase(data)
        print(data)
        print(p)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
