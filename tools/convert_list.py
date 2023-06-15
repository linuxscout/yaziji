#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# convert_list.py
#  
#  Copyright 2023 zerrouki <zerrouki@majd4>
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
import pyarabic.araby as araby
def treat_text(text):
    """
    Convert given texts into tokens and make a list
    """
    tokens = araby.tokenize(text)

    # uniq
    tokens = list(set(tokens))
    # remove non arabic words
    tokens = [tok for tok in tokens if araby.is_arabicword(tok)]
    # sort tokens
    # ~ print("Befort sort")
    # ~ print("\n".join(tokens))
    tokens.sort()
    # ~ print("After sort")
    # ~ print("\n".join(tokens))
   
    for token in tokens:
        print('"%s":_("%s"),'%(token, token))
    
    
def main(args):
    #verbs 
    # ~ text ="""قَامَ – قَعَدَ– أَكَلَ- شَرِبَ- جَهَّزَ- وَجَدَ- قَالَ- أَخَذَ- وَقَفَ –سَأَلَ-قَرَأَ- وَضَعَ- فَتَحَ- ضَرَبَ –جَلَسَ- شَكَرَ –عَلِمَ- رَكَعَ-سَجَدَ – فَهِمَ- وَعَدَ-صَامَ –عَاشَ- بَكَى- جَعَلَ- حَدَّثَ- خَبَّرَ-أَعْلَمَ- عَطِشَ- شَبِعَ- ذَهَبَ- خَرَجَ- كَتَبَ- رَمَى- نَامَ –بَاعَ- دَخَلَ- جَرَى- سَمِعَ- كَسَرَ- غَفَرَ- وَفَى- سَاعَدَ - أَخْبَرَ- اجْتَهَدَ- جَاءَ- شَاهَدَ- مَاتَ- رَسَبَ- لَبِسَ- رَسَمَ- نَجَحَ- سَافَرَ- نَزَلَ- طَلَعَ- عَرَفَ- وَصَلَ- لَعِبَ- سَكَنَ- حَفِظَ-ذَاكَرَ- تَعَلَّمَ-أَسْرَعَ- مَشَى- اشْتَرَى- قَبَضَ
    # ~ """
    # subjects
    text ="""وَلَدٌ
بِنْتٌ
طَالِبٌ
تِلْمِيذٌ
أُمٌّ
أَبٌ
أَسَدٌ
اِبْنٌ
طِفْلٌ
معَلِّمٌ
طَبِيبٌ
مُجْتَهِدٌ
رَجُلٌ
مَرْأَةٌ
مُهَنْدِسٌ
شُرْطِيٌّ
تَاجِرٌ
مُسْلِمٌ
قَاضٌِ
عُمَّالٌ
عَامِلٌ
مَطَرٌ
فَرَاشَةٌ
رَضِيعٌ
زُهُورٌ
دِيكٌ
حِصَانٌ
قِطٌّ
مُحَمَدُ
أَحْمَدُ
لَيْلَى
فَاطِمَةُ

    """
    
    # objects
    text = """تُفَاحَةٌ
طَعَامٌ
حَلِيبٌ
صَحْرَاءٌ
دَرْسٌ
قِطَّةٌ
مُعَلِمٌ
رَجُلٌ
لمْرأَةٌ
مسْرَحِيَّةٌ
قِصَّةٌ
قَمَرٌ
جَبَلٌ
عَصِيرٌ
مدْرَسةٌ
قُرْآنٌ
حَقِيبَةٌ
تِلْمِيذٌ
طَلَبَةٌ
كِتَابٌ
ثَوْبٌ
شَعْرٌ
صَوْتٌ
كَأْسٌ
نَاسٌ
عَلَمٌ
مِحْفَظَةٌ
كُرَةٌ
خُضَرٌ
فَوَاكِهٌ
    """
    # places:
    text= """أَمَاَمَ
وَرَاءَ
فَوْقَ
تَحْتَ
وَسَطَ
خَلْفَ
بَيْنَ
حَوْلَ
دَاخِلَ
خَارِجَ
يَمِينَ
يَسَارَ
شَرْقَ
غَرْبَ
جَنُوبَ
شَمَالَ"""
    # ~ text="""
# ~ سُوقٌ
# ~ بَيْتٌ
# ~ حَدِيقَةٌ
# ~ مَدْرَسَةٌ
# ~ مَدِينَةٌ
# ~ طَرِيقٌ
# ~ فِنَاءٌ
# ~ غُرْفَةٌ
# ~ مَطْبَخٌ
# ~ مَسْجِدٌ

    # ~ """
    #time
    text= """
      غَدًا-أَمْسِ- صَبَاحًا- ظُهْرًا- سَنَةً- سَاعَةً- صَيْفًا- شِتَاءً- رَبِيعَ-اليَوْمَ- دَائِمًا-أَوَّلَ أَمْسِ-البَارِحَةَ-أَحْيَانًا- بَعْدَ غَدٍ- مَسَاءً- كُلَّ يَومٍ- قَبْلَ- بَعْدَ-أَثْنَاءَ- وَقْتَ- عَامٍ- فَجْرًا- عَصْرًا- نَهْارًا- لَيْلًا- لَحْظَةَ    
    """
    
    # adjectives
    text = """سَعِيدٌ- حَزِينٌ- سَرِيعٌ- بَطِيءٌ- جَمِيلٌ- بَشِعٌ- ذَكِيٌ- غَبِيٌ- كَسُولٌ- مُجْتَهِدٌ- شُجَاعٌ-ضَعِيفٌ- قَوِيٌ-مَسْرُورٌ- فَرِحٌ- وَسِيمٌ- مُبْتَهِجٌ- لَئِيمٌ- حَنُونٌ- أَنِيقٌ- طَوِيلٌ- قَصِيرٌ- هَزِيلٌ- سَمِينٌ- كَرِيمٌ- بَخِيلٌ- مُرْتَفِعٌ- مُنْخَفِضٌ
    """
    treat_text(text)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
