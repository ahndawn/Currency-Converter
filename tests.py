from app import app
from unittest import TestCase


class ConversionTestCase(TestCase):
   def test_base(self):
        with app.test_client() as client:
        # can now make requests to flask via `client`
            resp = client.get('/')
            self.assertEqual(resp.status_code, 200)

class SessionTest(TestCase):
    def test_session_info_set(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['count'] = 999

            # Now those changes will be in Flask's `session`
            resp = client.get("/")

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(session['count'], 1000)