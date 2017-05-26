from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from books.models import *
from books.forms import *

# Books CRUD operations

class BookList(ListView):
    model = Book()

    def get_queryset(self):
        return Book.objects.alphabetical()

class BookDetail(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    form_class = BookForm

    def get_success_url(self):
        return reverse('books:book_detail', args=(self.object.id,))

class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    
    def get_success_url(self):
        return reverse('books:book_detail', args=(self.object.id,))

class BookDelete(DeleteView):
    model = Book
    
    def get_success_url(self):
        return reverse('books:book_list')


# Author CRUD operations

class AuthorList(ListView):
    model = Author
    template_name = 'authors/author_list.html'

    def get_queryset(self):
        return Author.objects.alphabetical()

class AuthorDetail(DetailView):
    model = Author
    template_name = 'authors/author_detail.html'

class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/author_form.html'

    def get_success_url(self):
        return reverse('books:author_detail', args=(self.object.id,))

class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/author_form.html'
    
    def get_success_url(self):
        return reverse('books:author_detail', args=(self.object.id,))

class AuthorDelete(DeleteView):
    model = Author
    template_name = 'authors/author_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('books:author_list')


# Publisher CRUD operations

class PublisherList(View):

    def get(self, request):
        template = 'publishers/publisher_list.html'
        context = {
            'publishers': Publisher.objects.alphabetical()
        }
        return render(request, template, context)

class PublisherDetail(DetailView):
    model = Publisher
    template_name = 'publishers/publisher_detail.html'

class PublisherCreate(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publishers/publisher_form.html'

    def get_success_url(self):
        return reverse('books:publisher_detail', args=(self.object.id,))

class PublisherUpdate(UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publishers/publisher_form.html'
    
    def get_success_url(self):
        return reverse('books:publisher_detail', args=(self.object.id,))

class PublisherDelete(DeleteView):
    model = Publisher
    template_name = 'publishers/publisher_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('books:publisher_list')

