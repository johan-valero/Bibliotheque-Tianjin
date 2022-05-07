from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/detail/', views.detail, name='detail'),
    path('liste/', views.liste, name='liste'),
]