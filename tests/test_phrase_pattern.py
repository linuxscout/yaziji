import unittest
from unittest.mock import patch, MagicMock
from libqutrub.verb_const import TenseImperative,  TensePast, TensePassivePast, TenseFuture
from libqutrub.verb_const import  ImperativePronouns, PronounsTable
from pyarabic import araby

import alyahmor.verb_affixer
import arramooz.arabicdictionary

import sys, os
# Local libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "./lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../yaziji"))
from yaziji.phrase_pattern import PhrasePattern  # Assuming the class is in phrase_pattern.py
from yaziji.wordnode import wordNode
from yaziji.error_listener import ErrorListener
from yaziji.yaziji_const import FATHA_WORD, DAMMA_WORD, KASRA_WORD
from yaziji.yaziji_const import MARFOU3, MANSOUB, MAJROUR, DEFINED, VERBAL_PHRASE, NOMINAL_PHRASE
from yaziji.yaziji_const import ACTIVE_VOICE, PASSIVE_VOICE, AFFIRMATIVE, NEGATIVE
from yaziji.yaziji_const import NUMBER_SINGULAR, NUMBER_DUAL, NUMBER_PLURAL, GENDER_FEMALE, GENDER_MALE

class TestPhrasePattern(unittest.TestCase):
    def setUp(self,):
        # Creating instance of PhrasePattern
        self.phrase = PhrasePattern()
    # @unittest.skip("Test later")


    # @unittest.skip("Test later")
    def test_check_compatibles_invalid(self):

        # uncompatible cases
        # الأمر مع ضمائر غير المخاطب
        tense = TenseImperative
        for pronoun in PronounsTable:
            if pronoun not in ImperativePronouns:
                self.phrase.phrase_features["tense"] = tense
                self.phrase.nodes["subject"].value = pronoun
                result = self.phrase.check_compatibles()
                self.assertEqual(result, -1, msg=f"الزمن ' {tense}'  غير متوافق مع الضمير '{pronoun}'.") # Should return -1 if incompatible

    # @unittest.skip("Test later")
    def test_check_compatibles_valid(self):
        # uncompatible cases
        # الأمر مع ضمائر غير المخاطب
        tense = TenseImperative
        for pronoun in ImperativePronouns:
            self.phrase.nodes["tense"].value = tense
            self.phrase.nodes["subject"].value = pronoun
            result = self.phrase.check_compatibles()
            self.assertTrue(result, msg=f"الزمن {tense}  متوافق مع الضمير {pronoun}")  # Should return True if compatible
        #TODO: Add more imcompatible cases


    def test_notify_error(self):
        # test how to manage errors
        self.phrase.error_observer = ErrorListener()
        self.assertIsNotNone(self.phrase.error_observer, msg="Error lister is None")

        self.phrase.notify_error(-1, "Just a test")
        message = 'Error received -1: Just a test'
        # return a list of message
        result_list = self.phrase.error_observer.show_errors()
        self.assertIn(message, result_list, "Message not in list errors")



    def test_conjugate_noun_by_tags(self):
        # Ensure that the method is callable and runs as expected
        test_set = [
            #valid cases
            {"word":"كِتَابٌ", "conjugated":'الْكِتَابُ',
             "tags":[MARFOU3, DEFINED,],
             "number":NUMBER_SINGULAR, "gender":GENDER_MALE, "defined":False, "valid":True,
             },

            #Invalid cases
            {"word": "أَحْمَدُ", "conjugated": 'الْأَحْمَدُ',
             "tags": [MARFOU3, DEFINED, ],
             "number": NUMBER_SINGULAR, "gender": GENDER_MALE, "defined": True, "valid": False,
             },
        ]
        for item in test_set:
            wordnode = wordNode("subject", item["word"], gender= item["gender"],
                                number = item["number"],
                                defined=item["defined"])
            conj = self.phrase.conjugate_noun_by_tags(wordnode,item["tags"])
            self.assertEqual(conj == item["conjugated"], item["valid"],
                             msg=f"Output Conjugated:'{conj}', word:{item['word']}\n{item}")
    # @unittest.skip("Test later")
    def test_get_pronoun(self,):
        # Mocking noun dictionary lookup to return predefined values
        # MockLookup.return_value = [{"vocalized": "كِتَابٌ"}]
        test_set = [
            { "word":"كِتاب", #kitab
              "feminin":False,
              "number":NUMBER_SINGULAR,
                    "pronoun":'هو',  "valid":True,
                    "pronoun_aux":'هو', "valid_aux":True,
                    "tense_verb":TensePast, "tense_aux": TensePast
            },
            { "word":"أم", #kitab
              "feminin": True,
              "number": NUMBER_SINGULAR,
                    "pronoun":'هي',  "valid":True,
                    "pronoun_aux":'هي', "valid_aux":True,
                    "tense_verb":TensePast, "tense_aux": TensePast
            },

            { "word":"أم", #kitab
              "feminin": True,
              "number": NUMBER_DUAL,
                    "pronoun":'هما مؤ',  "valid":True,
                    "pronoun_aux":'هما مؤ', "valid_aux":True,
                    "tense_verb":TensePast, "tense_aux": TensePast
            },
            { "word":"أم", #kitab
              "feminin": True,
              "number": NUMBER_PLURAL,
                    "pronoun":'هن',  "valid":True,
                    "pronoun_aux":'هن', "valid_aux":True,
                    "tense_verb":TensePast, "tense_aux": TensePast
            },
            { "word":"أم", #kitab
              "feminin": True,
              "number": NUMBER_PLURAL,
                    "pronoun":'هن',  "valid":True,
                    "pronoun_aux":'هي', "valid_aux":True,
                    "tense_verb":TensePast, "tense_aux": TensePassivePast
            },
        ]
        for item in test_set:
            wd = wordNode("subject", item["word"])
            item["gender"] = GENDER_FEMALE if item["feminin"] else GENDER_MALE
            wd.update(item)
            pronoun, pronoun_aux = self.phrase.get_pronoun(wd, item["tense_verb"] ,item["tense_aux"],
                                                           # feminin=item["feminin"],
                                                           # number=item["number"]
                                                           )
            #check pronoun
            self.assertEqual(pronoun == item["pronoun"], item["valid"],
                             msg=f"Output Pronoun:'{pronoun}', word:{item['word']}\n{item}")
            # check auxilary pronoun
            self.assertEqual(pronoun_aux == item["pronoun_aux"], item["valid_aux"],
                             msg=f"Output Auxilary Pronoun:'{pronoun}', word:'{item['word']}'\n{item}")


    def test_get_noun_attributes(self,):

        test_set = [
            {"word" :"كِتاب", #kitab
            "vocalized": "كِتَابٌ","number":NUMBER_SINGULAR,"gender":GENDER_MALE, "defined":False, "valid":True,
             },
            {"word" :"طاولة", #kitab
            "vocalized": "طَاوِلَةٌ","number":NUMBER_SINGULAR,"gender":GENDER_FEMALE,  "defined":False,"valid":True,
            },
            {"word": "أولاد",  # kitab
             "vocalized": "أَوْلاَدٌ", "number": "جمع تكسير", "gender": GENDER_MALE,  "defined":False,"valid": True,
             },
        ]
        attr_list = ["vocalized", "number","gender", "defined"]
        for item in test_set:
            attributes = self.phrase.get_noun_attributes(item["word"])
            for attr in attr_list:
                output = attributes.get(attr, "N/A")
                self.assertEqual(output == item[attr], item['valid'],
                     msg=f"word:'{item['word']}', attribute:'{attr}', output:{output}, expected:'{item[attr]}'\n{attributes.get_wordtype()}\n{attributes}")  # Ensure it returns the vocalized form

    def test_get_verb_attributes(self):
        ## test how to get valid verbs with respect of future type and transitivity
        test_set = [
            #valid cases
            {"vocalized": "فَتَحَ", "future_type": FATHA_WORD, "transitive": True,"valid_future":True, "valid_trans":True,},
            {"vocalized": "كَتَبَ", "future_type": DAMMA_WORD, "transitive": True,"valid_future":True, "valid_trans":True},
            {"vocalized": "أَكَلَ", "future_type": DAMMA_WORD, "transitive": True,"valid_future":True, "valid_trans":True},
            {"vocalized": "ضَرَبَ", "future_type": KASRA_WORD, "transitive": True,"valid_future":True, "valid_trans":True},

            # invalid cases
            {"vocalized": "جَلَسَ", "future_type": DAMMA_WORD, "transitive": False, "valid_future": False, "valid_trans":True},
            {"vocalized": "أَكَلَ", "future_type": KASRA_WORD, "transitive": False, "valid_future": False, "valid_trans":False},
        ]
        for item in test_set:
            verb = item["vocalized"]
            f_type = item["future_type"]
            trans = item["transitive"]
            # transitive, future_type = self.phrase.get_verb_attributes()
            ver_tuple = self.phrase.get_verb_attributes(verb, future_type=f_type, transitive=trans)
            out_trans: bool = ver_tuple.is_transitive()
            out_f_type = ver_tuple.get_future_type()
            self.assertTrue(ver_tuple, msg=f"Verb:'{verb}', future mark:'{f_type}, transitive:{trans}")
            # check future mark validity as expected
            self.assertEqual(f_type == out_f_type, item["valid_future"],
                             msg=f"Verb:'{verb}', Future Type: expected:'{f_type}', found:'{out_f_type}'")  # Ensure future type is returned correctly
            # check transitivity validity as expected
            self.assertEqual(trans == out_trans, item["valid_trans"],
                             msg=f"Verb:'{verb}', Transitivity: expected:'{trans}', found:'{out_trans}'")  # Ensure future type is returned correctly

    def test_add_components_valid(self):
        components_list =[ {"id":1, "components":{'subject': 'هو',
                                    'object': 'كِتَابٌ',
                                    'verb': 'قَرَأَ',
                                    'time': 'كُلَّ يَوْمٍ',
                                    'place': 'غُرْفَةٌ',
                                    'tense': TenseFuture,
                                    'voice': ACTIVE_VOICE,
                                    'auxiliary': 'أَرَادَ',
                                    'negative': AFFIRMATIVE,
                                    'phrase_type': VERBAL_PHRASE},
                            "valid":True,
                    },
                    {"id": 2, "components": {'subject': 'هو',
                                            'object': 'كِتَابٌ',
                                            'verb': 'قَرَأَ',
                                            'time': 'كُلَّ يَوْمٍ',
                                            'place': 'غُرْفَةٌ',
                                            'tense': TenseFuture,
                                            'voice': ACTIVE_VOICE,
                                            'auxiliary': 'أَرَادَ',
                                            'negative': AFFIRMATIVE,
                                            'phrase_type': VERBAL_PHRASE},
                    "valid": True,
                     },

                    {"id": 3, "components": {'subject': 'هو',
                                            'object': 'كِتَابٌ',
                                            'verb': 'قَرَأَ',
                                            'time': 'كُلَّ يَوْمٍ',
                                            'place': 'غُرْفَةٌ',
                                            'tense': TenseFuture,
                                            'voice': ACTIVE_VOICE,
                                            'auxiliary': 'أَرَادَ',
                                            'negative': AFFIRMATIVE,
                                            #'phrase_type': VERBAL_PHRASE
                                              },
                    "valid": False,
                    },
                    {"id": 4, "components": {'subject': 'هو',
                                            'object': 'كِتَابٌ',
                                            'verb': 'قَرَأَ',
                                            'time': 'كُلَّ يَوْمٍ',
                                            'place': 'غُرْفَةٌ',
                                            'tense': TenseFuture,
                                            'voice': ACTIVE_VOICE,
                                            'auxiliary': 'أَرَادَ',
                                            'negative': AFFIRMATIVE,
                                            'phrase_type': VERBAL_PHRASE,
                                            'wrong_name': 'حقل غير معروف'
                                              },
                    "valid": False,
                    },
            ]
        for item in components_list:
            result = self.phrase.add_components(item["components"])
            self.assertEqual(result > 0,item["valid"], msg=f"add components \nnames{self.phrase.nodes}\nfeatures{self.phrase.phrase_features}")  # Should return True if preparation is successful

    # @unittest.skip("Test later")
    def test_prepare_valid(self):
        components_list =[ {"id":1, "components":{'subject': 'هو',
                                    'object': 'كِتَابٌ',
                                    'verb': 'قَرَأَ',
                                    'time': 'كُلَّ يَوْمٍ',
                                    'place': 'غُرْفَةٌ',
                                    'tense': TenseFuture,
                                    'voice': ACTIVE_VOICE,
                                    'auxiliary': 'أَرَادَ',
                                    'negative': AFFIRMATIVE,
                                    'phrase_type': VERBAL_PHRASE},
                            "valid":True,
                    },
                    {"id": 2, "components": {'subject': 'هو',
                                            'object': 'كِتَابٌ',
                                            'verb': 'قَرَأَ',
                                            'time': 'كُلَّ يَوْمٍ',
                                            'place': 'غُرْفَةٌ',
                                            'tense': TenseFuture,
                                            'voice': ACTIVE_VOICE,
                                            'auxiliary': 'أَرَادَ',
                                            'negative': AFFIRMATIVE,
                                            'phrase_type': VERBAL_PHRASE},
                    "valid": True,
                    },
            ]



        for item in components_list:
            self.phrase.add_components(item["components"])
            result = self.phrase.prepare()
            self.assertTrue(result)  # Should return True if preparation is successful

    # @unittest.skip("Test later")
    def test_build(self):
        test_set=[ {"id":1,
                    "components":{'subject': 'تَاجِرٌ', 'object': '', 'verb': 'سَافَرَ', 'time': 'البَارِحَةَ', 'place': 'طَرِيقٌ',
                       'tense': TensePast, 'voice': PASSIVE_VOICE, 'auxiliary': 'اِسْتَطَاعَ',
                       'negative': NEGATIVE, 'phrase_type': NOMINAL_PHRASE},
                     "phrase":"التَّاجِرُ لَمْ يُسْتَطَعْ أَنْ يُسَافَرَ فِي الطَّرِيقِ البَارِحَةَ",
                    "valid":True,
                    },
                    {"id":1,
                    "components":{'subject': 'مُهَنْدِسٌ', 'object': '', 'verb': 'اشْتَرَى', 'time': 'أَمْسِ',
                                  'place': 'سُوقٌ', 'tense': TensePast, 'voice': ACTIVE_VOICE,
                                  'auxiliary': '', 'negative': NEGATIVE, 'phrase_type': VERBAL_PHRASE},
                      "phrase":"لَمْ يَشْتَرِ الْمُهَنْدِسُ فِي السُّوقِ أَمْسِ",
                      "valid":False,
                    },
        ]
        for item in test_set:
            self.phrase.add_components(item["components"])
            self.phrase.prepare()
            result = self.phrase.build()
            self.assertEqual(result == item["phrase"], item["valid"],
                            msg= f"\nResult  :{result}\nExpected:{item['phrase']}")  # Should return True if preparation is successful


if __name__ == '__main__':
    unittest.main()
