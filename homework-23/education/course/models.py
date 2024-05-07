from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Topic(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} topic'
