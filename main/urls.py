from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from .views import HomeView, SobreView, ContatoView, ProdutoView, ProdutoCreateView, ProdutoUpdateView, \
    ProdutoDeleteView, ProdutoDetailView, FabricanteView, FabricanteCreateView, FabricanteUpdateView, \
    FabricanteDeleteView, FabricanteDetailView, LoginView, LogoutView, PerfilView
from rest_framework.routers import DefaultRouter
from main.api.viewsets import ProdutoViewSet, FabricanteViewSet, UserViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='Produto')
router.register(r'fabricantes', FabricanteViewSet, basename='Fabricante')
router.register(r'users', UserViewSet, basename='User')
router.register(r'groups', GroupViewSet, basename='Group')

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    path('home/', login_required(HomeView.as_view()), name='home'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('accounts/profile/', login_required(PerfilView.as_view()), name='Perfil'),
    path('produtos/', login_required(ProdutoView.as_view()), name='produtos'),
    path('cadastroproduto/', login_required(ProdutoCreateView.as_view()), name='cadastro_produto'),
    path('detalhesdoproduto/<int:pk>', login_required(ProdutoDetailView.as_view()), name='detalhes_do_produto'),
    path('alterarproduto/<int:pk>', login_required(ProdutoUpdateView.as_view()), name='alterar_produto'),
    path('apagarproduto/<int:pk>', login_required(ProdutoDeleteView.as_view()), name='apagar_produto'),
    path('fabricantes/', login_required(FabricanteView.as_view()), name='fabricantes'),
    path('cadastrofabricante/', login_required(FabricanteCreateView.as_view()), name='cadastro_fabricante'),
    path('detalhesdofabricante/<int:pk>', login_required(FabricanteDetailView.as_view()), name='detalhes_do_fabricante'),
    path('alterarfabricante/<int:pk>', login_required(FabricanteUpdateView.as_view()), name='alterar_fabricante'),
    path('apagarfabricante/<int:pk>', login_required(FabricanteDeleteView.as_view()), name='apagar_fabricante'),
    path('sobre/', login_required(SobreView.as_view()), name='sobre'),
    path('contato/', login_required(ContatoView.as_view()), name='contato'),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
