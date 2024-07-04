from django.db import models

class book(models.Model):
    Titlename = models.CharField(max_length=50)
    Authorname = models.CharField(max_length=50)
    Genre = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Publisheddate = models.DateField()
    Rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
