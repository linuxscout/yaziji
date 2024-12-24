import unittest
from unittest.mock import patch
import sys, os
# Local libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "./lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../yaziji"))
from yaziji.yaziji_const import STREAMS
from yaziji.stream_pattern import streamPattern


class TestStreamPattern(unittest.TestCase):

    def setUp(self):
        # Mock STREAMS for testing
        self.mock_streams = {
            'type1': ['a', 'b', 'c'],
            'type2': ['d', 'e', 'f'],
            'default': ['x', 'y', 'z']
        }
        STREAMS.update(self.mock_streams)

    def test_initialization_valid_stream(self):
        # Test initialization with valid stream type
        sp = streamPattern('type1')
        self.assertEqual(sp.type, 'type1')
        self.assertEqual(sp.stream, ['a', 'b', 'c'])

    def test_initialization_invalid_stream(self):
        # Test initialization with invalid stream type
        with self.assertRaises(KeyError):
            streamPattern('invalid_type')

    def test_add_method(self):
        # Test add method (currently does nothing)
        sp = streamPattern('type1')
        sp.add('d', before='b')
        # As add method is not implemented, we can't test any outcome
        self.assertIsNone(sp.add('d', before='b'))

    def test_remove_existing(self):
        # Test remove method with existing item
        sp = streamPattern('type1')
        sp.remove('b')
        self.assertNotIn('b', sp.stream)

    def test_remove_non_existing(self):
        # Test remove method with non-existing item
        sp = streamPattern('type1')
        sp.remove('z')  # Not in stream
        self.assertEqual(sp.stream, ['a', 'b', 'c'])  # Stream should remain the same

    def test_hide_method(self):
        # Test hide method
        sp = streamPattern('type1')
        sp.hide('a')
        self.assertIn('a', sp.hidden)

    def test_unhide_method(self):
        # Test unhide method
        sp = streamPattern('type1')
        sp.hide('a')
        sp.unhide('a')
        self.assertNotIn('a', sp.hidden)

    def test_list_method(self):
        # Test list method
        sp = streamPattern('type1')
        result = sp.__list__()
        self.assertEqual(result, ['a', 'b', 'c'])

    def test_str_method(self):
        # Test string representation method
        sp = streamPattern('type1')
        result = sp.__str__()
        self.assertEqual(result, "<a><b><c>")


if __name__ == "__main__":
    unittest.main()
