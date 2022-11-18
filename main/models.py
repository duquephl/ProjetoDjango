import imghdr
import os
import shutil

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from pathlib import Path
from django.core.files.storage import FileSystemStorage
from django import forms
from operator import mod

from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.deconstruct import deconstructible


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


class Docs(models.Model):
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['nome_documento']

    nome_documento = models.CharField(max_length=256)
    arquivo = models.FileField(upload_to='files/documentos/')
    sobre = models.TextField()

    def __str__(self) -> str:
        return self.nome_documento


BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = BASE_DIR / "media"


def rename_file(instance, filename):
    print(str(MEDIA_ROOT) + "/" + instance.dir + instance.name + '.pdf')
    if os.path.exists(str(MEDIA_ROOT) + "/" + instance.dir + instance.name + '.pdf'):
        os.remove(str(MEDIA_ROOT) + "/" + instance.dir + instance.name + '.pdf')
    return instance.dir + instance.name + '.pdf'


class Agreement(models.Model):
    class Meta:
        verbose_name = 'Termo'
        verbose_name_plural = 'Termos'
        ordering = ['name']

    name = models.CharField(max_length=256)
    dir = models.CharField(max_length=256, default='agreements/')
    file = models.FileField(upload_to=rename_file, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    about = models.TextField()

    def __str__(self) -> str:
        return self.name
