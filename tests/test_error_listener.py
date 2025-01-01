import unittest
from unittest.mock import MagicMock

from libqutrub.verb_const import TenseImperative,  TensePast, TensePassivePast, TenseFuture
from libqutrub.verb_const import  PronounHuwa, PronounAnta

import sys, os
# Local libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "./lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../yaziji"))


# from yaziji.phrase_generator import PhraseGenerator
from yaziji.error_listener import ErrorListener, ERROR_MESSAGES

class TestInputErrorListener(unittest.TestCase):
    def setUp(self):
        # self.phrase_generator = PhraseGenerator()
        self.observer = ErrorListener()


    # @unittest.skip("Test later")
    def test_get_errorno(self):
        # Arrange
        for msg in ERROR_MESSAGES:
            result = self.observer.get_errorno(msg)
            self.assertTrue(result> 0,
                             msg=f"ُExample message ID '{msg}'\nResult  :{result}")
        msg = "ANYTHING"
        result = self.observer.get_errorno(msg)
        self.assertFalse(result > 0,
                         msg=f"ُExample message ID '{msg}'\nResult  :{result}")

if __name__ == '__main__':
    unittest.main()
