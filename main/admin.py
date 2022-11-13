from django.contrib import admin

from main.models import Fabricante, Produto, Docs, Agreement

# Register your models here.

admin.site.header = 'Administração do Site'
admin.site.register(Docs)
admin.site.register(Agreement)
admin.site.register(Produto)
admin.site.register(Fabricante)
