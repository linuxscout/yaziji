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
class wordNode:
    """
    a word node 
    """
    def __init__(self, name, value):
        self.name  = name
        self.value = value
        # the word form
        self.conjugated = value
        self.prefix = ""
        self.suffix = ""
        self.before = ""
        self.after = ""
        self.tense = ""

    def set_null(self,):
        self.value = ""
        self.conjugated = ""
        
class PhrasePattern:
    """
    A class to generator
    """
    def __init__(self):
        
        self.stream = stream_pattern.streamPattern(["subject", 
        "auxiliary",
        "negation",
        "verb",
        "object",
        "time",
        "place",
        ])
        self.nodes = {}
        self.verbaffixer = alyahmor.verb_affixer.verb_affixer()
    

    def add_components(self, components):
        """
        Add components
        """
        self.nodes["subject"]  = wordNode("subject", components.get("subject",""))
        self.nodes["object"]   = wordNode("object",  components.get("object",""))
        self.nodes["verb"]     = wordNode("verb",    components.get("verb",""))
        self.nodes["time"]     = wordNode("time",    components.get("time",""))
        self.nodes["place"]    = wordNode("place",   components.get("place",""))
        self.nodes["tense"]    = wordNode("tense",   components.get("tense",""))
        self.nodes["negative"] = wordNode("negative", components.get("negative",""))
        self.nodes["voice"]    = wordNode("voice",   components.get("voice",""))
        self.nodes["auxiliary"] = wordNode("auxiliary", components.get("auxiliary","")) 
        
        self.subject   = self.nodes["subject"].value
        self.predicate = self.nodes["object"].value
        self.verb      = self.nodes["verb"].value
        self.tense     = self.nodes["tense"].value
        self.negative  = self.nodes["negative"].value
        self.voice     = self.nodes["voice"].value
        self.auxiliary = self.nodes["auxiliary"].value
        self.time_circumstance  = self.nodes["time"].value
        self.place_circumstance = self.nodes["place"].value

    def prepare(self,):
        """
        extract more data from components
        """
        #prepare the verb
        # extract tense
        tense = self.get_tense(self.nodes["time"].value)
        tense_aux  = tense
        tense_verb = tense
        pronoun = self.get_pronoun(self.nodes["subject"].value)
        self.verb_conjugated = ""
        if self.nodes["auxiliary"].value:
            tense_aux = tense
            tense_verb = vconst.TenseSubjunctiveFuture
            # if auxiliary the tense change
            vbc_aux = libqutrub.classverb.VerbClass(self.auxiliary, transitive=False,future_type=araby.FATHA) 
            verb_aux = vbc_aux.conjugate_tense_for_pronoun(tense_aux, pronoun)
            verb_factor = u"أن"
            self.verb_aux = verb_aux
            self.nodes["auxiliary"].tense = tense_aux
            self.nodes["auxiliary"].conjugated = verb_aux
            self.nodes["auxiliary"].after = verb_factor
            if tense_aux == vconst.TenseJussiveFuture:
                self.nodes["auxiliary"].before = u"لم"
            elif tense_aux == vconst.TenseSubjunctiveFuture:
                self.nodes["auxiliary"].before = u"لن"

        else:
            self.stream.remove("auxiliary")
            self.nodes["auxiliary"].set_null()    
            self.stream.remove("factor_auxiliary")
        # verb
        vbc = libqutrub.classverb.VerbClass(self.verb, transitive=True,future_type=araby.FATHA) 
        self.verb_conjugated = vbc.conjugate_tense_for_pronoun(tense_verb, pronoun)
        self.nodes["verb"].tense = tense_verb    
        self.nodes["verb"].conjugated = self.verb_conjugated
        if tense_verb == vconst.TenseJussiveFuture:
            self.nodes["verb"].before = u"لم"
        elif tense_verb in (vconst.TenseSubjunctiveFuture, vconst.TensePassiveSubjunctiveFuture) and not self.nodes["auxiliary"].value:
            self.nodes["verb"].before = u"لن"
        # if the subject is a pronoun, it will be omitted
        if self.is_pronoun(self.subject):
            self.stream.remove("subject")
            self.nodes["subject"].set_null()             
            
        # if the object is a pronoun
        if self.is_pronoun(self.predicate):
            v_enclitic = self.get_enclitic(self.predicate)
            #~ self.verb_conjugated += "-" + v_enclitic
            forms = self.verbaffixer.vocalize(self.verb_conjugated, proclitic="", enclitic=v_enclitic)
            self.verb_conjugated = forms[0][0]
            self.nodes["verb"].conjugated = self.verb_conjugated
            self.stream.remove("object")
            self.nodes["object"].set_null()             
    def get_enclitic(self, pronoun):
        """
        Extract enclitic
        """
        return yaziji_const.ENCLITICS.get(pronoun,"")
        
    def get_tense(self, time_word):
        """
        Extract tense from time circomstance
        """
        # get the primary tense
        tense = ""
        # if not time circum or is neutral
        if not time_word or yaziji_const.TENSES.get(time_word,""):
            if self.nodes["tense"].value:
                tense = self.nodes["tense"].value
        else:
            tense = yaziji_const.TENSES.get(time_word,"")
        # negative
        if self.nodes["negative"].value == u"منفي":
            # if past the verb will be future majzum
            if tense == vconst.TensePast:
                tense = vconst.TenseJussiveFuture
            elif tense == vconst.TenseFuture:
                tense = vconst.TenseSubjunctiveFuture
        #voice active
        if self.nodes["voice"].value == u"مبني للمجهول":
            if tense == vconst.TensePast:
                tense = vconst.TensePassivePast
            elif tense == vconst.TenseFuture:
                tense = vconst.TensePassiveFuture
            elif tense == vconst.TenseJussiveFuture:
                tense = vconst.TensePassiveJussiveFuture
            elif tense == vconst.TenseSubjunctiveFuture:
                tense = vconst.TensePassiveSubjunctiveFuture
        return tense       
        
    def get_pronoun(self, word):
        """
        get the pronoun of the word
        """
        if word in vconst.PronounsTable:
            return word
        else:
            return vconst.PronounHuwa
    
    def is_pronoun(self, word):
        """
        get if is pronoun
        """
        return word in vconst.PronounsTable

           
        
    def build(self,):
        """
        build a phrase
        """
        # build phrase according to stream
        phrase = []
        for key in self.stream.__list__():
            wn = self.nodes.get(key, None)
            if wn:
                if wn.before:
                    phrase.append(wn.before)
                phrase.append(wn.conjugated) 
                if wn.after:
                    phrase.append(wn.after)                
        phrase = u" ".join(phrase)
        return phrase
        

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
