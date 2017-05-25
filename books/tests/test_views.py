from django.test import TestCase
from django.urls import reverse

from books.models import *
from books.tests.test_models import FactoryTestCase

class BookViewTests(FactoryTestCase):

    def setUp(self):
        self.factories.populate_books()

    def test_list_view_with_no_books(self):
        Book.objects.all().delete()

        response = self.client.get(reverse('books:book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No books are available.")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_list_view_with_books(self):
        response = self.client.get(reverse('books:book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['object_list']), 
            [repr(self.factories.b3), repr(self.factories.b1), repr(self.factories.b2)])
