from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


# Custom Validators

def validate_past_year(year):
    if year > timezone.now().year:
        raise ValidationError(
            _('%(value)s is in the future'),
            params={'value': year},
        )


# Models

class Author(models.Model):
    # Author fields
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # Scopes/Manager
    class QuerySet(models.QuerySet):
        def alphabetical(self):
            return self.order_by("last_name", "first_name")

    objects = QuerySet.as_manager()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Publisher(models.Model):
    # Publisher fields
    name = models.CharField(max_length=255)

    # Scopes/Manager
    class QuerySet(models.QuerySet):
        def alphabetical(self):
            return self.order_by("name")

    objects = QuerySet.as_manager()

    def __str__(self):
        return self.name


class Book(models.Model):
    # Book fields
    title = models.CharField(max_length=255)
    year_published = models.IntegerField(default=timezone.now().year, validators=[validate_past_year])
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    # Scopes/Manager
    class QuerySet(models.QuerySet):
        def alphabetical(self):
            return self.order_by("title")

        def last_decade(self):
            decade_ago = timezone.now().year - 10
            return self.filter(year_published__gt=decade_ago)

    objects = QuerySet.as_manager()

    def __str__(self):
        return self.title


