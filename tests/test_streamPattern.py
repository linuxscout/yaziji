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

    @unittest.skip("Test later, Not Implemented")
    def test_add_method(self):
        # Test add method (currently does nothing)
        test_set = [
            {"type":VERBAL_PHRASE, 'add':"IF", "before":"subject",
             "stream":['auxiliary', 'IF', 'subject', 'negation', 'verb', 'object', 'place', 'time'], "valid":True},
            {"type":NOMINAL_PHRASE, 'add':"IF", "after":"object",
             "stream": ['subject', 'IF','auxiliary',  'negation', 'verb', 'object', 'place', 'time'], "valid":True},
        ]
        for item in test_set:
            sp = streamPattern(item["type"])
            if "before" in item:
                sp.add(item["add"], before=item["before"])
            else:
                sp.add(item["add"], after=item["after"])
            # As add method is not implemented, we can't test any outcome
            self.assertEqual(sp.to_list(),item["stream"])

    # @unittest.skip("Test later")
    def test_remove(self):
        # Test remove method
        test_set = [
            {"id":1, "type":VERBAL_PHRASE, 'remove':"negation", "valid":True,
             "stream":['auxiliary', 'subject', 'verb', 'object', 'place', 'time'], },
            {"id":2, "type":NOMINAL_PHRASE, 'remove':"negation", "valid":True,
             "stream": ['subject', 'auxiliary', 'verb', 'object', 'place', 'time'],},
            {"id":3, "type":NOMINAL_PHRASE, 'remove':"negationNotExisting", "valid":True,
             "stream": ['subject', 'auxiliary', 'negation', 'verb', 'object', 'place', 'time'],},
        ]
        for item in test_set:
            sp = streamPattern(item["type"])
            sp.remove(item["remove"])
            # As add method is not implemented, we can't test any outcome
            self.assertEqual(sp.to_list(),item["stream"], msg=f"example n°{item['id']}")

    # @unittest.skip("Test later")
    def test_hide_method(self):
        # Test hide method
        test_set = [
            {"id":1, "type":VERBAL_PHRASE, 'hide':"negation", "valid":True,
             "stream":['auxiliary', 'subject', 'verb', 'object', 'place', 'time'], },
            {"id":2, "type":NOMINAL_PHRASE, 'hide':"negation", "valid":True,
             "stream": ['subject', 'auxiliary', 'verb', 'object', 'place', 'time'],},
            {"id":3, "type":NOMINAL_PHRASE, 'hide':"negationNotExisting", "valid":False,
             "stream": ['subject', 'auxiliary', 'negation', 'verb', 'object', 'place', 'time'],},
        ]
        for item in test_set:
            sp = streamPattern(item["type"])
            sp.hide(item["hide"])
            if item["valid"]:
                self.assertIn(item["hide"], sp.hidden)
            else:
                self.assertNotIn(item["hide"], sp.hidden)

    # @unittest.skip("Test later")
    def test_unhide_method(self):
        # Test unhide method
        test_set = [
            {"id":1, "type":VERBAL_PHRASE, 'hide':"negation", "valid":True,
             "stream":['auxiliary', 'subject', 'verb', 'object', 'place', 'time'], },
            {"id":2, "type":NOMINAL_PHRASE, 'hide':"negation", "valid":True,
             "stream": ['subject', 'auxiliary', 'verb', 'object', 'place', 'time'],},
            {"id":3, "type":NOMINAL_PHRASE, 'hide':"negationNotExisting", "valid":False,
             "stream": ['subject', 'auxiliary', 'negation', 'verb', 'object', 'place', 'time'],},
        ]
        for item in test_set:
            sp = streamPattern(item["type"])
            sp.hide(item["hide"])
            sp.unhide(item["hide"])
            self.assertNotIn(item["hide"], sp.hidden)

    # @unittest.skip("Test later")
    def test_list_method(self):
        # Test list method
        test_set = [
            {"id":1, "type":VERBAL_PHRASE,  "valid":True,
             "stream":['auxiliary', 'subject', 'negation','verb', 'object', 'place', 'time'], },
            {"id":2, "type":NOMINAL_PHRASE,  "valid":True,
             "stream": ['subject', 'auxiliary', 'negation','verb', 'object', 'place', 'time'],},
        ]
        for item in test_set:
            sp = streamPattern(item["type"])
            self.assertEqual(sp.to_list(),item["stream"], msg=f"example n°{item['id']}")


    def test_str_method(self):
        # Test string representation method
        test_set = [
            {"id":1, "type":VERBAL_PHRASE,  "valid":True,
             "stream":['auxiliary', 'subject', 'negation','verb', 'object', 'place', 'time'],
             "str":"<auxiliary><subject><negation><verb><object><place><time>"},
            {"id":2, "type":NOMINAL_PHRASE,  "valid":True,
             "stream": ['subject', 'auxiliary', 'negation','verb', 'object', 'place', 'time'],
             "str":"<subject><auxiliary><negation><verb><object><place><time>",
             },
        ]
        for item in test_set:
            sp = streamPattern(item["type"])
            result = sp.__str__()
            self.assertEqual(result, item["str"], msg=f"example n°{item['id']}")


if __name__ == "__main__":
    unittest.main()
