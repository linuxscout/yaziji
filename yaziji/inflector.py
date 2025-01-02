import logging
from typing import Dict, List, Optional

from libqutrub.verb_const import TenseImperative,  TensePast, TensePassivePast, TenseFuture
from libqutrub.verb_const import  ImperativePronouns, PronounsTable


# Local libraries

from yaziji_const import NOUN_TYPE
# from yaziji_const import ACTIVE_VOICE, PASSIVE_VOICE, AFFIRMATIVE, NEGATIVE
from yaziji_const import STATIC_INFLECTION

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
        return STATIC_INFLECTION.get(word, '')

    def inflect_word(self, word_node: wordNode):
        """
        Inflect a list of predifined words, like FI, MIN
        :param word:
        :return:
        """

        word_node.tagcode = self.tagcoder.encode(word_node.tags)
        # print("tags list:", u";".join(taglist))
        # print("tagcode:", tgcode)
        word_node.inflection = self.taginflecter.inflect(word_node.tagcode)
        # change inflection according to word fucntion
        word_node.inflection = self.add_function(word_node)

        # print("Inflection", inflection)
        # return f"{word_node.tags}[{word_node.tagcode}]: {word_node.inflection}"
        return word_node.inflection

    def add_function(self, wordnode):
        """
        add funciton to inflection
        :param wordnode:
        :return:
        """
        inflection = wordnode.inflection
        if wordnode.function:
            if inflection.startswith(NOUN_TYPE):
                inflection = inflection[len(NOUN_TYPE):]
            inflection = wordnode.function + inflection
        return inflection

    def inflect_nodes(self, nodes:Dict[str, wordNode], stream:streamPattern) -> list:
        """
        Build a phrase based on the stream of word roles and their conjugated forms.
        """
        # Initialize an empty list to construct the phrase
        i3rab_parts = []

        # Iterate through the word role order in the stream
        for key in stream.to_list():
            i3rab_element = {'kind' :'', # inflection for a partial phrase
                             'word' :'',
                             # "conjugable": '',
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
                                     # "conjugable": False,
                                     'inflect': self.inflect_static(word_node.before),
                                     }
                    i3rab_parts.append(i3rab_element)

                # Add the conjugated word itself
                # i3rab_parts.append(word_node.conjugated)

                if word_node.conjugable:
                    inflect_result = self.inflect_word(word_node)
                else:
                    inflect_result = self.inflect_static(word_node.word)

                i3rab_parts.append({'kind': word_node.conjugated,  # inflection for a partial phrase
                                    'word': "word",
                                    # "conjugable":word_node.conjugable,
                                    'inflect': inflect_result,
                                    })
                # Add any particles or suffixes after the word
                if word_node.after:
                    i3rab_parts.append({'kind':  word_node.after,  # inflection for a partial phrase
                                        'word': "word",
                                        # "conjugable": False,
                                        'inflect': self.inflect_static(word_node.after),
                                        })

        # Join the phrase parts with spaces and return the resulting phrase
        return i3rab_parts

    def to_string(self, inflect_parts, sep="\n"):
        """

        :param inflect_parts:
        :param sep:
        :return:
        """
        texts = []
        for item in inflect_parts:
            if item['kind']:
                texts.append(f"'{item['kind']}': '{item['inflect']}'.")
        return sep.join(texts)