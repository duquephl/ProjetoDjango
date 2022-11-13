"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.http import HttpResponse
from django.views.static import serve


def media_access(request, path, document_root=None):
    print(os.path.join(document_root, path))
    if os.path.exists(os.path.join(document_root, path)):
        if request.user.is_superuser:
            return serve(request, path, document_root)
        elif path.find('/termos/') != -1:
            return serve(request, path, document_root)
        elif request.user.is_anonymous:
            return HttpResponse('Not authorized to access this media.')
        elif path.find('/company_' + str(request.user.company.id) + '/') != -1:
            return serve(request, path, document_root)
        else:
            return HttpResponse('Not authorized to access this media.')
    else:
        return HttpResponse('Not authorized to access this media.')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^{}(?P<path>.*)$'.format(settings.MEDIA_URL[1:]), media_access, {'document_root': settings.MEDIA_ROOT}),
]
