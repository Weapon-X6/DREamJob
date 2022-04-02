from django.db import models
from enum import Enum


# 1. April 2022
class Country(Enum):
    GERMANY = 1
    US = 2
    FINLAND = 3
    SWEDEN = 4
    UK = 5


class Company(models.Model):
    name = models.CharField(max_length=33)
    country = Country
    funding = models.FloatField


class Application(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE())
    salary_from = models.DecimalField
    salary_to = models.DecimalField



