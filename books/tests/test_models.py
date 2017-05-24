from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone

from books.models import *
from books.tests.utilities import *

class AuthorTest(TestCase):

    factories = Populate()

    def setUp(self):
        self.factories.populate_authors()

    def test_validations(self):
        bad_author = AuthorFactory.create(first_name="")
        self.assertRaises(ValidationError, bad_author.full_clean)

    def test_author_name(self):
        a = Author.objects.get(first_name="John")
        self.assertEqual("John Smith", str(a))

    def test_alphabetical(self):
        self.assertQuerysetEqual(Author.objects.alphabetical(), 
            ["<Author: Ernest Hemingway>", "<Author: Rick Huang>", "<Author: Bob Smith>", "<Author: John Smith>"])


class PublisherTest(TestCase):

    factories = Populate()

    def setUp(self):
        self.factories.populate_publishers()

    def test_validations(self):
        bad_publisher = PublisherFactory.create(name="")
        self.assertRaises(ValidationError, bad_publisher.full_clean)

    def test_alphabetical(self):
        self.assertQuerysetEqual(Publisher.objects.alphabetical(), 
            [repr(self.factories.p1), repr(self.factories.p2), repr(self.factories.p3)])


class BookTest(TestCase):

    factories = Populate()

    def setUp(self):
        self.factories.populate_books()

    def test_validations(self):
        bad_book = BookFactory.build(title="", publisher=self.factories.p1, authors=[self.factories.a1])
        self.assertRaises(ValidationError, bad_book.full_clean)

        bad_book = BookFactory.build(year_published=timezone.now().year + 2, publisher=self.factories.p1, authors=[self.factories.a1])
        self.assertRaises(ValidationError, bad_book.full_clean)


    def test_alphabetical(self):
        self.assertQuerysetEqual(Book.objects.alphabetical(), 
            [repr(self.factories.b3), repr(self.factories.b1), repr(self.factories.b2)])

    def test_last_decade(self):
        self.assertQuerysetEqual(Book.objects.last_decade().alphabetical(), 
            [repr(self.factories.b1), repr(self.factories.b2)])

