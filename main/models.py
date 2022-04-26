from django.db import models
from django.db.models import Model
from ckeditor.fields import RichTextField
# Create your models here.


class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    branch = RichTextField(null=True, blank=True)


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default=" ", null=True, blank=True)
    subTitle = models.CharField(max_length=70, default=" ", null=True, blank=True)
    price = models.IntegerField(default=" ", null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default=" ", null=True, blank=True)
    date = models.DateField(default=" ", null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    description = RichTextField(null=True, blank=True)


class Home(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default=" ", null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)


class About(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default=" ", null=True, blank=True)
    name = models.CharField(max_length=60, default=" ", null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)