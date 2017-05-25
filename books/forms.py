from django import forms
from books.models import *

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ["title", "year_published", "publisher", "authors"] 
        widgets = {
            'authors': forms.CheckboxSelectMultiple,
        }