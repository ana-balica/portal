from django.test import TestCase
from django.contrib.auth.models import User


class TestTestCase(TestCase):
    def test_case(self):
        self.assertEqual(1, 1)