from datetime import date
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthday = models.DateField()

class Publisher(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='publisher_images', blank=True, null=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    edition = models.IntegerField(default=1)
    author = models.ForeignKey(Author)
    BOOK_TYPE = (
        ('printed', 'Printed'),
        ('ebook', 'eBook'),
        ('pdf', 'pdf'),
    )
    type = models.CharField(max_length=1, choices=BOOK_TYPE)
    SUBJECT = (
        ('quran', 'Kuran'),
        ('translation', 'Meal'),
        ('tafsier', 'Tefsir'),
        ('aqeedah', 'Akaid'),
        ('fiqh', 'Fikih'),
        ('siyyer', 'Siyer'),
        ('tassawuf', 'Tassavuf'),
        ('other', 'Other'),
    )
    subject = models.CharField(max_length=1, choices=SUBJECT)
    read = models.BooleanField(default=False)
    publisher = models.ForeignKey(Publisher)
    published = models.DateField(default=lambda: date.today())

