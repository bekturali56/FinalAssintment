from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=50)
    price=models.IntegerField(help_text="Enter Price")