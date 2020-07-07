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
        u"غدا": vconst.TenseFuture,
        u"اليوم": vconst.TenseFuture,
        u"كل يوم": vconst.TenseFuture,
        u"دائما": vconst.TenseFuture,
        u"أحيانا": vconst.TenseFuture,
        u"بعد غد": vconst.TenseFuture,
        # past
        u"البارحة": vconst.TensePast,
        u"أمس": vconst.TensePast,
        u"أول أمس": vconst.TensePast,
        # neutral
        u"صباحا": vconst.TensePast,
        u"مساء": vconst.TensePast,
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
        }
