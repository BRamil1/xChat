from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from config import settings

client = Client()


class MainTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username=settings.TEST_login, password=settings.TEST_password)
        self.user.save()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
