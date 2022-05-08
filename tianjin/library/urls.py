from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/detail/', views.detail, name='detail'),
    path('liste/', views.liste, name='liste'),
    path('resultat/', views.resultat, name='resultat'),
    path('category/', views.category, name='category'),
    path('<int:category_id>/list_category/', views.list_category, name='list_category'),
]