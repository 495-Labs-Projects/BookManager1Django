from django.test import TestCase, RequestFactory
from django.urls import reverse

from books.models import *
from books.forms import *
from books.views import *
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

    def test_new_book_view(self):
        response = self.client.get(reverse('books:book_new'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], BookForm)
        self.assertContains(response, "Create Book")

    def test_create_book_view(self):
        num_books = Book.objects.count()
        response = self.client.post(reverse('books:book_new'),
            {'title': 'Test Title', 'year_published': 2017, 'publisher': self.factories.p1.id, 'authors': [self.factories.a1.id]}) 
        self.assertEqual(Book.objects.count(), num_books + 1)
        self.assertRedirects(response, reverse('books:book_detail', args=(num_books+1,)))

    def test_create_bad_book_view(self):
        num_books = Book.objects.count()
        response = self.client.post(reverse('books:book_new'),
            {'title': 'Test Title', 'year_published': 2019, 'publisher': self.factories.p1.id}) 
        self.assertEqual(Book.objects.count(), num_books)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], BookForm)

    def test_edit_book_view(self):
        response = self.client.get(reverse('books:book_edit', args=(self.factories.b1.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], BookForm)
        self.assertContains(response, "Update Book")

    def test_update_book_view(self):
        response = self.client.post(reverse('books:book_edit', args=(self.factories.b1.id,)),
            {'title': 'Test Story', 'year_published': 2017, 'publisher': self.factories.p1.id, 'authors': [self.factories.a1.id]})
        self.factories.b1.refresh_from_db()
        self.assertEqual(self.factories.b1.title, 'Test Story')
        self.assertRedirects(response, reverse('books:book_detail', args=(self.factories.b1.id,)))

    def test_update_bad_book_view(self):
        response = self.client.post(reverse('books:book_edit', args=(self.factories.b1.id,)),
            {'title': 'Test Story', 'year_published': 2019, 'publisher': self.factories.p1.id})
        self.factories.b1.refresh_from_db()
        self.assertEqual(self.factories.b1.title, 'Cool Story')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], BookForm)

    def test_delete_book_view(self):
        num_books = Book.objects.count()
        response = self.client.post(reverse('books:book_delete', args=(self.factories.b1.id,)))
        self.assertEqual(Book.objects.count(), num_books - 1)
        self.assertRedirects(response, reverse('books:book_list'))




        # num_publishers = Publisher.objects.count()
        # response = self.client.post(reverse('books:publisher_new'), 
        #     {'name': 'Test Pub'})
        # self.assertEqual(Publisher.objects.count(), num_publishers + 1)
        # self.assertRedirects(response, reverse('books:publisher_detail', args=(4,)))

