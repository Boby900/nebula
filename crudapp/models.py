from django.db import models

# Create your models here.
class Book(models.Model):
    oid = models.IntegerField(primary_key=True)
    title= models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    author= models.ForeignKey("self", on_delete = models.CASCADE)
    publishedDate = models.DateField()
    