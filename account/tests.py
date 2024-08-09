from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from config import settings

client = Client()


class AccountTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username=settings.TEST_login, password=settings.TEST_password)
        self.user.save()

    def test_signup_func(self):
        response = client.post(reverse('signup_user'),
                               {"username": settings.TEST_login + "_signup",
                                "password1": settings.TEST_password,
                                "password2": settings.TEST_password})
        self.assertEqual(response.status_code, 200)

    def test_login_func(self):
        response = client.post(reverse('login_user'),
                               {"username": settings.TEST_login + "_signup",
                                "password": settings.TEST_password})
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_account_settings(self):
        self.client.login(username=settings.TEST_login, password=settings.TEST_password)
        response = self.client.get(reverse("account"))
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_logout_func(self):
        self.client.login(username=settings.TEST_login, password=settings.TEST_password)
        response = self.client.post(reverse("logout_user"), user=self.user, follow=True)
        self.assertEqual(response.status_code, 200)
