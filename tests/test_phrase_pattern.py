import unittest
from unittest.mock import patch, MagicMock
from libqutrub.verb_const import TenseImperative, ImperativePronouns, PronounsTable, TensePast, TensePassivePast
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
from yaziji.yaziji_const import FATHA_WORD, DAMMA_WORD, KASRA_WORD
from yaziji.yaziji_const import MARFOU3, MANSOUB, MAJROUR, DEFINED

class TestPhrasePattern(unittest.TestCase):
    def setUp(self,):
        # Creating instance of PhrasePattern
        self.phrase = PhrasePattern()
    # @unittest.skip("Test later")
    def test_add_components_valid(self):
        components_list =[ {"id":1, "components":{'subject': 'هو',
                                    'object': 'كِتَابٌ',
                                    'verb': 'قَرَأَ',
                                    'time': 'كُلَّ يَوْمٍ',
                                    'place': 'غُرْفَةٌ',
                                    'tense': 'المضارع المعلوم',
                                    'voice': 'معلوم',
                                    'auxiliary': 'أَرَادَ',
                                    'negative': 'مثبت',
                                    'phrase_type': 'جملة فعلية'},
                            "valid":True,
                    },
                    {"id": 2, "components": {'subject': 'هو',
                                            'object': 'كِتَابٌ',
                                            'verb': 'قَرَأَ',
                                            'time': 'كُلَّ يَوْمٍ',
                                            'place': 'غُرْفَةٌ',
                                            'tense': 'المضارع المعلوم',
                                            'voice': 'معلوم',
                                            'auxiliary': 'أَرَادَ',
                                            'negative': 'مثبت',
                                            'phrase_type': 'جملة فعلية'},
                    "valid": True,
                    },
            ]
        for item in components_list:
            result = self.phrase.add_components(item["components"])
            # for node in self.phrase.nodes:
            #     print(node.__str__())
            self.assertFalse(result, msg=f"add components \nnames{self.phrase.nodes}\nfeatures{self.phrase.phrase_features}")  # Should return True if preparation is successful

    # @unittest.skip("Test later")
    def test_prepare_valid(self):
        components_list =[ {"id":1, "components":{'subject': 'هو',
                                    'object': 'كِتَابٌ',
                                    'verb': 'قَرَأَ',
                                    'time': 'كُلَّ يَوْمٍ',
                                    'place': 'غُرْفَةٌ',
                                    'tense': 'المضارع المعلوم',
                                    'voice': 'معلوم',
                                    'auxiliary': 'أَرَادَ',
                                    'negative': 'مثبت',
                                    'phrase_type': 'جملة فعلية'},
                            "valid":True,
                    },
                    {"id": 2, "components": {'subject': 'هو',
                                            'object': 'كِتَابٌ',
                                            'verb': 'قَرَأَ',
                                            'time': 'كُلَّ يَوْمٍ',
                                            'place': 'غُرْفَةٌ',
                                            'tense': 'المضارع المعلوم',
                                            'voice': 'معلوم',
                                            'auxiliary': 'أَرَادَ',
                                            'negative': 'مثبت',
                                            'phrase_type': 'جملة فعلية'},
                    "valid": True,
                    },
            ]



        for item in components_list:
            self.phrase.add_components(item["components"])
            result = self.phrase.prepare()
            self.assertIsNone(result)  # Should return True if preparation is successful

    @unittest.skip("Test later")
    def test_check_compatibles_invalid(self):

        # uncompatible cases
        # الأمر مع ضمائر غير المخاطب
        tense = TenseImperative
        for pronoun in PronounsTable:
            if pronoun not in ImperativePronouns:
                self.phrase.nodes["tense"].value = tense
                self.phrase.nodes["subject"].value = pronoun
                result = self.phrase.check_compatibles()
                self.assertEqual(result, -1, msg=f"الزمن {tense}  غير متوافق مع الضمير {pronoun}")  # Should return -1 if incompatible

    @unittest.skip("Test later")
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

    @unittest.skip("Test later")
    @patch('libqutrub.classverb.VerbClass')
    def test_build(self, MockVerbClass):
        mock_conjugate = MagicMock(return_value="مُعَرب")
        MockVerbClass.return_value.conjugate_tense_for_pronoun = mock_conjugate

        components = {
            'subject': 'هو',
            'object': 'كتاب',
            'verb': 'قرأ',
            'tense': 'ماض',
            'negative': 'منفي',
            'voice': 'مبني للمجهول',
            'auxiliary': 'كان',
            'time': 'اليوم',
            'place': 'المدرسة',
            'phrase_type': 'جملة فعلية'
        }
        self.phrase.add_components(components)
        self.phrase.prepare()
        phrase = self.phrase.build()
        self.assertIsInstance(phrase, str)  # Should return a string
        self.assertGreater(len(phrase), 0)  # The phrase should not be empty


    def test_conjugate_noun_by_tags(self):
        # Ensure that the method is callable and runs as expected
        test_set = [
            #valid cases
            {"word":"كِتَابٌ", "conjugated":'الْكِتَابُ',
             "tags":[MARFOU3, DEFINED,],
             "number":"مفرد", "gender":"مذكر", "defined":False, "valid":True,
             },

            #Invalid cases
            {"word": "أَحْمَدُ", "conjugated": 'الْأَحْمَدُ',
             "tags": [MARFOU3, DEFINED, ],
             "number": "مفرد", "gender": "مذكر", "defined": True, "valid": False,
             },
        ]
        for item in test_set:
            wordnode = wordNode("subject", item["word"], gender= item["gender"],
                                number = item["number"],
                                defined=item["defined"])
            conj = self.phrase.conjugate_noun_by_tags(wordnode,item["tags"])
            self.assertEqual(conj == item["conjugated"], item["valid"],
                             msg=f"Output Conjugated:'{conj}', word:{item['word']}\n{item}")
    @unittest.skip("Test later")
    def test_get_pronoun(self,):
        # Mocking noun dictionary lookup to return predefined values
        # MockLookup.return_value = [{"vocalized": "كِتَابٌ"}]
        test_set = [
            { "word":"كِتاب", #kitab
              "feminin":False,
              "number":1,
                    "pronoun":'هو',  "valid":True,
                    "pronoun_aux":'هو', "valid_aux":True,
                    "tense_verb":TensePast, "tense_aux": TensePast
            },
            { "word":"أم", #kitab
              "feminin": True,
              "number": 1,
                    "pronoun":'هي',  "valid":True,
                    "pronoun_aux":'هي', "valid_aux":True,
                    "tense_verb":TensePast, "tense_aux": TensePast
            },

            { "word":"أم", #kitab
              "feminin": True,
              "number": 2,
                    "pronoun":'هما مؤ',  "valid":True,
                    "pronoun_aux":'هما مؤ', "valid_aux":True,
                    "tense_verb":TensePast, "tense_aux": TensePast
            },
            { "word":"أم", #kitab
              "feminin": True,
              "number": 3,
                    "pronoun":'هن',  "valid":True,
                    "pronoun_aux":'هن', "valid_aux":True,
                    "tense_verb":TensePast, "tense_aux": TensePast
            },
            { "word":"أم", #kitab
              "feminin": True,
              "number": "جمع",
                    "pronoun":'هن',  "valid":True,
                    "pronoun_aux":'هي', "valid_aux":True,
                    "tense_verb":TensePast, "tense_aux": TensePassivePast
            },
        ]
        for item in test_set:
            wd = wordNode("subject", item["word"])
            item["gender"] = "مؤنث" if item["feminin"] else "مذكر"
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
        # Mocking noun dictionary lookup to return predefined values
        # MockLookup.return_value = [{"vocalized": "كِتَابٌ"}]
        test_set = [
            {"word" :"كِتاب", #kitab
            "vocalized": "كِتَابٌ","number":"مفرد","gender":"مذكر", "defined":False, "valid":True,
             },
            {"word" :"طاولة", #kitab
            "vocalized": "طَاوِلَةٌ","number":"مفرد","gender":"مؤنث",  "defined":False,"valid":True,
            },
            {"word": "أولاد",  # kitab
             "vocalized": "أَوْلاَدٌ", "number": "جمع تكسير", "gender": "مذكر",  "defined":False,"valid": True,
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

if __name__ == '__main__':
    unittest.main()
