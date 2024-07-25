from django.test import TestCase, Client

client = Client()


class AccountTest(TestCase):
    def test_login(self):
        response = client.post('/account/login', {"username": "admin", "password": "admin"})
        self.assertEqual(response.status_code, 200)
