import unittest
from unittest.mock import MagicMock

from libqutrub.verb_const import TenseImperative,  TensePast, TensePassivePast, TenseFuture
from libqutrub.verb_const import  ImperativePronouns, PronounsTable

import sys, os
# Local libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "./lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../yaziji"))

from yaziji.yaziji_const import VERBAL_PHRASE, NOMINAL_PHRASE
from yaziji.yaziji_const import ACTIVE_VOICE, PASSIVE_VOICE, AFFIRMATIVE, NEGATIVE


from yaziji.phrase_generator import PhraseGenerator

class TestPhraseGenerator(unittest.TestCase):
    def setUp(self):
        self.phrase_generator = PhraseGenerator()


    # @unittest.skip("Test later")
    def test_build_error_success(self):
        # Arrange
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
            result = self.phrase_generator.build(item["components"])
            phrase = result.get("phrase",'')
            self.assertEqual(phrase == item["phrase"], item["valid"],
                             msg=f"\nResult  :{result}\nExpected:{item['phrase']}")  # Should return True if preparation is successful

    # @unittest.skip("Test later")
    def test_build_error_handling(self):
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
                      # "error":"Error received -1: ERROR: Incompatible Subject مُهَنْدِسٌ and tense 'الأمر'.",
                      "error":"Error received INCOMPATIBLE_SUBJECT_TENSE: ERROR: Incompatible Subject 'مُهَنْدِسٌ' and tense 'الأمر'.",
                      "valid":True,
                    },
        ]
        for item in test_set:
            result = self.phrase_generator.build(item["components"])
            phrase = result.get("phrase",'')
            errors = result.get("errors",'')
            self.assertEqual(phrase == item["phrase"], item["valid"],
                             msg=f"\nResult  :'{result}'\nExpected:'{item['phrase']}'")
            self.assertEqual(errors == item["error"], item["valid"],
                             msg=f"\nResult  :'{errors}'\nExpected:'{item['error']}'")

    # @unittest.skip("Test later")
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


    def test_sample(self):
        # Assert message error
        sample = self.phrase_generator.sample()
        # print(sample)
        self.assertIsNotNone(sample, msg=f"Can't sample data {sample}")
        # self.assertIsNone(sample, msg=f"Can't sample data {sample}")

if __name__ == '__main__':
    unittest.main()
