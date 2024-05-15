from django.db import models
from django.core.validators import MaxValueValidator


class Film(models.Model):
    title = models.CharField(max_length=50)
    rating = models.FloatField(default=0, validators=[MaxValueValidator(10)])
    duration = models.DurationField()
    director = models.ForeignKey(to='actors.Director', on_delete=models.CASCADE)
    actors = models.ManyToManyField(to='actors.Actor', blank=True)

    def __str__(self):
        return f'{self.title} - {self.rating}/10⭐'
