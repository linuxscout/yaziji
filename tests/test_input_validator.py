import unittest
from unittest.mock import MagicMock

from libqutrub.verb_const import TenseImperative,  TensePast, TensePassivePast, TenseFuture
from libqutrub.verb_const import  PronounHuwa, PronounAnta

import sys, os
# Local libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "./lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../yaziji"))

from yaziji.yaziji_const import VERBAL_PHRASE, NOMINAL_PHRASE
from yaziji.yaziji_const import ACTIVE_VOICE, PASSIVE_VOICE, AFFIRMATIVE, NEGATIVE



# from yaziji.phrase_generator import PhraseGenerator
from yaziji.validator import Validator

class TestInputValidator(unittest.TestCase):
    def setUp(self):
        # self.phrase_generator = PhraseGenerator()
        self.validator = Validator()


    # @unittest.skip("Test later")
    def test_check_sufficient_component(self):
        # Arrange
        test_set=[  {"id":1,
                    "components":{'subject': '', 'object': '', 'verb': '', 'time': 'أَمْسِ',
                                  'place':'', 'tense': TensePast, 'voice': ACTIVE_VOICE,
                                  'auxiliary': '', 'negative': NEGATIVE, 'phrase_type': VERBAL_PHRASE},
                      "phrase":"ِ",
                      "valid":False,
                     "note": "جملة فارغة",
                    },

                    {"id":2,
                    "components": {'subject': '', 'object': '', 'verb': '', 'time': '', 'place': '', 'tense': 'الماضي المعلوم',
                      'voice': 'مبني للمجهول', 'auxiliary': '', 'negative': 'مثبت', 'phrase_type': 'جملة اسمية',
                       },
                      "phrase":"",
                      "note":"جملة اسمية بلا اسم",
                      "valid":False,
                    },

                    {"id":3,
                    "components": {'subject': 'أَحْمَدُ', 'object': 'تُفَاحَةٌ', 'verb': '', 'time': '', 'place': '',
                                   'tense': 'الماضي المعلوم', 'voice': 'مبني للمجهول', 'auxiliary': '',
                                   'negative': 'مثبت', 'phrase_type': 'جملة فعلية',
                                   },
                      "phrase":"",
                      "note":"جملة فعلية بلا فعل",
                      "valid":False,
                    },

                    {"id": 4,
                     "components": {'subject': '', 'object': '', 'verb': 'اجْتَهَدَ', 'time': '',
                                    'place': '', 'tense': 'الماضي المعلوم', 'voice': 'معلوم',
                                    'auxiliary': '', 'negative': 'مثبت',
                                    'phrase_type': 'جملة فعلية'},

                     'phrase': 'اِجْتَهَدَ',
                     "valid": False,
                     "note": "فعل بلا فاعل ولا مفعول",


                     },
                    {"id": 5,
                     "components": {'subject': '', 'object': 'طَعَامٌ', 'verb': 'أَكَلَ', 'time': '',
                                    'place': '', 'tense': 'الماضي المعلوم', 'voice': ACTIVE_VOICE,
                                    'auxiliary': '', 'negative': 'مثبت', 'phrase_type': 'جملة فعلية',
                                    },

                     'phrase': 'أَكَلَ الطَّعَامَ',
                     "valid": False,
                     "note": "فعل مبني للمعلوم بلا فاعل",
                     },
                    {"id": 6,
                     "components": {'subject': '', 'object': '', 'verb': 'أَكَلَ', 'time': '',
                                    'place': '', 'tense': 'الماضي المعلوم', 'voice': PASSIVE_VOICE,
                                    'auxiliary': '', 'negative': 'مثبت', 'phrase_type': 'جملة فعلية',
                                    },

                     'phrase': 'أُكِلَ',
                     "valid": False,
                     "note": "مبني للمجهول دون نائب فاعل",
                     },

                    {"id": 7,
                     "components": {'subject': 'رَجُلٌ', 'object': '', 'verb': 'أَكَلَ', 'time': '',
                                     'place': '', 'tense': TenseImperative, 'voice': 'معلوم',
                                     'auxiliary': '', 'negative': 'مثبت',
                                     'phrase_type': 'جملة فعلية', },

                     'phrase': 'الرَّجُلُ أَكَلَ',
                     "valid": False,
                     "note": "فعل أمر  بلا ضمير مخاطب",
                     },

                    ###
                    ## Valid cases
                    ##

                    {"id":20,
                    "components":{'subject': 'أَحْمَدُ', 'object': '', 'verb': '', 'time': '',
                                  'place': 'مَسْجِدٌ', 'tense': 'الماضي المعلوم',
                                   'voice': 'مبني للمجهول', 'auxiliary': '', 'negative': 'مثبت',
                                  'phrase_type': NOMINAL_PHRASE,},
                       'phrase': 'أَحْمَدُ فِي الْمَسْجِدِ',
                      "valid":True,
                     "note": "مبتدأ جار ومجرور",
                    },



                   {"id":21,
                    "components":{'subject': '', 'object': 'طَعَامٌ', 'verb': 'أَكَلَ', 'time': '',
                                  'place': '', 'tense': 'الماضي المعلوم', 'voice': PASSIVE_VOICE,
                                  'auxiliary': '', 'negative': 'مثبت', 'phrase_type': 'جملة فعلية',
                                  },

                       'phrase': 'أُكِلَ الطَّعَامُ',
                      "valid":True,
                     "note": "فعل ونائب فاعل",
                    },



                    {"id":22,
                    "components":{'subject': 'مُهَنْدِسٌ', 'object': '', 'verb': 'اشْتَرَى', 'time': 'أَمْسِ',
                                  'place': 'سُوقٌ', 'tense': TensePast, 'voice': ACTIVE_VOICE,
                                  'auxiliary': '', 'negative': NEGATIVE, 'phrase_type': VERBAL_PHRASE},
                      "phrase":"لَمْ يَشْتَرِ الْمُهَنْدِسُ فِي السُّوقِ أَمْسِ",
                      "valid":True,
                     "note": "فعل وفاعل",
                    },

                    {"id":22,
                    "components":{'subject': 'مُهَنْدِسٌ', 'object': '', 'verb': '', 'time': 'أَمْسِ',
                                  'place': '', 'tense': TensePast, 'voice': ACTIVE_VOICE,
                                  'auxiliary': '', 'negative': NEGATIVE, 'phrase_type': NOMINAL_PHRASE,
                                  "adjective":"جميل",
                                  },
                      "phrase":"ِ",
                      "valid":True,
                     "note": "مبتدأ وخبر",
                    },
        ]
        for item in test_set:
            result = self.validator.check_sufficient_components(item["components"])
            note = self.validator.get_note()
            self.assertEqual(result, item["valid"],
                             msg=f"ُExample n°{item['id']}\nResult  :{result}\nExpected:{item['valid']}\nMy Note{item['note']} \nThe Validator Note {note}")

    # @unittest.skip("Test later")
    def test_check_features(self):
        # Arrange
        test_set = [
                {'id': 1,
                'components': {'phrase_type': NOMINAL_PHRASE, 'tense': TenseFuture, 'negative': AFFIRMATIVE,
                               'voice': PASSIVE_VOICE, 'tense_verb': TenseImperative, "transitive":True,
                        'pronoun_verb': PronounHuwa, 'has_verb': False, 'has_auxiliary': True, 'has_object': True, 'has_subject': False},
                'valid': True,
                'note': ''
                },
                {'id': 2,
                'components': {'phrase_type': NOMINAL_PHRASE, 'tense': TenseImperative, 'negative': NEGATIVE,
                               'voice': PASSIVE_VOICE, 'tense_verb': TensePast,            "transitive":False,
                        'pronoun_verb': PronounAnta, 'has_verb': True, 'has_auxiliary': False, 'has_object': True, 'has_subject': True},
                'valid': False,
                'note': 'فعل لازم في المبني للمجهول'
                },
                {'id': 3,
                'components': {'phrase_type': NOMINAL_PHRASE, 'tense': TenseImperative, 'negative': AFFIRMATIVE,
                               'voice': PASSIVE_VOICE, 'tense_verb': TenseImperative,  "transitive":False,
                        'pronoun_verb': PronounAnta, 'has_verb': True, 'has_auxiliary': False, 'has_object': True, 'has_subject': True},
                'valid': False,
                 'note': 'فعل لازم في المبني للمجهول'
                },
                {'id': 4,
                'components': {'phrase_type': NOMINAL_PHRASE, 'tense': TensePast, 'negative': AFFIRMATIVE,
                               'voice': PASSIVE_VOICE, 'tense_verb': TensePast, "transitive":True,
                        'pronoun_verb': PronounAnta, 'has_verb': False, 'has_auxiliary': False, 'has_object': True, 'has_subject': True},
                'valid': True,
                'note': ''
                },
                {'id': 5,
                'components': {'phrase_type': NOMINAL_PHRASE, 'tense': TenseImperative, 'negative': AFFIRMATIVE,
                               'voice': PASSIVE_VOICE, 'tense_verb': TenseImperative,  "transitive":False,
                        'pronoun_verb': PronounAnta, 'has_verb': True, 'has_auxiliary': True, 'has_object': False, 'has_subject': True},
                'valid': False,
                 'note': 'فعل لازم في المبني للمجهول'
                },
                {'id': 6,
                'components': {'phrase_type': VERBAL_PHRASE, 'tense': TenseFuture, 'negative': NEGATIVE,
                               'voice': ACTIVE_VOICE, 'tense_verb': TenseImperative,  "transitive":True,
                        'pronoun_verb': PronounAnta, 'has_verb': False, 'has_auxiliary': True, 'has_object': True, 'has_subject': True},
                'valid': True,
                'note': ''
                },
                {'id': 7,
                'components': {'phrase_type': VERBAL_PHRASE, 'tense': TenseImperative, 'negative': NEGATIVE,
                               'voice': ACTIVE_VOICE, 'tense_verb': TenseImperative,  "transitive":False,
                        'pronoun_verb': PronounHuwa, 'has_verb': True, 'has_auxiliary': False, 'has_object': True, 'has_subject': False},
                'valid': False,
                'note': 'فعل لازم مع مفعول'
                },
                {'id': 8,
                'components': {'phrase_type': NOMINAL_PHRASE, 'tense': TenseFuture, 'negative': NEGATIVE,
                               'voice': PASSIVE_VOICE, 'tense_verb': TenseImperative,   "transitive":True,
                        'pronoun_verb': PronounHuwa, 'has_verb': True, 'has_auxiliary': False, 'has_object': False, 'has_subject': False},
                'valid': False,
                'note': 'فعل متعدٍ بلا مفعول'
                },
                {'id': 9,
                'components': {'phrase_type': VERBAL_PHRASE, 'tense': TensePast, 'negative': AFFIRMATIVE,
                               'voice': ACTIVE_VOICE, 'tense_verb': TenseImperative,  "transitive":False,
                        'pronoun_verb': PronounHuwa, 'has_verb': True, 'has_auxiliary': False, 'has_object': False, 'has_subject': False},
                'valid': False,
                'note': 'فعل أمر بضمير غير مخاطب'
                },
                {'id': 10,
                'components': {'phrase_type': NOMINAL_PHRASE, 'tense': TensePast, 'negative': NEGATIVE,
                               'voice': PASSIVE_VOICE, 'tense_verb': TensePast, "transitive":True,
                        'pronoun_verb': PronounHuwa, 'has_verb': True, 'has_auxiliary': True, 'has_object': True, 'has_subject': False},
                'valid': True,
                'note': ''
                }]



        for item in test_set:
            result = self.validator.check_features(item["components"])
            note = self.validator.get_note()
            self.assertEqual(result, item["valid"],
                             msg=f"ُExample n°{item['id']}\nResult  :{result}\nExpected:{item['valid']}\nMy Note{item['note']} \nThe Validator Note {note}")


    @unittest.skip("Test later")
    def test_load_dictionary_default(self):
        # Arrange
        test_set=[ {"id":1,
                    "components":{'subject': 'تَاجِرٌ', 'object': '', 'verb': 'سَافَرَ', 'time': 'البَارِحَةَ', 'place': 'طَرِيقٌ',
                       'tense': TensePast, 'voice': PASSIVE_VOICE, 'auxiliary': 'اِسْتَطَاعَ',
                       'negative': NEGATIVE, 'phrase_type': NOMINAL_PHRASE},
                     "phrase":"التَّاجِرُ لَمْ يُسْتَطَعْ أَنْ يُسَافَرَ فِي الطَّرِيقِ البَارِحَةَ",
                    "error":"",
                    "valid":True,
                    },
                    {"id":1,
                    "components":{'subject': 'مُهَنْدِسٌ', 'object': '', 'verb': 'اشْتَرَى', 'time': 'أَمْسِ',
                                  'place': 'سُوقٌ', 'tense': TenseImperative, 'voice': ACTIVE_VOICE,
                                  'auxiliary': '', 'negative': NEGATIVE, 'phrase_type': VERBAL_PHRASE},
                      # "phrase":"Imperative Tense Incompatible with pronoun.",
                      "phrase":"",
                      "error":"Error received -1: ERROR: Incompatible Subject مُهَنْدِسٌ and tense 'الأمر'.",
                      "valid":True,
                    },
        ]
        for item in test_set:
            wordindex_attributes = self.phrase_generator.add_features(item["components"])
            self.assertIsNotNone(wordindex_attributes,
                             msg=f"\nError on dictionary loading: {self.phrase_generator.dict_path}.")

    # @unittest.skip("Test later")
    def test_check_unsupported_components(self):
        # Arrange
        test_set = [
                {'id': 9,
                 "components": {'subject': '', 'object': '', 'verb': '', 'time': 'أَمْسِ',
                                'place': '', 'tense': TensePast, 'voice': ACTIVE_VOICE,
                                'auxiliary': '', 'negative': NEGATIVE, 'phrase_type': VERBAL_PHRASE},
                'valid': True,
                'note': ''
                },
                {'id': 10,
                'components': {'wrong_field': NOMINAL_PHRASE,},
                'valid': False,
                'note': 'Unsupported field name'
                }]



        for item in test_set:
            result = self.validator.check_unsupported_components(item["components"])
            note = self.validator.get_note()
            self.assertEqual(result, item["valid"],
                             msg=f"ُExample n°{item['id']}\nResult  :{result}\nExpected:{item['valid']}\nMy Note{item['note']} \nThe Validator Note {note}")

    # @unittest.skip("Test later")
    def test_check_required_components(self):
        # Arrange
        test_set = [
                {'id': 8,
                 "components": {'subject': '', 'object': '', 'verb': '', 'time': 'أَمْسِ',
                                'place': '', 'tense': TensePast, 'voice': ACTIVE_VOICE,
                                'auxiliary': '', 'negative': NEGATIVE, 'phrase_type': VERBAL_PHRASE},
                'valid': True,
                'note': ''
                },
            {'id': 9,
                 "components": {'subject': '', 'object': '', 'verb': '', 'time': 'أَمْسِ',
                                'place': '', 'tense': TensePast, 'voice': ACTIVE_VOICE,
                                'auxiliary': '', 'negative': NEGATIVE, 'phrase_type': ""},
                'valid': False,
                'note': ''
                },
                {'id': 10,
                'components': {'wrong_field': NOMINAL_PHRASE,},
                'valid': False,
                'note': 'Required name'
                }]



        for item in test_set:
            result = self.validator.check_required_components(item["components"])
            note = self.validator.get_note()
            self.assertEqual(result, item["valid"],
                             msg=f"ُExample n°{item['id']}\nResult  :{result}\nExpected:{item['valid']}\nMy Note{item['note']} \nThe Validator Note {note}")


    @unittest.skip("Test later")
    def test_sample(self):
        # Assert message error
        sample = self.validator.check.sample()
        # print(sample)
        self.assertIsNotNone(sample, msg=f"Can't sample data {sample}")
        # self.assertIsNone(sample, msg=f"Can't sample data {sample}")

if __name__ == '__main__':
    unittest.main()
