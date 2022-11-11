from django.contrib import admin

from main.models import Fabricante, Produto, User

# Register your models here.

admin.site.header = 'Administração do Site'
admin.site.register(Produto)
admin.site.register(Fabricante)
admin.site.register(User)