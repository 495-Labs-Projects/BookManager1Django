from django.test import TestCase

from books.models import *
from books.tests.utilities import *

class AuthorTest(TestCase):

    factories = Populate()

    def setUp(self):
        self.factories.populate_authors()

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

    def test_alphabetical(self):
        self.assertQuerysetEqual(Publisher.objects.alphabetical(), 
            [repr(self.factories.p1), repr(self.factories.p2), repr(self.factories.p3)])


# class BookTest(TestCase):

#     def setUp(self):
#         populate_publishers()

#     def test_alphabetical(self):
#         self.assertQuerysetEqual(Publisher.objects.alphabetical(), 
#             ["<Publisher: Pearson>", "<Publisher: Random House>", "<Publisher: Scholastic>"])

