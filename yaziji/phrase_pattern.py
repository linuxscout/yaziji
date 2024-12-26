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

import logging
from typing import Dict, Union

import libqutrub.verb_const as vconst
import libqutrub.classverb
import libqutrub.verb_db
import pyarabic.araby as araby
import alyahmor.verb_affixer
import alyahmor.noun_affixer
import arramooz.arabicdictionary
from arramooz.nountuple import NounTuple
from arramooz.verbtuple import VerbTuple

import yaziji_const
from yaziji_const import MARFOU3, MANSOUB, MAJROUR, DEFINED, PASSIVE_VOICE, VERBAL_PHRASE
from yaziji_const import HIDDEN
import yz_utils
import stream_pattern
from wordnode import wordNode
from components_set import componentsSet
class PhrasePattern:
    """
    A class to generator
    """
    def __init__(self, error_observer=None):
        # init error_observer
        self.error_observer = error_observer
        # Init objects
        self.stream = stream_pattern.streamPattern("default")
        
        # a verb affixer to conjugate and affixe a verb
        self.verbaffixer = alyahmor.verb_affixer.verb_affixer()
        # a noun affixer to flex a noun
        self.nounaffixer = alyahmor.noun_affixer.noun_affixer()
        # dictionanries used to get lemmas and words
        self.verb_dict = arramooz.arabicdictionary.ArabicDictionary('verbs')
        self.noun_dict = arramooz.arabicdictionary.ArabicDictionary('nouns')

        self.components_config = componentsSet()


        self.phrase_type = ""
        # init defaul word nodes
        self.nodes = {}
        # init default features
        self.phrase_features ={
            'phrase_type':"",
            "tense":"",
            'negative':"",
            "voice":"",
            "tense_verb":"",
            "tense_aux":"",
            "pronoun_verb":"",
            "pronoun_aux":"",
            "factor_verb":"",
            "factor_aux":"",
        }
        #TODO: change the list to dynamic list

        self.nodes_names = ["phrase_type","subject", "object", "verb", "time", "place", "tense", "negative", "voice",  "auxiliary"]

        self.nodes_names_nouns = self.components_config.get_names_by_wordtype("noun")

        # init nodes
        # prepare only nodes with word type
        for name  in self.nodes_names:
            self.nodes[name] = wordNode("default", "")
        # prepare features nodes

    def add_components(self, components):
        """
        Add components

        """
        # collect informations from nodes names from given components
        for name in self.nodes_names:
            # check if a required name is not found
            if self.is_required(name) and components.get(name, "") == "":
                response = -2
                # self.notify_error(response,f"ERROR: A required name '{name}' not found. ",)
                self.notify_error_id(response,"REQUIRED_NAME", {"name":name})
                return response
            if self.components_config.get_type(name) == "word":

                self.nodes[name]  = wordNode(name, components.get(name,""))
            elif self.components_config.get_type(name) == "feature":
                # save features in features table
                self.phrase_features[name] = components.get(name, "")
            else:
                self.nodes[name] = wordNode(name, components.get(name, ""))
        # check for extra components not supported
        for key in components:
            if key not in self.nodes_names and not key in self.phrase_features:
                response = -3
                # self.notify_error(response,f"ERROR: Unsupported component key '{key}'.")
                self.notify_error_id(response,"UNSUPPORTED_COMPONENT", {"name":key})
                return response
        # select a stream for a given phrase type
        # the stream is the word order and phrase components
        # for example, in Nominal Phrase, the order cacomponentsn be
        # [        "subject",
        #     "auxiliary",
        #         "negation",
        #         "verb",
        #         "object",
        #         "place",
        #         "time",
        #         ],
        # if self.get_feature_value("phrase_type",VERBAL_PHRASE) :
        if self.get_feature_value("phrase_type","") :
            # phrase_type is given in inputs
            # store it in phrase_type
            # this determine the way to order phrase words
            self.phrase_type = self.get_feature_value("phrase_type")
        else:
            response = -4
            # self.notify_error(response,f"ERROR: Required Phrase type is empty'.")
            self.notify_error_id(response, "EMPTY_PHRASE_TYPE")
            return response
        # get the phrase word order (stream) according to phrase type
        self.stream = stream_pattern.streamPattern(self.phrase_type)

        #TODO: this should return a dynamic list to allow adding new phrase parts
        #TODO: return all attributes
        #TODO: why extract all this, when we can use nodes as dict
        # words
        self.subject   = self.get_node_value("subject")
        self.predicate = self.get_node_value("object")
        self.verb      = self.get_node_value("verb")
        self.auxiliary = self.get_node_value("auxiliary")
        self.time_circumstance = self.get_node_value("time")
        self.place_circumstance = self.get_node_value("place")

        #featues
        self.tense     = self.get_feature_value("tense")
        self.negative  = self.get_feature_value("negative")
        self.voice     = self.get_feature_value("voice")
        self.phrase_features["has_verb"]       = bool(self.get_node_value("verb"))
        self.phrase_features["has_auxiliary"]  = bool(self.get_node_value("auxiliary"))
        self.phrase_features["transitive"]  = True



        #check for errors
        response = self.check_compatibles()
        if response < 0:
            # self.notify_error(response,f"ERROR: Incompatible Subject {self.subject} and tense '{self.tense}'.")
            self.notify_error_id(response, "INCOMPATIBLE_SUBJECT_TENSE", {"subject":self.subject,"tense":self.tense})
            return response
        return True

    def is_required(self,name):
        """
        check if name is required
        :param name:
        :return:
        """
        return self.components_config.is_required(name)

    def get_feature_value(self, feature, default=""):
        """
        get feature value
        :param feature:
        :return:
        """
        # return self.get_node_value(feature)
        return self.phrase_features.get(feature, default)

    def get_node_value(self, name, default=""):
        """
        get feature value
        :param feature:
        :return:
        """
        if self.nodes.get(name, None):
            return self.nodes.get(name, None).value
        return default

    def get_node(self, name):
        """
        get feature value
        :param feature:
        :return:
        """
        return  self.nodes.get(name, None)

    def check_compatibles(self):
        """
        Check if input components are compatibles
        :return:
        """
        # مشكلة في التصريف بين الضمير وفعل الأمر
        if  (self.get_feature_value("tense") == vconst.TenseImperative
                and  self.get_node_value("subject")  not in vconst.ImperativePronouns):
            return -1 # error code
        #TODO:
        # check verbs
        return True

    def prepare(self):
        """
        Extract and prepare data from components.
        """
        # Prepare noun-type nodes
        for key in self.nodes_names_nouns:
            value = self.get_node_value(key)
            if value:
                attributes = self.get_noun_attributes(value)
                self.nodes[key].update(attributes)

        # Extract tense features
        time_value = self.get_node_value("time")
        tense_verb, tense_aux, factor_verb, factor_aux = self.get_tense(time_value)
        self.phrase_features.update({
            "tense_verb": tense_verb,
            "tense_aux": tense_aux,
            "factor_verb": factor_verb,
            "factor_aux": factor_aux,
        })

        # Extract pronouns
        subject_node = self.get_node("subject")
        pronoun_verb, pronoun_aux = self.get_pronoun(subject_node, tense_verb, tense_aux)
        self.phrase_features.update({
            "pronoun_verb": pronoun_verb,
            "pronoun_aux": pronoun_aux,
        })

        # Handle missing pronoun errors
        if not pronoun_verb:
            self.nodes["verb"].conjugated = "[ImperativeError Pronoun]"
            return False

        # Prepare auxiliary verb
        if self.get_feature_value("has_auxiliary") and self.get_feature_value("has_verb"):
            self.prepare_verb(self.nodes["auxiliary"], "auxiliary")
        else:
            self.nodes["auxiliary"].hide()

        # Prepare main verb
        if self.get_feature_value("has_verb"):
            self.prepare_verb(self.nodes["verb"], vtype="")
            self.phrase_features["transitive"] = self.nodes["verb"].transitive

            # Handle pronoun objects for transitive active verbs
            if (
                    self.is_pronoun(self.predicate)
                    and self.nodes["verb"].transitive
                    and self.get_feature_value("voice") != PASSIVE_VOICE
            ):
                v_enclitic = self.get_enclitic(self.predicate)
                self.nodes["verb"].encilitc = v_enclitic
                self.nodes["verb"].proclitic = ""
                verb_conjugated = self.nodes["verb"].conjugated
                forms = self.verbaffixer.vocalize(verb_conjugated, proclitic="", enclitic=v_enclitic)
                self.nodes["verb"].conjugated = forms[0][0]

        # Prepare object (predicate)
        if self.predicate:
            self.prepare_predicate(self.nodes["object"])

        # Prepare subject
        if self.subject:
            tags = [MARFOU3, DEFINED]
            if self.get_feature_value("has_verb") and self.phrase_type == VERBAL_PHRASE:
                if self.is_pronoun(self.subject) or self.get_feature_value("voice") == PASSIVE_VOICE:
                    tags = [HIDDEN]  # Hide the subject
            self.nodes["subject"].conjugated = self.conjugate_noun_by_tags(self.nodes["subject"], tags=tags)

        # Prepare place circumstance
        if self.place_circumstance:
            self.nodes["place"].before = u"فِي"
            self.nodes["place"].conjugated = self.conjugate_noun_by_tags(
                self.nodes["place"], tags=[MAJROUR, DEFINED]
            )

        return True

    # def prepare(self,):
    #     """
    #     extract more data from components
    #     """
    #     # prepare the noun type nodes
    #     for key in self.nodes_names_nouns:
    #         value = self.get_node_value(key)
    #         if value:
    #             # prepare some attributes
    #             attributes = self.get_noun_attributes(value)
    #             # set some attributes from dictionary
    #             self.nodes[key].update(attributes)
    #
    #     # extract tense
    #     tense_verb, tense_aux, factor_verb, factor_aux = self.get_tense(self.get_node_value("time"))
    #     self.phrase_features["tense_verb"] = tense_verb
    #     self.phrase_features["tense_aux"] = tense_aux
    #     self.phrase_features["factor_verb"] = factor_verb
    #     self.phrase_features["factor_aux"] = factor_aux
    #
    #     # extract pronouns
    #     pronoun_verb, pronoun_aux = self.get_pronoun(self.get_node("subject"), tense_verb, tense_aux)
    #     self.phrase_features["pronoun_verb"] = pronoun_verb
    #     self.phrase_features["pronoun_aux"] = pronoun_aux
    #     # Error on pronoun and
    #     if not pronoun_verb:
    #         self.nodes["verb"].conjugated = "[ImperativeError Pronoun]"
    #         return False
    #     if self.get_feature_value("has_auxiliary") and self.get_feature_value("has_verb"):
    #         self.prepare_verb(self.nodes["auxiliary"],"auxiliary")
    #     else:
    #         self.nodes["auxiliary"].hide()
    #     # verb
    #     if self.get_feature_value("has_verb"):
    #         self.prepare_verb(self.nodes["verb"],vtype="")
    #         self.phrase_features["transitive"] = self.nodes["verb"].transitive
    #
    #
    #
    #         # if the object is a pronoun
    #         if self.is_pronoun(self.predicate) and  self.nodes["verb"].transitive and self.get_feature_value("voice") != PASSIVE_VOICE :
    #             v_enclitic = self.get_enclitic(self.predicate)
    #             # save enclitic to be used later
    #             self.nodes["verb"].encilitc = self.get_enclitic(self.predicate)
    #             self.nodes["verb"].proclitic = ""
    #             verb_conjugated =  self.nodes["verb"].conjugated
    #             forms = self.verbaffixer.vocalize(verb_conjugated, proclitic="", enclitic=v_enclitic)
    #             # seletc first one of generated forms
    #             verb_conjugated = forms[0][0]
    #             self.nodes["verb"].conjugated = verb_conjugated
    #
    #     if self.predicate :
    #         self.prepare_predicate(self.nodes["object"])
    #
    #     if self.subject :
    #         # if is there is verb
    #         word = self.subject
    #         tags = [MARFOU3, DEFINED]
    #         if self.get_feature_value("has_verb"):
    #             # إذا كان الضمير متصلا
    #             # أو الفعل مبني للمجهول
    #             if (self.phrase_type == VERBAL_PHRASE
    #                 and ( self.is_pronoun(self.subject) or self.get_feature_value("voice") == PASSIVE_VOICE)
    #                ):
    #                 # hide the subject from stream
    #                 tags = [HIDDEN, ]
    #                 # self.nodes["subject"].hide()
    #
    #         # مبتدأ وخبر
    #         self.nodes["subject"].conjugated  = self.conjugate_noun_by_tags(self.nodes["subject"], tags=tags)
    #
    #     if self.place_circumstance :
    #         word = self.place_circumstance
    #         self.nodes["place"].before = u"فِي"
    #         self.nodes["place"].conjugated  = self.conjugate_noun_by_tags(self.nodes["place"], tags=[MAJROUR, DEFINED])
    #     # return True

    def prepare_predicate(self, word_node):
        """
        :return:
        """
        # if is there a verb
        word = self.predicate
        if self.get_feature_value("has_verb"):
            # إذا كان الضمير متصلا
            # أو الفعل لازما
            if self.is_pronoun(self.predicate) or not self.get_feature_value("transitive"):
                # word_node.set_null()
                word_node.hide()
                tags = [HIDDEN]
            # إذا كان مبنيا للمجهول
            # ما لم يسم فاعله
            # او خبر
            elif self.get_feature_value("voice") == PASSIVE_VOICE and not self.get_feature_value("has_auxiliary"):
                # word_node.conjugated  = self.conjugate_noun(word, u"مرفوع")
                # word_node.conjugated = self.conjugate_noun_by_tags(word_node,
                #                                                               tags=[MARFOU3, DEFINED])
                tags = [MARFOU3, DEFINED]
            else:

                # word_node.conjugated  = self.conjugate_noun(word, u"منصوب")
                # word_node.conjugated = self.conjugate_noun_by_tags(word_node,
                #                                                               tags=[MANSOUB, DEFINED])
                tags=[MANSOUB, DEFINED]
        else:
            # مبتدأ وخبر
            # word_node.conjugated  = self.conjugate_noun_by_tags(word_node, tags=[MARFOU3, DEFINED])
            tags = [MARFOU3, DEFINED]
        word_node.tags = tags
        word_node.conjugated  = self.conjugate_noun_by_tags(word_node, tags)

    def prepare_verb(self, wordnode , vtype=""):
        """
        prepare verb to be conjugated
        :param wordnode: 
        :param vtype:
        :return: 
        """

        future_type = wordnode.future_type
        transitive = wordnode.transitive
        ver_tuple = self.get_verb_attributes(wordnode.value, future_type=future_type, transitive=transitive,
                                             auxiliary= bool(vtype == "auxiliary"))
        transitive  = ver_tuple.is_transitive()
        future_type = ver_tuple.get_future_type()
        vocalized   = ver_tuple.get_vocalized()

        # add suffix to get auxiliary features
        suffix = "_aux" if vtype == "auxiliary" else "_verb"
        tense = self.get_feature_value("tense"+suffix)
        pronoun = self.get_feature_value("pronoun"+suffix)
        factor = self.get_feature_value("factor"+suffix)
        #conjugation
        # to move
        vbc = libqutrub.classverb.VerbClass(vocalized, transitive, future_type)
        conj = vbc.conjugate_tense_for_pronoun(tense,pronoun)
        # print(f"vbc {conj}, {suffix}, {vocalized}, '{pronoun}', {tense} feature aux {self.get_feature_value('tense_aux')}")
        # save attributes
        wordnode.tense = tense
        wordnode.conjugated = conj
        wordnode.before = factor
        wordnode.transitive = transitive
        wordnode.future_type = future_type
        wordnode.pronoun = pronoun

    def conjugate_noun_by_tags(self, word_node, tags):
        """
        Conjugate a noun according to the given tags.
        """
        if HIDDEN in word_node.tags or HIDDEN in tags:
            word_node.hide()
            return ""
        # Handle special cases for words like pronouns
        vocalized = yaziji_const.SPECIAL_VOCALIZED.get(word_node.word, "")
        if vocalized:
            return vocalized

        # Initialize affix components
        proclitic = ""
        enclitic = ""
        suffix = ""

        # Build proclitic for defined nouns
        if "تعريف" in tags and not word_node.is_defined():
            proclitic = u"ال"

        # Determine suffix based on tags
        suffix_mapping = {
            MANSOUB: araby.FATHA,
            MAJROUR: araby.KASRA,
            MARFOU3: araby.DAMMA,
        }
        suffix = next((suffix_mapping[tag] for tag in tags if tag in suffix_mapping), araby.FATHA)

        # Apply affixation and retrieve forms
        word = word_node.value
        forms = self.nounaffixer.vocalize(word_node.vocalized, proclitic, suffix, enclitic)

        # Return the conjugated form or the original word
        return forms[0][0] if forms else word

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
        Extract tense from time circumstance.
        """
        # Determine primary tense based on the time word
        given_tense =  self.get_feature_value("tense")
        # if time word give tense, use it, else use given tense
        tense = yaziji_const.TENSES.get(time_word, given_tense if given_tense else "")
        verb_factor = ""

        # Handle negative tense cases
        if self.get_feature_value("negative") == u"منفي":
            if tense == vconst.TensePast:
                tense, verb_factor = vconst.TenseJussiveFuture, u"لَمْ"
            elif tense == vconst.TenseFuture:
                tense, verb_factor = vconst.TenseSubjunctiveFuture, u"لَنْ"

        # Handle passive voice
        if self.get_feature_value("voice") == PASSIVE_VOICE:
            passive_mapping = {
                vconst.TensePast: vconst.TensePassivePast,
                vconst.TenseFuture: vconst.TensePassiveFuture,
                vconst.TenseJussiveFuture: vconst.TensePassiveJussiveFuture,
                vconst.TenseSubjunctiveFuture: vconst.TensePassiveSubjunctiveFuture,
            }
            tense = passive_mapping.get(tense, tense)

        # Prepare auxiliary and verb tenses
        tense_aux = tense
        tense_verb = tense
        factor_aux = verb_factor
        factor_verb = verb_factor

        # Handle auxiliary and main verb adjustments
        # الفعل المساعد يأخذ التصريف والفعل الأصلي يصبح مضارعا منصوبا
        if self.verb and self.auxiliary:
            # Adjust the main verb for subjunctive future tense
            if self.get_feature_value("voice") == PASSIVE_VOICE:
                tense_verb = vconst.TensePassiveSubjunctiveFuture
            else:
                tense_verb = vconst.TenseSubjunctiveFuture
            factor_verb = u"أَنْ"

        return tense_verb, tense_aux, factor_verb, factor_aux



    def get_verb_attributes(self, word, auxiliary = False, future_type="NA", transitive="NA"):
        """
        return transitive and future_type
        """

        
        if auxiliary:
            word_tuple_result = VerbTuple({"vocalized":word,
                                 "unvocalized":araby.strip_harakat(word),
                                 "transitive": True,
                                 "future_type": yaziji_const.AUXILIARY.get(word, araby.FATHA)
                                 })
        else:
            word_nm = araby.strip_tashkeel(word)
            foundlist = self.verb_dict.lookup(word_nm)
            # Convert foundlist to a list of dictionaries
            foundlist = [VerbTuple(x) for x in foundlist]

            # Find the first matching vocalized form
            word_tuple_result_list = [
                item for item in foundlist if araby.vocalizedlike(word, item.get_vocalized())
            ]
            # filter by future_type
            if future_type != "NA":
                word_tuple_result_list = [
                    item for item in word_tuple_result_list
                    if yz_utils.equal_future_type(future_type, item.get_future_type())
                ]
            # filter by transitive
            if transitive != "NA":
                word_tuple_result_list = [
                    item for item in word_tuple_result_list if transitive == item.is_transitive()
                ]

            word_tuple_result = None
            if word_tuple_result_list:
                word_tuple_result = word_tuple_result_list[0]
            else:
                # No matching vocalization found, use the first result if available
                if foundlist:
                    word_tuple_result = foundlist[0]
                else:
                    word_tuple_result = VerbTuple({"vocalized": word,
                                                   "unvocalized": araby.strip_harakat(word),
                                                   "transitive": True,
                                                   "future_type": araby.FATHA,
                                                   })

        return word_tuple_result

    def get_noun_attributes(self, word: str) -> Dict[str, Union[str, None]]:
        """
        Returns the vocalized form and other attributes of the given noun.
        """
        # Strip diacritics (tashkeel) from the word
        word_nm = araby.strip_tashkeel(word)
        vocalized_input = word
        foundlist = self.noun_dict.lookup(word_nm)


        # Convert foundlist to a list of dictionaries
        foundlist = [NounTuple(x) for x in foundlist]

        # Find the first matching vocalized form
        word_tuple_result_list = [
            item for item in foundlist if araby.vocalizedlike(word, item.get_vocalized())
        ]
        word_tuple_result = None
        if word_tuple_result_list:
            word_tuple_result = word_tuple_result_list[0]
        else:
            # No matching vocalization found, use the first result if available
            if foundlist:
                word_tuple_result = foundlist[0]
            else:
                word_tuple_result = NounTuple({"vocalized": word})
        # logging.info(f"WORD: {word_tuple_result}, Found List: {foundlist}")
        return word_tuple_result


    def get_pronoun(self, word_node, tense_verb, tense_aux):
        """
        get the pronoun of the word
        """
        pronoun = ""
        pronoun_aux = ""
        # if not isinstance(word_node, wordNode):
        #     print("not instance", type(word_node))
        #     return  False, False
        word = word_node.value
        feminin = word_node.feminin
        number = word_node.number
        if word in vconst.PronounsTable:
            pronoun = word
        else:
            pronoun = yz_utils.get_pronoun("غائب",feminin, number)

        #
        pronoun_aux = pronoun
        if tense_aux in vconst.TablePassiveTense:
            if feminin:
                pronoun_aux = vconst.PronounHya
            else:
                pronoun_aux = vconst.PronounHuwa
        # test if the pronoun is compatible with tense
        # print(f" verb '{tense_verb}'-'{pronoun}', auxilairy '{tense_aux}'-'{pronoun_aux}',")
        if not self.is_compatible(tense_verb, pronoun) and not self.is_compatible(tense_aux, pronoun_aux):
        # if (tense_verb == vconst.TenseImperative or tense_aux == vconst.TenseImperative)  and pronoun not in vconst.ImperativePronouns:
            return False, False
        return pronoun, pronoun_aux
    
    def is_pronoun(self, word):
        """
        get if is pronoun
        """
        return word in vconst.PronounsTable

    def build(self) -> str:
        """
        Build a phrase based on the stream of word roles and their conjugated forms.
        """
        # Initialize an empty list to construct the phrase
        phrase_parts = []

        # Iterate through the word role order in the stream
        for key in self.stream.to_list():
            # Retrieve the corresponding word node
            word_node = self.nodes.get(key)
            #  some words can be hidden like a pronoun for a verb
            #   # أنت تلعب ==> تلعب
            # Skip if the word node is hidden or has no value
            if word_node and word_node.value and not word_node.hidden:
                # some words generate particles  to be added before and after
                # for example a majzoum future tense need "لم" particalrd
                if word_node.before:
                    phrase_parts.append(word_node.before)

                # Add the conjugated word itself
                phrase_parts.append(word_node.conjugated)

                # Add any particles or suffixes after the word
                if word_node.after:
                    phrase_parts.append(word_node.after)

        # Join the phrase parts with spaces and return the resulting phrase
        return " ".join(phrase_parts)

    def notify_error(self, errorno, message, level="error"):
        """
        Notify error
        :param errorno:
        :param message:
        :return:
        """
        if self.error_observer:
            self.error_observer.notify_error(errorno, message)
            return True
        else:
            logging.info(f"ERROR #{errorno}: {message}")
        return True

    def notify_error_id(self, errorno, message_id, args={}):
        # get error message from observer
        if self.error_observer:
            error_message = self.error_observer.error_message(message_id)
            formatted_message = f"{error_message}".format_map(args)
        else:
            formatted_message = message_id + str(args)
        return self.notify_error(errorno, formatted_message)

    def log(selfself, location, message):
        logging.info(f"PHRASE_Pattern DEBUG: #{location}: {message}")

    # def build(self,):
    #     """
    #     build a phrase
    #     """
    #     # build phrase according to stream
    #     phrase = []
    #     # a strean contains the word role order in the phrase
    #     for key in self.stream.__list__():
    #         # each word node has conjugated form
    #         wn = self.nodes.get(key, None)
    #         # some words can be hidden like a pronoun for a verb
    #         # أنت تلعب ==> تلعب
    #         if wn and wn.value and not wn.hidden:
    #             # some words generate particles  to be added before and after
    #             # for example a majzoum future tense need "لم" partical
    #             if wn.before:
    #                 phrase.append(wn.before)
    #
    #             phrase.append(wn.conjugated)
    #             if wn.after:
    #                 phrase.append(wn.after)
    #     phrase = u" ".join(phrase)
    #     return phrase
    #

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
