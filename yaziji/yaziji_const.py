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
import pyarabic.araby as araby

FATHA_WORD = "فتحة"
DAMMA_WORD = "ضمة"
KASRA_WORD = "كسرة"

PRONOUNS_INDEX = {
    'متكلم': {
        'مذكر': {
            'مفرد': 'أنا',
            'جمع': 'نحن'
        },
        'مؤنث': {
            'مفرد': 'أنا',
            'جمع': 'نحن'
        }
    },
    'مخاطب': {
        'مذكر': {
            'مفرد': 'أنت',
            'مثنى': 'أنتما',
            'جمع': 'أنتم'
        },
        'مؤنث': {
            'مفرد': 'أنتِ',
            'مثنى': 'أنتما مؤ',
            'جمع': 'أنتن'
        }
    },
    'غائب': {
        'مذكر': {
            'مفرد': 'هو',
            'مثنى': 'هما',
            'جمع': 'هم'
        },
        'مؤنث': {
            'مفرد': 'هي',
            'مثنى': 'هما مؤ',
            'جمع': 'هن'
        }
    }
}

# Define constants for gender and number types
GENDER_FEMALE = "مؤنث"
GENDER_MALE = "مذكر"
NUMBER_SINGULAR = "مفرد"
NUMBER_DUAL = "مثنى"
NUMBER_PLURAL = "جمع"
NUMBER_IRRGULAR_PLURAL = "جمع تكسير"
MARFOU3 = "مرفوع"
MANSOUB = "منصوب"
MAJROUR = "مجرور"
DEFINED = "تعريف"

VERB_TYPE = "فعل"
NOUN_TYPE = "اسم"
ADVERB_TYPE = "ظرف"

PASSIVE_VOICE = "مبني للمجهول"
ACTIVE_VOICE = "معلوم"
NEGATIVE = "منفي"
AFFIRMATIVE = "مثبت"
VERBAL_PHRASE  = "جملة فعلية"
NOMINAL_PHRASE = "جملة اسمية"
HIDDEN ="مخفي"


PARTICAL_LAM = "لَمْ"
PARTICAL_LAN = "لَنْ"
PARTICAL_LA = "لا"
PARTICAL_FI = "فِي"
PARTICAL_AN = 'أَنْ'

TRANSITIVE_COMMON ="مشترك"
TRANSITIVE_INDIRECT ="متعدي بحرف"
TRANSITIVE_DOUBLE ="متعدي لمفعولين"
TRANSITIVE_INTRANSITIVE ="لازم"
TRANSITIVE_TYPE_VALUES = [TRANSITIVE_COMMON , TRANSITIVE_INDIRECT, TRANSITIVE_DOUBLE, TRANSITIVE_INTRANSITIVE]

ENCLITICS = {vconst.PronounAna : u"ني",
            vconst.PronounNahnu : u"نا",
            vconst.PronounAnta : u"ك",
            vconst.PronounAnti : u"ك", #u"كِ",
            vconst.PronounAntuma : u"كما",
            vconst.PronounAntuma_f : u"كما",
            vconst.PronounAntum : u"كم",
            vconst.PronounAntunna : u"كن",
            vconst.PronounHuwa : u"ه",
            vconst.PronounHya : u"ها",
            vconst.PronounHuma : u"هما",
            vconst.PronounHuma_f : u"هما",
            vconst.PronounHum : u"هم",
            vconst.PronounHunna : u"هن",
        }
        
TENSES = {
        # future
        u"غَدًا": vconst.TenseFuture,
        u"الْيَوْمَ": vconst.TenseFuture,
        u"كُلَّ يَوْمٍ": vconst.TenseFuture,
        u"دَائِمًا": vconst.TenseFuture,
        u"أَحْيَانًا": vconst.TenseFuture,
        u"بَعْدَ غَدٍ": vconst.TenseFuture,
        # past
        u"الْبَارِحَةَ": vconst.TensePast,
        u"أَمْسِ": vconst.TensePast,
        u"أَوَّلَ أَمْسِ": vconst.TensePast,
        # neutral
        u"صَبَاحًا": "",
        u"مَسَاءً": "",
        }

TRANSLATION={
            "subject":u"فاعل",
            "object":u"مفعول",
            "verb":u"فعل",
            "time":u"ظرف زمان",
            "place":u"ظرف مكان", 
            "tense":u"زمن",
            "voice":u"مبني للمعلوم/مجهول",
            "auxiliary":u"فعل مساعد",
            "negative":u"مثبت/منفي",
            u"phrase_type":u"نوع الجملة",
        }

STREAMS= {
    "default": ["auxiliary",
        "subject", 
        "negation",
        "verb",
        "object",
        "place",
        "time",
        ],
    u"جملة اسمية": ["subject",
    "auxiliary",
        "negation",
        "verb",
        "object",
        "place",
        "time",
        ],
    u"جملة فعلية":
        ["auxiliary",
        "subject", 
        "negation",
        "verb",
        "object",
        "place",
        "time",
        ],
    }

SPECIAL_VOCALIZED ={
    u'أنا': u'أَنَا',
u'نحن': u'نَحْنُ',
u'أنت': u'أَنْتَ',
u'أنتِ': u'أَنْتِ',
u'أنتما': u'أَنْتُمَا',
u'أنتما مؤ': u'أَنْتُمَا',
u'أنتم': u'أَنْتُمْ',
u'أنتن': u'أَنْتُنَّ',
u'هو': u'هُوَ',
u'هي': u'هِي',
u'هما': u'هُمَا',
u'هما مؤ': u'هُمَا',
u'هم': u'هُمْ',
u'هن': u'هُنَّ',
}

AUXILIARY= {
     u"اِسْتَطَاعَ":araby.KASRA,
        u"أَرَادَ": araby.KASRA,
        u"كَادَ":araby.FATHA,
    
}

TIME_ADVERB_INFLECTION = "ظرف زمان منصوب على الظرفية"
STATIC_INFLECTION= {
PARTICAL_LA : "حرف نهي جازم",
PARTICAL_LAM: "حرف جزم",
PARTICAL_LAN: "حرف نصب",
PARTICAL_AN: "حرف نصب",
PARTICAL_FI : "حرف جر",
    "أَمْسِ": "ظرف زمان مبني على الكسر في محل نصب على الظرفية",
   "دَائِمًا":TIME_ADVERB_INFLECTION,
    "أَوَّلَ أَمْسِ":TIME_ADVERB_INFLECTION,
    "الْبَارِحَةَ":TIME_ADVERB_INFLECTION,
    "أَحْيَانًا":TIME_ADVERB_INFLECTION,
    "بَعْدَ غَدٍ":TIME_ADVERB_INFLECTION,
    "مَسَاءً":TIME_ADVERB_INFLECTION,
    "الْيَوْمَ":TIME_ADVERB_INFLECTION,
    "غَدًا":TIME_ADVERB_INFLECTION,
    "صَبَاحًا":TIME_ADVERB_INFLECTION,
    "كُلَّ يَوْمٍ":TIME_ADVERB_INFLECTION,
    "البَارِحَةَ":TIME_ADVERB_INFLECTION,
    "اليَوْمَ":TIME_ADVERB_INFLECTION,
    "سَاعَةً":TIME_ADVERB_INFLECTION,
    "سَنَةً":TIME_ADVERB_INFLECTION,
    "شِتَاءً":TIME_ADVERB_INFLECTION,
    "صَيْفًا":TIME_ADVERB_INFLECTION,
    "ظُهْرًا":TIME_ADVERB_INFLECTION,
    "عَصْرًا":TIME_ADVERB_INFLECTION,
    "فَجْرًا":TIME_ADVERB_INFLECTION,
    "لَحْظَةَ":TIME_ADVERB_INFLECTION,
    "لَيْلًا":TIME_ADVERB_INFLECTION,
    "نَهْارًا":TIME_ADVERB_INFLECTION
}


SUBJECT_FUNCTION = "فاعل/مبتدأ"
VERBAL_SUBJECT_FUNCTION = "فاعل"
OBJECT_FUNCTION = "مفعول به"
PASSIVE_SUBJECT_FUNCTION = "نائب فاعل"
ADJECTIVE_FUNCTION = "فاعل"
NOMINAL_SUBJECT_FUNCTION = "مبتدأ"
PREDICATE_FUNCTION = "خبر"


NODES_CONFIG = {
   # features
   "phrase_type":{
      "type":"feature",
      "conjugable":False,
      "wordtype":"",
      "required":True
   },
   "tense":{
      "type":"feature",
      "conjugable":False,
      "wordtype":"",
      "required":False
   },
   "voice":{
      "type":"feature",
      "conjugable":False,
      "wordtype":"",
      "required":False
   },
   "negative":{
      "type":"feature",
      "conjugable":False,
      "wordtype":"",
      "required":False
   },
   # words
   "subject":{
      "type":"word",
      "conjugable":True,
      "wordtype":NOUN_TYPE,
       "function": SUBJECT_FUNCTION,  # initial function
      "required":False,
   },
   "object":{
      "type":"word",
      "conjugable":True,
      "wordtype":NOUN_TYPE,
      "function": OBJECT_FUNCTION,  # initial function
      "required":False
   },
   "verb":{
      "type":"word",
      "conjugable":True,
      "wordtype":VERB_TYPE,
      "required":False
   },
   "auxiliary":{
      "type":"word",
      "conjugable":True,
      "wordtype":VERB_TYPE,
      "required":False
   },
   "time":{
      "type":"word",
      "conjugable":False,
      "wordtype":ADVERB_TYPE,
      "required":False
   },
   "place":{
      "type":"word",
      "conjugable":True,
      "wordtype":NOUN_TYPE,
      "required":False
   },
   "adjective":{
      "type":"word",
      "conjugable":True,
      "wordtype":NOUN_TYPE,
      "function": ADJECTIVE_FUNCTION,
      "required":False
   }
}