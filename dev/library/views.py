from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Author, Category, Langage, Book
from django import template
from django.template.loader import get_template 
from django.template import loader

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


def category(request):
    category_list =  Category.objects.order_by('id')
    langage =  Langage.objects.order_by('id')
    author = Author.objects.order_by('id')
    context = {
        'category_list': category_list,
        'langage': langage,
        'author': author,
    }
    return render(request, 'library/category.html', context)

def list_category(request, category_id):
    category1 = get_object_or_404(Category, pk=category_id)
    list_book = Book.objects.filter(category_id=category_id).values()
    context = {
        'category':category1,
        'list_book': list_book,
    }
    return render(request, 'library/list_category.html', context)

def list_langage(request, language_id):
    langage = get_object_or_404(Langage, pk=language_id)
    list_book = Book.objects.filter(language_id=language_id).values()
    context = {
        'langage':langage,
        'list_book': list_book,
    }
    return render(request, 'library/list_langage.html', context)

def list_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    list_book = Book.objects.filter(author_id=author_id).values()
    context = {
        'author':author,
        'list_book': list_book,
    }
    return render(request, 'library/list_author.html', context)


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
