import unittest
from unittest.mock import patch
import sys, os
# Local libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "./lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../yaziji"))
from yaziji.yaziji_const import STREAMS, VERBAL_PHRASE, NOMINAL_PHRASE
from yaziji.stream_pattern import streamPattern


class TestStreamPattern(unittest.TestCase):

    def setUp(self):
        # Mock STREAMS for testing
        pass
    # @unittest.skip("Test later")
    def test_initialization_valid_stream(self):
        # Test initialization with valid stream type
        test_set = [
            {"type":VERBAL_PHRASE, "valid":True},
            {"type":NOMINAL_PHRASE, "valid":True},
            {"type":"default", "valid":True},
            {"type":"type1", "valid":False},
        ]
        for item in test_set:
            if item["valid"]:
                sp = streamPattern(item["type"])
                self.assertEqual(sp.type!=None, item["valid"],
                                 msg=f" stream '{item['type']}'")
            else:
                with self.assertRaises(KeyError) as context:
                    streamPattern(item["type"])

                self.assertEqual(str(context.exception), f"('steam_pattern.py:Phrase type not exists', '{item['type']}')")

    @unittest.skip("Test later")
    def test_initialization_invalid_stream(self):
        # Test initialization with invalid stream type
        with self.assertRaises(KeyError):
            streamPattern('invalid_type')

    @unittest.skip("Test later")
    def test_add_method(self):
        # Test add method (currently does nothing)
        sp = streamPattern('type1')
        sp.add('d', before='b')
        # As add method is not implemented, we can't test any outcome
        self.assertIsNone(sp.add('d', before='b'))

    @unittest.skip("Test later")
    def test_remove_existing(self):
        # Test remove method with existing item
        sp = streamPattern('type1')
        sp.remove('b')
        self.assertNotIn('b', sp.stream)

    @unittest.skip("Test later")
    def test_remove_non_existing(self):
        # Test remove method with non-existing item
        sp = streamPattern('type1')
        sp.remove('z')  # Not in stream
        self.assertEqual(sp.stream, ['a', 'b', 'c'])  # Stream should remain the same

    @unittest.skip("Test later")
    def test_hide_method(self):
        # Test hide method
        sp = streamPattern('type1')
        sp.hide('a')
        self.assertIn('a', sp.hidden)

    @unittest.skip("Test later")
    def test_unhide_method(self):
        # Test unhide method
        sp = streamPattern('type1')
        sp.hide('a')
        sp.unhide('a')
        self.assertNotIn('a', sp.hidden)

    @unittest.skip("Test later")
    def test_list_method(self):
        # Test list method
        sp = streamPattern('type1')
        result = sp.__list__()
        self.assertEqual(result, ['a', 'b', 'c'])
    @unittest.skip("Test later")
    def test_str_method(self):
        # Test string representation method
        sp = streamPattern('type1')
        result = sp.__str__()
        self.assertEqual(result, "<a><b><c>")


if __name__ == "__main__":
    unittest.main()
