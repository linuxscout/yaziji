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
import libqutrub.verb_db
import pyarabic.araby as araby
import alyahmor.verb_affixer
import alyahmor.noun_affixer
import arramooz.arabicdictionary

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
        self.transitive = True

    def set_null(self,):
        self.value = ""
        self.conjugated = ""
        
class PhrasePattern:
    """
    A class to generator
    """
    def __init__(self):
        
        self.stream = stream_pattern.streamPattern(["auxiliary",
        "subject", 
        "negation",
        "verb",
        "object",
        "time",
        "place",
        ])
        

        self.verbaffixer = alyahmor.verb_affixer.verb_affixer()
        self.nounaffixer = alyahmor.noun_affixer.noun_affixer()
        self.verb_dict = arramooz.arabicdictionary.ArabicDictionary('verbs')
        self.noun_dict = arramooz.arabicdictionary.ArabicDictionary('nouns')
        default_wn =  wordNode("default", "")  
        self.nodes = {"subject"  : default_wn,
        "object"   : default_wn,
        "verb"     : default_wn,
        "time"     : default_wn,
        "place"    : default_wn,
        "tense"    : default_wn,
        "negative" : default_wn,
        "voice"    : default_wn,
        "auxiliary" : default_wn,
        "phrase_type":default_wn,
        }

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
        phrase_type = components.get("phrase_type","")
        self.nodes["phrase_type"] = wordNode("phrase_type", components.get("phrase","")) 
        
        stream = yaziji_const.STREAMS.get(phrase_type, yaziji_const.STREAMS["default"] )
        print(phrase_type, stream) 
        self.stream = stream_pattern.streamPattern(stream)
        
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
        pronoun_aux = pronoun
        self.verb_conjugated = ""
        if self.nodes["auxiliary"].value and self.nodes["verb"].value:
            tense_aux = tense
            if self.nodes['voice'].value =="مبني للمجهول":
                pronoun_aux = vconst.PronounHuwa
            tense_verb = vconst.TenseSubjunctiveFuture
            # if auxiliary the tense change
            transitive, future_type = self.get_verb_attributes(self.auxiliary)            
            vbc_aux = libqutrub.classverb.VerbClass(self.auxiliary, transitive, future_type)
            if not self.is_compatible(tense_aux, pronoun_aux):
                verb_aux =  u"[ImperativeError '%s']"%pronoun_aux       
            else:
                verb_aux = vbc_aux.conjugate_tense_for_pronoun(tense_aux, pronoun_aux)
            verb_factor = u"أَنْ"
            self.verb_aux = verb_aux
            self.nodes["auxiliary"].tense = tense_aux
            self.nodes["auxiliary"].conjugated = verb_aux
            self.nodes["verb"].before = verb_factor
            if tense_aux in (vconst.TenseJussiveFuture, vconst.TensePassiveJussiveFuture):
                self.nodes["auxiliary"].before = u"لَمْ"
            elif tense_aux in (vconst.TenseSubjunctiveFuture, vconst.TensePassiveSubjunctiveFuture) :
                self.nodes["auxiliary"].before = u"لَنْ"

        else:
            self.nodes["auxiliary"].set_null()    
        # verb
        if self.verb:
            transitive, future_type = self.get_verb_attributes(self.verb)
            vbc = libqutrub.classverb.VerbClass(self.verb, transitive,future_type)
            if not self.is_compatible(tense_verb, pronoun):
                self.verb_conjugated = u"[ImperativeError '%s']"%pronoun            
            else:
                self.verb_conjugated = vbc.conjugate_tense_for_pronoun(tense_verb, pronoun)
                
            self.nodes["verb"].tense = tense_verb    
            self.nodes["verb"].transitive = transitive    
            self.nodes["verb"].conjugated = self.verb_conjugated
            if tense_verb in (vconst.TenseJussiveFuture, vconst.TensePassiveJussiveFuture):
                self.nodes["verb"].before = u"لَمْ"
            elif tense_verb in (vconst.TenseSubjunctiveFuture, vconst.TensePassiveSubjunctiveFuture) and not self.nodes["auxiliary"].value:
                self.nodes["verb"].before = u"لَنْ"
            # if the subject is a pronoun, it will be omitted
            if self.is_pronoun(self.subject):
                self.nodes["subject"].set_null()             
                
            # if the object is a pronoun
            if self.is_pronoun(self.predicate) and  self.nodes["verb"].transitive and self.nodes["voice"].value != u"مبني للمجهول" :
                v_enclitic = self.get_enclitic(self.predicate)
                #~ self.verb_conjugated += "-" + v_enclitic
                forms = self.verbaffixer.vocalize(self.verb_conjugated, proclitic="", enclitic=v_enclitic)
                self.verb_conjugated = forms[0][0]
                self.nodes["verb"].conjugated = self.verb_conjugated
        if self.place_circumstance :
            word = self.place_circumstance
            self.nodes["place"].before = u"فِي"
            self.nodes["place"].conjugated  = self.conjugate_noun(word, u"مجرور")       
        if self.predicate :
            # if is there is verb
            word = self.predicate
            if self.nodes['verb'].value:
                # إذا كان الضمير متصلا
                # أو الفعل لازما
                if self.is_pronoun(self.predicate) or not self.nodes['verb'].transitive:
                    self.nodes["object"].set_null()
                # إذا كان مبنيا للمجهول
                # ما لم يسم فاعله
                # او خبر
                elif self.nodes['voice'].value =="مبني للمجهول" and not self.nodes['auxiliary'].value:
                    self.nodes["object"].conjugated  = self.conjugate_noun(word, u"مرفوع")       

                else:

                    self.nodes["object"].conjugated  = self.conjugate_noun(word, u"منصوب")       
            else:
                # مبتدأ وخبر
                self.nodes["object"].conjugated  = self.conjugate_noun(word, u"مرفوع")       
                
        if self.subject :
            # if is there is verb
            word = self.subject
            if self.nodes['verb'].value:
                # إذا كان الضمير متصلا
                # أو الفعل مبني للمجهول
                if self.is_pronoun(self.subject) or self.nodes['voice'].value =="مبني للمجهول":
                    self.nodes["subject"].set_null()
   
            # مبتدأ وخبر
            self.nodes["subject"].conjugated  = self.conjugate_noun(word, u"مرفوع")       
                

    def conjugate_noun(self, word, tag):
        """
        conjugate a word according to tag
        """
        enclitic = u""        
        proclitic = u""       
        suffix = ""
        if tag == u"منصوب":
            suffix = araby.FATHA
        elif tag == u"مجرور":
            suffix = araby.KASRA
        elif tag == u"مرفوع":
            suffix = araby.DAMMA
        else:
            suffix = araby.FATHA
            
        if not self.is_pronoun(word):
            proclitic = u"ال"

        if word in yaziji_const.SPECIAL_VOCALIZED:
            voc = yaziji_const.SPECIAL_VOCALIZED[word]
            conj = voc
        else:
            # get vocalized form of the word
            noun_tuple = self.get_noun_attributes(word)
            voc = noun_tuple.get("vocalized","")
            forms = self.nounaffixer.vocalize(voc, proclitic, suffix, enclitic)
            if forms:
                conj = forms[0][0] 
            else:
                conj = word
        return conj
        
            
    def is_compatible(self, tense, pronoun):
        
        if tense == vconst.TenseImperative and pronoun not in vconst.ImperativePronouns:
            return False
        return True
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
        if not time_word or not yaziji_const.TENSES.get(time_word,""):
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
    def get_verb_attributes(self, word):
        """
        return transitive and future_type
        """
        transitive = True
        future_type = araby.FATHA
        

        word_nm = araby.strip_tashkeel(word)
        foundlist = self.verb_dict.lookup(word_nm)
        for word_tuple in foundlist:
            word_tuple = dict(word_tuple)
            # if found the same vocalization
            if word == word_tuple['vocalized']:
                transitive = word_tuple['transitive']
                future_type = word_tuple['future_type']
                print("1-Transitive", transitive)
                print("1-future_type", future_type)                
                break;
        else: # no vocalization, try the first one
            word_tuple = dict(foundlist[0])
            # if found
            transitive = word_tuple['transitive']
            future_type = word_tuple['future_type']
            print("Transitive", transitive)
            print("future_type", future_type)
            #~ print("vocalized", vocalized)
        #~ print("verb************", word)
        return transitive, future_type

    def get_noun_attributes(self, word):
        """
        return vocalized form
        """
        vocalized = word
       
        word_nm = araby.strip_tashkeel(word)
        foundlist = self.noun_dict.lookup(word_nm)
        word_tuple_res = None
        for word_tuple in foundlist:
            word_tuple = dict(word_tuple)
            # if found the same vocalization
            word_tuple_res = word_tuple
            break
        else: # no vocalization, try the first one
            if foundlist:
                word_tuple_res = dict(foundlist[0])
            else:
                word_tuple_res = {"vocalized":word}
        return word_tuple_res        
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
            if wn and wn.value:
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
