from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Author, Category, Langage, Book
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

def detail(request):
    detail = get_object_or_404(Book, pk=publication_id)
    context = {'detail': detail}
    return render(request, 'library/detail.html', context)