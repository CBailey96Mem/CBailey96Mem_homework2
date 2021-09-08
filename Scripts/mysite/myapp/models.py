from django.db import models

# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length=45)
    numb = models.IntegerField(default=1337)

class MyOtherModel(models.Model):
    otherName = models.CharField(max_length=45)
    numb = models.ForeignKey(MyModel, default=1337, on_delete=models.SET_DEFAULT)