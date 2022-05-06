from django.db import models
import datetime
# from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name_author = models.CharField(max_length=50)
    firstname_author = models.CharField(max_length=50)
    birthdate_author = models.DateField("Date de naissance du l'auteur")
    picture_author = models.ImageField(upload_to="pictures_author", blank=True)

    def __str__(self):
        affiche = f"{self.firstname_author} {self.name_author}"
        return affiche

class Category(models.Model):
    name_category = models.CharField(max_length=100)

    def __str__(self):
        affiche = f"{self.name_category}"
        return affiche

class Langage(models.Model):
    name_langage = models.CharField(max_length=50)

    def __str__(self):
        affiche = f"{self.name_langage}"
        return affiche

class Book(models.Model):
    name_book = models.CharField(max_length=50)
    date_book = models.DateField("Date de publication")
    synopsis_book = models.TextField(null=True, blank=True)
    picture_book = models.ImageField(upload_to="pictures_book", blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    language = models.ForeignKey(Langage, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        affiche = f"{self.name_book}"
        return affiche