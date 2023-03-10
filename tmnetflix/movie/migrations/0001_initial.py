# Generated by Django 4.1.7 on 2023-02-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('poster', models.ImageField(upload_to='movie/image')),
                ('video', models.FileField(upload_to='movie/video')),
                ('category', models.CharField(choices=[('A', 'Экшен'), ('D', 'Драма'), ('C', 'Комедия'), ('R', 'Романтика')], max_length=1)),
                ('language', models.CharField(choices=[('RU', 'RUSSIAN'), ('TM', 'TURKMEN')], max_length=2)),
                ('status', models.CharField(choices=[('RA', 'Недавное'), ('MW', 'Популярное'), ('TR', 'Лучшее')], max_length=2)),
                ('year_of_production', models.DateField()),
                ('views_count', models.IntegerField(default=0)),
            ],
        ),
    ]
