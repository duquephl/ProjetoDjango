import pytz
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from datetime import timezone


# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username']

    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    rua = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    cep = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=100, null=False, blank=False, unique=True)
    celular = models.CharField(max_length=100, null=False, blank=False, unique=True)
    cpf = models.CharField(max_length=100, null=False, blank=False, unique=True)
    rg = models.CharField(max_length=100, null=False, blank=False, unique=True)
    #data_nascimento = models.DateField(null=False, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


