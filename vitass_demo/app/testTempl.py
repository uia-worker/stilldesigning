# app/testTempl.py

from django.test import TestCase
# from app.models import SomeModel


class SomeTestCase(TestCase):
    def testSome(self):
        post = "My post"
        self.assertEqual(post, "My post")
