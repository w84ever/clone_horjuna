from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

CATEGORY_CHOICES = (
    ('A', 'Экшен'),
    ('D', 'Драма'),
    ('C', 'Комедия'),
    ('R', 'Романтика'),
)

LANGUAGE_CHOICES = (
    ('RU', 'RUSSIAN'),
    ('TM', 'TURKMEN'),
)

STATUS_CHOICES = (
    ('RA', 'Недавное'),
    ('MW', 'Популярное'),
    ('TR', 'Лучшее'),
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    poster = models.ImageField(upload_to='image')
    video = models.FileField(upload_to='video')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)

    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(blank=True, null=True)
    
    def save(self ,*args ,**kwargs):
        if not self.slug :
            self.slug = slugify(self.title)
        super(Movie , self).save( *args , **kwargs)

    def __str__(self) -> str:
        return self.title
    

class Banner(models.Model):
    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='image', blank=True)

    def __str__(self) -> str:
        return self.name
    
class MainBanner(models.Model):
    name = models.CharField(max_length=30)
    banner = models.ImageField(upload_to='image')

    def __str__(self) -> str:
        return self.name