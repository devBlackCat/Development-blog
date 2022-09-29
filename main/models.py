from enum import unique
from itertools import count
from django.db import models

# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Question(models.Model):
    number = models.IntegerField(unique=True)
    contact = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.number}.{self.contact}'

class Choice(models.Model):
    contact = models.CharField(max_length=100)
    question = models.ForeignKey(to='main.Question', on_delete=models.CASCADE)
    question = models.ForeignKey(to='main.Developer', on_delete=models.CASCADE,null=True)
    def __str__(self):
         return self.contact