from django.test import TestCase

class SmokeTest(TestCase):
    def test_bad_maths(self):
        self._baseAssertEqual(1+1, 3)

