from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from books.models import Book
from books.forms import BookForm

class BookList(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    form_class = BookForm

    def get_success_url(self):
        return reverse('books:book_list')

class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    
    def get_success_url(self):
        return reverse('books:book_list')

class BookDelete(DeleteView):
    model = Book
    
    def get_success_url(self):
        return reverse('books:book_list')
