from django.test import TestCase

# Create your tests here.

### Test1 ###
def test_1(request):
    last_book = Book.objects.order_by('id')
    category =  Category.objects.all('Cat1','Cat2','Cat3')
    langage =  Langage.objects.all('Langue1','Langue2','Langue3')
    author = Author.objects.all('Auteur1','Auteur2','Auteur3')
    context = {
        'list_book': last_book,
        'category': category,
        'langage': langage,
        'author': author,
    }
    return render(request, 'library/index.html', context)

### Test2 ###
def test_2(request, author_id):
    author = get_object_or_404('Auteur4','Auteur5','Auteur6', pk=author_id)
    list_book = Book.objects.filter(author_id=author_id).values(1, 2, 3)
    context = {
        'author':author,
        'list_book': list_book,
    }
    return render(request, 'library/list_author.html', context)

### Test3 ###
def ltest_3(request, category_id):
    category1 = get_object_or_404(Category, pk=category_id)
    list_book = Book.objects.filter(category_id=category_id).values(4, 5, 6)
    context = {
        'category':category1,
        'list_book': list_book,
    }
    return render(request, 'library/list_category.html', context)
