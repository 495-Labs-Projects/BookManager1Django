from django.test import TestCase

from books.models import *
from books.tests.utilities import *

class AuthorTest(TestCase):

    def setUp(self):
        populate_authors()

    def test_author_name(self):
        a = Author.objects.get(first_name="John")
        self.assertEqual("John Smith", str(a))

    def test_alphabetical(self):
        self.assertQuerysetEqual(Author.objects.alphabetical(), 
            ["<Author: Ernest Hemingway>", "<Author: Rick Huang>", "<Author: Bob Smith>", "<Author: John Smith>"])
