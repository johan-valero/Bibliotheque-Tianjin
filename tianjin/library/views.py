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
    context = {'book': book}
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

    if request.method == 'POST': 
        searchInput = request.POST["searchInput"]
        searchInput.lower()

        b = Book.objects.all()
        c =  Category.objects.all()
        l =  Langage.objects.all()
        a = Author.objects.all()

        book = []
        category = []
        langage = []
        author = []

        for item in b:
            info = item.readLines().lower()
            if info.find(searchInput) != -1:
                book.append(item)

        for item in c:
            info = item.readLines().lower()
            if info.find(searchInput) != -1:
                category.append(item)

        for item in l:
            info = item.readLines().lower()
            if info.find(searchInput) != -1:
                langage.append(item)

        for item in a:
            info = item.readLines().lower()
            if info.find(searchInput) != -1:
                author.append(item)

        template = loader.get_template('library/resultat.html')
        context = {
            'book': book,
            'category': category,
            'langage': langage,
            'author': author,
            }

        return HttpResponse(template.render(context, request))
    else:
        return render(request, 'library/resultat.html')