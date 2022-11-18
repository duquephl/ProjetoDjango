from rest_framework import serializers
from django.contrib.auth.models import User, Group
from main.models import Produto,Fabricante

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

