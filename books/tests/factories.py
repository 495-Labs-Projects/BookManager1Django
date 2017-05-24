import factory
from books.models import *


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = "John"
    last_name = "Smith"