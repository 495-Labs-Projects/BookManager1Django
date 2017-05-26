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


class AuthorViewTests(FactoryTestCase):

    def setUp(self):
        self.factories.populate_books()

    def test_list_view_with_no_authors(self):
        Author.objects.all().delete()

        response = self.client.get(reverse('books:author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No authors are available.")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_list_view_with_authors(self):
        response = self.client.get(reverse('books:author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['object_list']), 
            [repr(self.factories.a4), repr(self.factories.a3), repr(self.factories.a2), repr(self.factories.a1)])

    def test_new_author_view(self):
        response = self.client.get(reverse('books:author_new'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], AuthorForm)
        self.assertContains(response, "Create Author")

    def test_create_author_view(self):
        num_authors = Author.objects.count()
        response = self.client.post(reverse('books:author_new'),
            {'first_name': 'Test', 'last_name': 'Author'}) 
        self.assertEqual(Author.objects.count(), num_authors + 1)
        self.assertRedirects(response, reverse('books:author_detail', args=(num_authors+1,)))

    def test_create_bad_author_view(self):
        num_authors = Author.objects.count()
        response = self.client.post(reverse('books:author_new'),
            {'first_name': '', 'last_name': 'Author'}) 
        self.assertEqual(Author.objects.count(), num_authors)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], AuthorForm)

    def test_edit_author_view(self):
        response = self.client.get(reverse('books:author_edit', args=(self.factories.a1.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], AuthorForm)
        self.assertContains(response, "Update Author")

    def test_update_author_view(self):
        response = self.client.post(reverse('books:author_edit', args=(self.factories.a1.id,)),
            {'first_name': 'Test', 'last_name': 'Author'})
        self.factories.a1.refresh_from_db()
        self.assertEqual(self.factories.a1.first_name, 'Test')
        self.assertRedirects(response, reverse('books:author_detail', args=(self.factories.a1.id,)))

    def test_update_bad_author_view(self):
        response = self.client.post(reverse('books:author_edit', args=(self.factories.a1.id,)),
            {'first_name': '', 'last_name': 'Author'})
        self.factories.a1.refresh_from_db()
        self.assertEqual(self.factories.a1.first_name, 'John')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], AuthorForm)

    def test_delete_book_view(self):
        num_authors = Author.objects.count()
        response = self.client.post(reverse('books:author_delete', args=(self.factories.a3.id,)))
        self.assertEqual(Author.objects.count(), num_authors - 1)
        self.assertRedirects(response, reverse('books:author_list'))


class PublisherViewTests(FactoryTestCase):

    def setUp(self):
        self.factories.populate_books()

    def test_list_view_with_no_publishers(self):
        Publisher.objects.all().delete()

        response = self.client.get(reverse('books:publisher_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No publishers are available.")
        self.assertQuerysetEqual(response.context['publishers'], [])

    def test_list_view_with_publishers(self):
        response = self.client.get(reverse('books:publisher_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['publishers']), 
            [repr(self.factories.p1), repr(self.factories.p2), repr(self.factories.p3)])

    def test_new_publisher_view(self):
        response = self.client.get(reverse('books:publisher_new'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], PublisherForm)
        self.assertContains(response, "Create Publisher")

    def test_create_publisher_view(self):
        num_publishers = Publisher.objects.count()
        response = self.client.post(reverse('books:publisher_new'),
            {'name': 'Test Publisher'}) 
        self.assertEqual(Publisher.objects.count(), num_publishers + 1)
        self.assertRedirects(response, reverse('books:publisher_detail', args=(num_publishers+1,)))

    def test_create_bad_publisher_view(self):
        num_publishers = Publisher.objects.count()
        response = self.client.post(reverse('books:publisher_new'),
            {'name': ''}) 
        self.assertEqual(Publisher.objects.count(), num_publishers)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], PublisherForm)

    def test_edit_publisher_view(self):
        response = self.client.get(reverse('books:publisher_edit', args=(self.factories.p1.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], PublisherForm)
        self.assertContains(response, "Update Publisher")

    def test_update_publisher_view(self):
        response = self.client.post(reverse('books:publisher_edit', args=(self.factories.p1.id,)),
            {'name': 'Test Publisher'})
        self.factories.p1.refresh_from_db()
        self.assertEqual(self.factories.p1.name, 'Test Publisher')
        self.assertRedirects(response, reverse('books:publisher_detail', args=(self.factories.p1.id,)))

    def test_update_bad_publisher_view(self):
        response = self.client.post(reverse('books:publisher_edit', args=(self.factories.p1.id,)),
            {'name': ''})
        self.factories.p1.refresh_from_db()
        self.assertEqual(self.factories.p1.name, 'Pearson')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], PublisherForm)

    def test_delete_book_view(self):
        num_publishers = Publisher.objects.count()
        response = self.client.post(reverse('books:publisher_delete', args=(self.factories.p1.id,)))
        self.assertEqual(Publisher.objects.count(), num_publishers - 1)
        self.assertRedirects(response, reverse('books:publisher_list'))

