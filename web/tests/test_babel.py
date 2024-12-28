import unittest

import sys, os
import json
# Local libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from yaziji_babel import app  # Import your Flask app instance


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client for the Flask app."""
        self.app = app.test_client()
        self.app.testing = True
        self.languages = "ar,bn,de,en,es,fr,id,ja,ku,zh,he".split(',')

    def test_select_get(self):
        """Test the selectGet route."""
        response = self.app.get('/selectGet')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIn(b'fields', response.data, msg=f"Returned Data {data.keys()}\n{data}")
        self.assertIn(b'web-labels', response.data, msg=f"Returned Data {data.keys()}\n{data}")


    def test_select_get_lang(self):
        """Test the selectGet route."""
        languages = self.languages
        for lang in languages:
            response = self.app.get(f'/{lang}/selectGet')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode('utf-8'))
            self.assertIn(b'fields', response.data, msg=f"\n\nReturned Data  for language '{lang}': {data.keys()}\n{data}")
            self.assertIn(b'web-labels', response.data, msg=f"\n\nReturned Data for language '{lang}': {data.keys()}\n{data}")
            # if lang == "fr":
            #     self.assertNotIn(b'web-labels', response.data, msg=f"\n\nReturned Data for language '{lang}': {data.keys()}\n{data}")
            #     print("------------------",response.data)




if __name__ == '__main__':
    unittest.main()
