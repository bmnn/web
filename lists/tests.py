from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import homepage
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.models import Item

POSTED_ITEM = 'A new list item'


class HomePage(TestCase):
   
    @staticmethod
    def post(text):  

        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = text
        return request

    def test_root_resolves_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_homepage_returns_html(self):
        request = HttpRequest()
        response = homepage(request)
        expected = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected)

    def test_homepage_saves_postRequest(self):
        response = homepage(self.post(POSTED_ITEM))

        self.assertEqual(Item.objects.count(), 1)
        first = Item.objects.first()

        self.assertEqual(first.text, POSTED_ITEM)

        # self.assertIn('A new list item', response.content.decode())
        expected = render_to_string('home.html', 
                                    {'new_item_text': POSTED_ITEM
                                     })

    def test_homepage_redirects_postRequest(self):
        response = homepage(self.post(POSTED_ITEM))
        self.assertEqual(response.status_code,
                         302)
        self.assertEqual(response['location'], '/')

    def test_emptyPost(self):
        homepage(HttpRequest())
        self.assertEqual(Item.objects.count(), 0)

    def test_displayItems(self):
        TEMPLATE = "item #%s"
        
        for i in range(2):
            Item.objects.create(text =  TEMPLATE %(i))
        request = HttpRequest()
        response = homepage(HttpRequest())
        for i in range(2):
            self.assertIn(TEMPLATE %(i), response.content.decode())
       
class ItemModel(TestCase):
    def test_savingAndRetrieving(self):
        first = Item()
        first.text = "The first (ever) item"
        first.save()

        second = Item()
        second.text = "Item the second"
        second.save()

        items = Item.objects.all()
        self.assertEqual(items.count(), 2)

        self.assertEqual(items[0].text, first.text)
        self.assertEqual(items[1].text, second.text)



