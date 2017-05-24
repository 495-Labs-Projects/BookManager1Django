from books.tests.factories import *

class Populate():

    def populate_authors(self):
        self.a1 = AuthorFactory.create()
        self.a2 = AuthorFactory.create(first_name="Bob", last_name="Smith")
        self.a3 = AuthorFactory.create(first_name="Rick", last_name="Huang")
        self.a4 = AuthorFactory.create(first_name="Ernest", last_name="Hemingway")

    def populate_publishers(self):
        self.p1 = PublisherFactory.create()
        self.p2 = PublisherFactory.create(name="Random House")
        self.p3 = PublisherFactory.create(name="Scholastic")
