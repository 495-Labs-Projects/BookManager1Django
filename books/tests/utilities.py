from books.tests.factories import *


def populate_authors():
    AuthorFactory.create()
    AuthorFactory.create(first_name="Bob", last_name="Smith")
    AuthorFactory.create(first_name="Rick", last_name="Huang")
    AuthorFactory.create(first_name="Ernest", last_name="Hemingway")

