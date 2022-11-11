from django.core.files.storage import FileSystemStorage
from django import forms
from operator import mod
from django.db import models

# Create your models here.
class Fabricante(models.Model):
    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'
        ordering = ['fabricante']

    fabricante = models.CharField(max_length=100)
    imagem_logo = models.ImageField(upload_to='images/fabricantes/')
    sobre = models.TextField()

    def __str__(self) -> str:
        return self.fabricante
        
class Produto(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome_produto']
    
    nome_produto = models.CharField(max_length=256)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, blank=True)
    codigo_de_barra = models.PositiveBigIntegerField()
    preco = models.FloatField()
    gramatura = models.FloatField()
    imagem_produto = models.ImageField(upload_to='images/produtos/')
    sobre = models.TextField()

    def __str__(self) -> str:
        return self.nome_produto

class User(models.Model):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']
    
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    def __str__(self) -> str:
        return self.username
