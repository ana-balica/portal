from django.test import TestCase


class TestTestCase(TestCase):
    def test_case(self):
        self.assertEqual(1, 1)
