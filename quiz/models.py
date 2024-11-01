from django.db import models


# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Question(models.Model):
    name = models.CharField(max_length=255)
    options = models.CharField(max_length=255)
    correct_option = models.IntegerField()
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    points = models.CharField(max_length=255)
