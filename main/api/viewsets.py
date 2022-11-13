from django.contrib.auth.models import Group, User
from django_filters.rest_framework import DjangoFilterBackend
from main.api.serializers import (FabricanteSerializer, ProdutoSerializer,)#GroupSerializer, UserSerializer)
from main.models import Fabricante, Produto
from rest_framework import permissions, viewsets, filters


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['fabricante', 'nome_produto', 'id']
    search_fields = ['fabricante', 'nome_produto']
    ordering_fields = ['nome_produto', 'fabricante', 'id']


class FabricanteViewSet(viewsets.ModelViewSet):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['fabricante', 'id']
    search_fields = ['fabricante']
    ordering_fields = ['fabricante', 'id']

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['username','email','id']
#     search_fields = ['username','email']
#     ordering_fields = ['username','email','id']
#
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['name','id']
#     search_fields = ['name']
#     ordering_fields = ['name','id']
