from books.tests.factories import *
from django.utils import timezone

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

    def populate_books(self):
        self.populate_authors()
        self.populate_publishers()

        self.b1 = BookFactory(publisher=self.p1, authors=[self.a1, self.a2])
        self.b2 = BookFactory(title="Rick's Story", year_published=timezone.now().year-5, publisher=self.p2, authors=[self.a3])
        self.b3 = BookFactory(title="A Farewell to Arms", year_published=1929, publisher=self.p3, authors=[self.a4])
