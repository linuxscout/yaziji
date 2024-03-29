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
from wordnode import wordNode

class PhrasePattern:
    """
    A class to generator
    """
    def __init__(self):
        
        self.stream = stream_pattern.streamPattern("default")
        
        # a verb affixer to conjugate and affixe a verb
        self.verbaffixer = alyahmor.verb_affixer.verb_affixer()
        # a noun affixer to flex a noun
        self.nounaffixer = alyahmor.noun_affixer.noun_affixer()
        # dictionanries used to get lemmas and words
        self.verb_dict = arramooz.arabicdictionary.ArabicDictionary('verbs')
        self.noun_dict = arramooz.arabicdictionary.ArabicDictionary('nouns')

        self.phrase_type = ""
        # init defaul word nodes
        self.nodes = {}
        self.nodes_names = ['subject', 'object', 'verb', 'time', 'place', 'tense', 'negative', 'voice', 'auxiliary', 'phrase_type']
        for attr in self.nodes_names:
            self.nodes[attr] = wordNode("default", "")

    def add_components(self, components):
        """
        Add components

        """
        # collect informations from nodes names from given components
        for name in self.nodes_names:
            self.nodes[name]  = wordNode(name, components.get(name,""))
        # select a stream for a given phrase type
        # the stream is the word order and phrase components
        # for example, in Nominal Phrase, the order can be
        # [        "subject",
        #     "auxiliary",
        #         "negation",
        #         "verb",
        #         "object",
        #         "place",
        #         "time",
        #         ],
        if self.nodes.get("phrase_type", None) :
            self.phrase_type = self.nodes.get("phrase_type").value
        # get the phrase word order (stream) according to phrase type
        self.stream = stream_pattern.streamPattern(self.phrase_type)

        self.subject   = self.nodes["subject"].value
        self.predicate = self.nodes["object"].value
        self.verb      = self.nodes["verb"].value
        self.tense     = self.nodes["tense"].value
        self.negative  = self.nodes["negative"].value
        self.voice     = self.nodes["voice"].value
        self.auxiliary = self.nodes["auxiliary"].value
        self.time_circumstance  = self.nodes["time"].value
        self.place_circumstance = self.nodes["place"].value
        
        #check for errors
        response = self.check_compatibles()
        if response < 0:
            return response

        return True
    def check_compatibles(self):
        """
        Check if input components are compatibles
        :return:
        """
        # مشكلة في التصريف بين الضمير وفعل الأمر
        if  self.nodes["tense"].value == vconst.TenseImperative and self.nodes["subject"].value  not in vconst.ImperativePronouns:
            return -1 # error code
        #TODO:
        # check verbs
        return True

    def prepare(self,):
        """
        extract more data from components
        """
        # prepare the verb
        # extract tense
        tense_verb, tense_aux, factor_verb, factor_aux = self.get_tense(self.nodes["time"].value)
        # extract pronoun
        pronoun_verb, pronoun_aux = self.get_pronoun(self.nodes["subject"].value, tense_verb, tense_aux)
        
        # Error on pronoun and 
        if not pronoun_verb:
            self.nodes["verb"].conjugated = "[ImperativeError Pronoun]"
            return False
        if self.nodes["auxiliary"].value and self.nodes["verb"].value:
            transitive, future_type = self.get_verb_attributes(self.auxiliary, "auxiliary")            
            vbc_aux = libqutrub.classverb.VerbClass(self.auxiliary, transitive, future_type)
            verb_aux = vbc_aux.conjugate_tense_for_pronoun(tense_aux, pronoun_aux)
            self.nodes["auxiliary"].tense = tense_aux
            self.nodes["auxiliary"].conjugated = verb_aux
            self.nodes["auxiliary"].before = factor_aux
        else:
            self.nodes["auxiliary"].hide()
        # verb
        if self.verb:
            transitive, future_type = self.get_verb_attributes(self.verb)
            vbc = libqutrub.classverb.VerbClass(self.verb, transitive,future_type)
            verb_conjugated = vbc.conjugate_tense_for_pronoun(tense_verb, pronoun_verb)
                
            self.nodes["verb"].tense = tense_verb    
            self.nodes["verb"].transitive = transitive    
            self.nodes["verb"].conjugated = verb_conjugated
            self.nodes["verb"].before = factor_verb
             
                
            # if the object is a pronoun
            if self.is_pronoun(self.predicate) and  self.nodes["verb"].transitive and self.nodes["voice"].value != u"مبني للمجهول" :
                v_enclitic = self.get_enclitic(self.predicate)
                #~ self.verb_conjugated += "-" + v_enclitic
                forms = self.verbaffixer.vocalize(verb_conjugated, proclitic="", enclitic=v_enclitic)
                verb_conjugated = forms[0][0]
                self.nodes["verb"].conjugated = verb_conjugated

        if self.predicate :
            # if is there a verb
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
                if (self.phrase_type == "جملة فعلية"
                    and ( self.is_pronoun(self.subject) or self.nodes['voice'].value == "مبني للمجهول")
                   ):
                    # hide the subject from stream
                    self.nodes['subject'].hide()
   
            # مبتدأ وخبر
            self.nodes["subject"].conjugated  = self.conjugate_noun(word, u"مرفوع")       

        if self.place_circumstance :
            word = self.place_circumstance
            self.nodes["place"].before = u"فِي"
            self.nodes["place"].conjugated  = self.conjugate_noun(word, u"مجرور")       
                

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
        verb_factor = u""
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
                verb_factor = u"لَمْ"
            elif tense == vconst.TenseFuture:
                tense = vconst.TenseSubjunctiveFuture
                verb_factor = u"لَنْ"                
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
        tense_aux = tense
        tense_verb = tense
        factor_aux = verb_factor
        factor_verb = verb_factor
        
        # verb and auxiliary
        if self.verb and self.auxiliary:
            # auxilary and verb
            #الفعل المساعد يأخذ التصريف والفعل الأصلي يصبح مضارعا منصوبا
            if self.nodes["voice"].value == u"مبني للمجهول":
                tense_verb = vconst.TensePassiveSubjunctiveFuture
            elif self.nodes["voice"].value:
                tense_verb = vconst.TenseSubjunctiveFuture
            
            factor_verb = u"أَنْ"
            
        return tense_verb, tense_aux, factor_verb, factor_aux

    def get_verb_attributes(self, word, auxiliary = False):
        """
        return transitive and future_type
        """
        transitive = True
        future_type = araby.FATHA
        
        if auxiliary:
            transitive = True
            future_type = yaziji_const.AUXILIARY.get(word, araby.FATHA)
            return transitive, future_type

        word_nm = araby.strip_tashkeel(word)
        foundlist = self.verb_dict.lookup(word_nm)
        for word_tuple in foundlist:
            word_tuple = dict(word_tuple)
            # if found the same vocalization
            if word == word_tuple['vocalized']:
                transitive = word_tuple['transitive']
                future_type = word_tuple['future_type']
                #~ print("1-Transitive", transitive)
                #~ print("1-future_type", future_type)                
                break;
        else: # no vocalization, try the first one
            word_tuple = dict(foundlist[0])
            # if found
            transitive = word_tuple['transitive']
            future_type = word_tuple['future_type']
            #~ print("Transitive", transitive)
            #~ print("future_type", future_type)
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
    def get_pronoun(self, word, tense_verb, tense_aux):
        """
        get the pronoun of the word
        """
        pronoun = ""
        pronoun_aux = ""
        if word in vconst.PronounsTable:
            pronoun = word
        else:
            pronoun = vconst.PronounHuwa
        pronoun_aux = pronoun
        if tense_aux in vconst.TablePassiveTense:
            pronoun_aux = vconst.PronounHuwa
        # test if the pronoun is compatible with tense
        if (tense_verb == vconst.TenseImperative or tense_aux == vconst.TenseImperative)  and pronoun not in vconst.ImperativePronouns:
            return False, False
        return pronoun, pronoun_aux
    
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
        # a strean contains the word role order in the phrase
        for key in self.stream.__list__():
            # each word node has conjugated form
            wn = self.nodes.get(key, None)
            # some words can be hidden like a pronoun for a verb
            # أنت تلعب ==> تلعب
            if wn and wn.value and not wn.hidden:
                # some words generate particles  to be added before and after
                # for example a majzoum future tense need "لم" partical
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
