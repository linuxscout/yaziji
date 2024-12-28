import unittest

import sys, os
import json
# Local libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from yaziji_webserver import app  # Import your Flask app instance


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client for the Flask app."""
        self.app = app.test_client()
        self.app.testing = True
        self.languages = "ar,bn,de,en,es,fr,id,ja,ku,zh,he".split(',')

    # @unittest.skip("Test later")
    def test_home_page(self):
        """Test the home page."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'index.html', response.data)


    def test_index_page(self):
        """Test the /index/ route."""
        response = self.app.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'index.html', response.data)

    # @unittest.skip("Test later")
    def test_ajax_get_random_text(self):
        """Test the AJAX get_random_text action."""
        response = self.app.post('/ajaxGet', json={"data": {"action": "randomtext"}})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"RANDOM TEXT TEST", response.data, msg=f"Returned Data \n{response.data}")

    # @unittest.skip("Test later")
    def test_ajax_report(self):
        """Test the AJAX report action."""
        response = self.app.post('/ajaxGet', json={"data": {"text":"Taha","action": "report", "subject":"Taha"}})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'REPORT:', response.data, msg=f"Returned Data \n{response.data}")
        # empty return
        self.assertNotIn(b'{}', response.data, msg=f"Empty returned Data \n{response.data}")

    # @unittest.skip("Test later")
    def test_ajax_rating(self):
        """Test the AJAX rating action."""
        response = self.app.post('/ajaxGet',
                                 json={"data": {"text":"4", "action": "rating","rating":"4",
                    "subject": "هما مؤ", "object": ""}})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'RATING:', response.data)
        self.assertIn(b"'rating': '4'", response.data, msg=f"Returned Data \n{response.data}")

    # @unittest.skip("Test later")
    def test_ajax_action_sample(self):
        """Test AJAX action sample processing."""
        response = self.app.post(
            '/ajaxGet',
            json={"data": {"text": "", "action": "sample",
                           # options for samples
                           'subject': 'معَلِّمٌ', 'object': '', 'verb': 'رَسَبَ', 'time': 'بَعْدَ غَدٍ',
                           'place': 'مَدِينَةٌ', 'tense': 'الماضي المعلوم', 'voice': 'مبني للمجهول',
                           'auxiliary': 'اِسْتَطَاعَ', 'negative': 'مثبت', 'phrase_type': 'جملة فعلية',
                           }}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"'phrase':", response.data, msg=f"Returned Data \n{response.data}")
        self.assertIn(b"'inflection':", response.data, msg=f"Returned Data \n{response.data}")


    # @unittest.skip("Test later")
    def test_ajax_action_phrase(self):
        """Test AJAX action processing."""

        response = self.app.post(
            '/ajaxGet',
            json={"data": {"text": "", "action": "phrase",
                           # options for samples
                           'subject': 'معَلِّمٌ', 'object': '', 'verb': 'رَسَبَ', 'time': 'بَعْدَ غَدٍ',
                           'place': 'مَدِينَةٌ', 'tense': 'الماضي المعلوم', 'voice': 'مبني للمجهول',
                           'auxiliary': 'اِسْتَطَاعَ', 'negative': 'مثبت', 'phrase_type': 'جملة فعلية',
                           }}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'phrase', response.data, msg=f"Returned Data \n{response.data}")
        self.assertIn(b'inflection', response.data, msg=f"Returned Data \n{response.data}")

    # @unittest.skip("Test later")
    def test_ajax_action(self):
        """Test AJAX action processing."""
        response = self.app.post(
            '/ajaxGet',
            json={"data": {"text": "TEST", "action": "TEST", "param": ""}}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"TEST"', response.data, msg=f"Returned Data \n{response.data}")



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
            # self.assertNotIn(b'web-labels', response.data, msg=f"\n\nReturned Data for language '{lang}': {data.keys()}\n{data}")
            print(response.data)
    @unittest.skip("Test later")
    def test_404_error(self):
        """Test a 404 error page."""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'404.html', response.data)


if __name__ == '__main__':
    unittest.main()
