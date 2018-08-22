from django.db import models

# Create your models here.
class Result(models.Model):
    gender = models.BooleanField()
    grade = models.CharField(max_length=64)
    alimony = models.IntegerField()
    sourceOfExpense = models.CharField(max_length=64)
    costType = models.CharField(max_length=64)
    costTypeCount = models.CharField(max_length=128)
    record = models.CharField(max_length=64)
    plan = models.CharField(max_length=64)
    demand = models.CharField(max_length=64)
    measure = models.CharField(max_length=64)
