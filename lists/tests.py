from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import homepage

class HomePage(TestCase):
    def test_root_resolves_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

