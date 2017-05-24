import factory
from books.models import *


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = "John"
    last_name = "Smith"


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher

    name = "Pearson"

# class BookFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Book


#     title = "Cool Story"
#     year_published = 2015

#     publisher = factory.RelatedFactory(PublisherFactory, 'book')

#     @factory.post_generation
#     def authors(self, create, extracted, **kwargs):
#         if not create:
#             return
#         if extracted:
#             for author in extracted:
#                 self.authors.add(author)
