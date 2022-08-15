from django.db import models
from django.contrib import admin


# Create your models here.

class Sudoku(models.Model):
    question = models.CharField(max_length=100)
    solution = models.CharField(max_length=100)

    # def __str__(self):
        # return self.id


class User(models.Model):
    username = models.CharField(max_length=40, null=False)
    bestScore = models.IntegerField()
    bestTime = models.CharField(max_length=10, null=True)
    solvedQuestion = models.IntegerField()

    def __str__(self):
        return self.username

admin.site.register(Sudoku)
admin.site.register(User)

