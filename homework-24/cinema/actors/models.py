from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    films = models.ManyToManyField(to='movie.Film', blank=True)

    def __str__(self):
        return f'Actor #{self.pk}: {self.name} {self.surname}'


class Director(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'Director #{self.pk}: {self.name} {self.surname}'
