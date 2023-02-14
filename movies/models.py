from django.db import models
import uuid
# Create your models here.

class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim

class Movie(models.Model):
    
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True, verbose_name="Film Kategorisi")
    isim = models.CharField(max_length=100, verbose_name='Film İsmi')
    resim = models.FileField(upload_to='filmler/', verbose_name="Film Resmi")

    def __str__(self):
        return self.isim


# manytomany
# onetoone
# manytoone = foreignkey