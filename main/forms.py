from django import forms
from .models import Produto, Fabricante, Docs


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'fabricante', 'codigo_de_barra', 'preco', 'gramatura', 'imagem_produto', 'sobre']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fabricante'].queryset = Fabricante.objects.all()


class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['fabricante', 'imagem_logo', 'sobre']


class DocsForm(forms.ModelForm):
    class Meta:
        model = Docs
        fields = ['nome_documento', 'arquivo', 'sobre']
