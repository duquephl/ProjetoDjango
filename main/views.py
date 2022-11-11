from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Produto, Fabricante
from .forms import ProdutoForm, FabricanteForm
from allauth.account.views import LoginView, LogoutView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/home.html'


class SobreView(TemplateView):
    template_name = 'main/sobre.html'


class ContatoView(TemplateView):
    template_name = 'main/contato.html'


class ProdutoView(ListView):
    model = Produto
    queryset = Produto.objects.all().order_by('nome_produto')


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    success_url = "/produtos/"


class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    success_url = "/produtos/"


class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = "/produtos/"


class ProdutoDetailView(DetailView):
    queryset = Produto.objects.all()
    template_name = "main/detalhesdoproduto.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


class FabricanteView(ListView):
    model = Fabricante
    queryset = Fabricante.objects.all().order_by('fabricante')


class FabricanteCreateView(CreateView):
    model = Fabricante
    form_class = FabricanteForm
    success_url = "/fabricantes/"


class FabricanteUpdateView(UpdateView):
    model = Fabricante
    form_class = FabricanteForm
    success_url = "/fabricantes/"


class FabricanteDeleteView(DeleteView):
    model = Fabricante
    success_url = "/fabricantes/"


class FabricanteDetailView(DetailView):
    queryset = Fabricante.objects.all()
    template_name = "main/detalhesdofabricante.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FabricanteDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


class PerfilView(TemplateView):
    template_name = "main/perfil.html"


class LoginView(LoginView):
    template_name = "account/login.html"
    success_url = "/home/"
    redirect_field_name = "/home/"


class LogoutView(LogoutView):
    template_name = "account/logout.html"
    success_url = " "
    redirect_field_name = " "



'''
def home(request):
    return render(request, 'main/home.html')

def sobre(request):
    return render(request, 'main/sobre.html')

def contato(request):
    return render(request, 'main/contato.html')
'''
