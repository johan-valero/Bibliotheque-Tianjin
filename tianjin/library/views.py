from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Author, Category, Langage, Book
from django import template
from django.template.loader import get_template 
from django.template import loader
# from django.contrib.auth.models import User

# Create your views here.
def index(request):
    last_book = Book.objects.order_by('id')
    category =  Category.objects.all()
    langage =  Langage.objects.all()
    author = Author.objects.all()
    context = {
        'list_book': last_book,
        'category': category,
        'langage': langage,
        'author': author,
    }
    return render(request, 'library/index.html', context)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {
        'book': book
    }
    return render(request, 'library/detail.html', context)

def liste(request):
    book = Book.objects.order_by('id')
    category =  Category.objects.all()
    langage =  Langage.objects.all()
    author = Author.objects.all()
    context = {
        'book': book,
        'category': category,
        'langage': langage,
        'author': author,
    }
    return render(request, 'library/liste.html', context)   


def resultat(request):
    context = {}
    if request.method == "POST":
        search_input = request.POST['search_input'].lower()
        books = Book.objects.filter(name_book__contains=search_input)

        books_date = Book.objects.filter(date_book__contains=search_input)

        books_author = Book.objects.filter(author__name_author__contains=search_input)

        books_firstname = Book.objects.filter(author__firstname_author__contains=search_input)

        books_language = Book.objects.filter(language__name_langage__contains=search_input)

        books_category = Book.objects.filter(category__name_category__contains=search_input)

        context = {
            'search_input': search_input,
            'books' :books,
            'books_firstname': books_firstname,
            'books_date': books_date,
            'books_author': books_author,
            'books_language': books_language,
            'books_category': books_category,
        }

        return render(request, 'library/resultat.html', context)
    else:
        return render(request, 'library/resultat.html', context)
