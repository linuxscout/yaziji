import unittest

import sys, os
# Local libraries
from libqutrub.verb_const import TenseFuture, TensePast

sys.path.append(os.path.join(os.path.dirname(__file__), "./lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../yaziji"))
# Import the classes and methods
from yaziji.inflector import Inflector
from yaziji.wordnode import wordNode
from yaziji.stream_pattern import streamPattern
from yaziji.phrase_generator import PhraseGenerator
from yaziji.yaziji_const import FATHA_WORD, DAMMA_WORD, KASRA_WORD
from yaziji.yaziji_const import MARFOU3, MANSOUB, MAJROUR, DEFINED, VERBAL_PHRASE, NOMINAL_PHRASE
from yaziji.yaziji_const import ACTIVE_VOICE, PASSIVE_VOICE, AFFIRMATIVE, NEGATIVE
from yaziji.yaziji_const import NUMBER_SINGULAR, NUMBER_DUAL, NUMBER_PLURAL, GENDER_FEMALE, GENDER_MALE


class TestInflector(unittest.TestCase):
    def setUp(self):
        """Set up the mock objects and an instance of Inflector."""
        # Mock componentsSet

        # Mock nodes dictionary
        # Create an instance of Inflector with mocked data
        self.inflector = Inflector()
        self.phrase_generator = PhraseGenerator()

    @unittest.skip("Test later")
    def test_inflect_static(self):
        """Test the inflect_static method."""
        result = self.inflector.inflect_static("FI")
        self.assertEqual(result, "")

    @unittest.skip("Test later")
    def test_inflect_word(self):
        """Test the inflect_word method."""


        test_set=[ {"id":1,
                    "components":{'subject': 'تَاجِرٌ', 'object': '', 'verb': 'سَافَرَ', 'time': 'البَارِحَةَ', 'place': 'طَرِيقٌ',
                       'tense': TensePast, 'voice': PASSIVE_VOICE, 'auxiliary': 'اِسْتَطَاعَ',
                       'negative': NEGATIVE, 'phrase_type': NOMINAL_PHRASE},
                     "phrase":"التَّاجِرُ لَمْ يُسْتَطَعْ أَنْ يُسَافَرَ فِي الطَّرِيقِ البَارِحَةَ",
                    "valid":True,
                    },
                    {"id":2,
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
            nodes = self.phrase_generator.pattern.nodes
            stream = self.phrase_generator.pattern.stream
            # features = self.phrase_generator.pattern.phrase_features
            print(f"--------Example n°{item['id']}-----------------")
            print("PHRASE:",phrase)
            for key,wdnode in nodes.items():
                if key in stream.to_list():
                    # print("Node", wdnode)
                    # print("Node tags", wdnode.tags)
                    inflection = self.inflector.inflect_word(wdnode)
                    self.assertTrue(inflection,
                                    msg= f"Name: '{wdnode.name}', word:'{wdnode.word}:{wdnode.conjugated}', tags:{wdnode.tags} \ncode '{wdnode.tagcode}' \tinflection: '{inflection}'")
        # self.assertTrue(False)
            # self.assertEqual(phrase == item["phrase"], item["valid"],
            #                  msg=f"\nResult  :{result}\nExpected:{item['phrase']}")  # Should return True if preparation is successful


    # @unittest.skip("Test later")
    def test_inflect_nodes(self):
        """Test the i3rab method."""
        # Override nodes with mock data


        test_set=[ {"id":1,
                    "components":{'subject': 'تَاجِرٌ', 'object': '', 'verb': 'سَافَرَ', 'time': 'البَارِحَةَ', 'place': 'طَرِيقٌ',
                       'tense': TensePast, 'voice': PASSIVE_VOICE, 'auxiliary': 'اِسْتَطَاعَ',
                       'negative': NEGATIVE, 'phrase_type': NOMINAL_PHRASE},
                     "phrase":"التَّاجِرُ لَمْ يُسْتَطَعْ أَنْ يُسَافَرَ فِي الطَّرِيقِ البَارِحَةَ",
                    "valid":True,
                    },
                    {"id":2,
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
            nodes = self.phrase_generator.pattern.nodes
            stream = self.phrase_generator.pattern.stream
            features = self.phrase_generator.pattern.phrase_features
            inflect_parts = self.inflector.inflect_nodes(nodes, stream)
            inflect_text = self.inflector.to_string(inflect_parts)
            self.assertTrue(inflect_text,
                            msg=f"Example n°{item['id']}: Inflection for '{phrase}'\n{inflect_text}.")


    @unittest.skip("Test later")
    def test_i3rab_with_hidden_node(self):
        """Test i3rab when a word node is hidden."""
        # Make one node hidden
        self.mock_word_node.hidden = True
        self.inflector.nodes = {"key1": self.mock_word_node}

        # Call the method
        result = self.inflector.i3rab()

        # Expect empty list as all nodes are hidden
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
