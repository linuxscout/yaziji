import logging
from typing import Dict, List, Optional

from libqutrub.verb_const import TenseImperative,  TensePast, TensePassivePast, TenseFuture
from libqutrub.verb_const import  ImperativePronouns, PronounsTable


# Local libraries

from yaziji_const import VERBAL_PHRASE, NOMINAL_PHRASE
from yaziji_const import ACTIVE_VOICE, PASSIVE_VOICE, AFFIRMATIVE, NEGATIVE

from components_set import componentsSet
from wordnode import wordNode
from stream_pattern import streamPattern
from mysam import tagcoder, tagmaker, taginflector


from error_listener import ErrorListener, INFO_CONST, WARNING_CONST, ERROR_CONST
# from yaziji.phrase_generator import PhraseGenerator
class Inflector:

    def __init__(self, ):
        """
        Initialize the Validator class with a rules base.
        """
        self.tagcoder = tagcoder.tagCoder()
        self.tagmaker = tagmaker.tagMaker()
        self.taginflecter = taginflector.tagInflector()
        pass

    def inflect_static(self ,word):
        """
        Inflect a list of predifined words, like FI, MIN
        :param word:
        :return:
        """
        return ""

    def inflect_word(self, word_node :wordNode):
        """
        Inflect a list of predifined words, like FI, MIN
        :param word:
        :return:
        """
        taglist = word_node.tags
        tgcode = self.tagcoder.encode(word_node.tags)
        print("tags list:", u";".join(taglist))
        print("tagcode:", tgcode)
        return tgcode

    def i3rab(self, nodes:Dict[str, wordNode], stream:streamPattern) -> list:
        """
        Build a phrase based on the stream of word roles and their conjugated forms.
        """
        # Initialize an empty list to construct the phrase
        i3rab_parts = []

        # Iterate through the word role order in the stream
        for key in stream.to_list():
            i3rab_element = {'kind' :'', # inflection for a partial phrase
                             'word' :'',
                             'inflect' :''}
            # Retrieve the corresponding word node
            word_node = nodes.get(key)
            #  some words can be hidden like a pronoun for a verb
            #   # أنت تلعب ==> تلعب
            # Skip if the word node is hidden or has no value
            if word_node and word_node.value and not word_node.hidden:
                # some words generate particles  to be added before and after
                # for example a majzoum future tense need "لم" particalrd
                if word_node.before:
                    i3rab_element = {'kind':  word_node.before,  # inflection for a partial phrase
                                     'word': "word",
                                     'inflect': self.inflect_static(word_node.before),
                                     }
                    i3rab_parts.append(i3rab_element)

                # Add the conjugated word itself
                # i3rab_parts.append(word_node.conjugated)
                i3rab_parts.append({'kind': word_node.conjugated,  # inflection for a partial phrase
                                    'word': "word",
                                    'inflect': self.inflect_static(word_node.after),
                                    })
                # Add any particles or suffixes after the word
                if word_node.after:
                    i3rab_parts.append({'kind':  word_node.after,  # inflection for a partial phrase
                                        'word': "word",
                                        'inflect': self.inflect_static(word_node.after),
                                        })


        # Join the phrase parts with spaces and return the resulting phrase
        return i3rab_parts