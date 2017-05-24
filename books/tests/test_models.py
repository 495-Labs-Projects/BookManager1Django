from django.test import TestCase

from books.models import *

class AuthorTest(TestCase):

    def test_author_name(self):
        a = Author(first_name="Bob", last_name="Smith")
        self.assertEqual("Bob Smith", str(a))
