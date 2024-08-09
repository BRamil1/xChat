from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from xChannel.models import Message

from config import settings

client = Client()


class XChannelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username=settings.TEST_login, password=settings.TEST_password)
        self.user.save()
        self.message1 = Message.objects.create(user=self.user, text='Hello World!')
        self.message2 = Message.objects.create(user=self.user, text='Hello Ukraine!')
        self.message1.save()
        self.message2.save()

    def test_channel(self):
        self.client.login(username=settings.TEST_login, password=settings.TEST_password)
        response = self.client.get(reverse("xChannel"))
        self.assertEqual(response.status_code, 200)

    def test_my_messages(self):
        self.client.login(username=settings.TEST_login, password=settings.TEST_password)
        response = self.client.get(reverse("my_messages"))
        self.assertEqual(response.status_code, 200)

    def test_create_text(self):
        self.client.login(username=settings.TEST_login, password=settings.TEST_password)
        response = self.client.post(reverse("create"), data={"text": "test"}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_edit_text(self):
        pass

    def test_delete(self):
        self.client.login(username=settings.TEST_login, password=settings.TEST_password)
        response = self.client.post(reverse("delete", args=str(self.message1.id)),
                                    data={"id_msg": self.message1.id}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_all(self):
        self.client.login(username=settings.TEST_login, password=settings.TEST_password)
        response = self.client.post(reverse("delete_all"), follow=True)
        self.assertEqual(response.status_code, 200)
