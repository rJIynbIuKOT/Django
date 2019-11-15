from django.db import models

class Publisher(models.Model):
    name = models.CharField('Имя издателя', max_length=100)

    def order(self):
        return self.books.order_by('name')

    def __str__(self):
        return '{}'.format(self.name)

class Author(models.Model):
    SEX = [
        ('Мужской', 'М'),
        ('Женский', 'Ж')
    ]
    name = models.CharField('Имя автора', max_length=100)
    year_of_birthday = models.IntegerField('Год рождения')
    gender = models.CharField('Пол', max_length=100, choices=SEX)

    def order(self):
        return self.books.order_by('name')

    def __str__(self):
        return '{} ({}г. р.)'.format(self.name, self.year_of_birthday)

class Book(models.Model):
    author = models.ForeignKey('books.Author', models.CASCADE, related_name='books')
    publisher = models.ForeignKey('books.Publisher', models.CASCADE, related_name='books')
    name = models.CharField('Название', max_length=100)
    year = models.IntegerField('Год написания')
    genre = models.CharField('Жанр', max_length=100)
    description = models.TextField('Краткое описание')
    image = models.ImageField(upload_to = 'books/images', null=True, blank=True)

    def __str__(self):
        return '{} - {} ({}, {}г)'.format(self.name, self.author.name, self.publisher.name, self.year)