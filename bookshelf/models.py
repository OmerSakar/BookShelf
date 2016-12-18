from django.db import models
from django.core import validators
from datetime import date
from enum import Enum

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthday = models.DateField(null=True, blank=True)

class Publisher(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='files/publisher_images', blank=True, null=True)

class Subject(Enum):
    QURAN, TRANSLATION, TAFSIER, AQEEDAH, FIQH, SIYYER, TASSAWUF, OTHER = range(8)

class BookType(Enum):
    PRINTED, EBOOK, PDF = range(3)

class Book(models.Model):
    title = models.CharField(max_length=100)
    edition = models.IntegerField(null=True, blank=True)
    authors = models.ManyToManyField(Author)
    book_types = models.CharField(BookType, max_length=1, validators=[validators.validate_comma_separated_integer_list], blank=True, null=True)
    file = models.FileField(upload_to='files/books' ,null=True, blank=True)
    subjects = models.CharField(Subject, max_length=1, validators=[validators.validate_comma_separated_integer_list], blank=True, null=True)
    read = models.BooleanField(default=False)
    publisher = models.ForeignKey(Publisher, null=True, blank=True)
    published = models.DateField(default=date.today)

    def __str__(self):
        return self.title



