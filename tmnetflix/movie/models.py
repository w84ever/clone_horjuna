from django.db import models


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

    def __str__(self) -> str:
        return self.title