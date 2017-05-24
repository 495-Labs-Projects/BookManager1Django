import factory
from books.models import *


class AuthorFactory(factory.Factory):
    class Meta:
        model = models.AuthorFactory

    first_name = "John"
    last_name = "Smith"
