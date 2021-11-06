from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarLocacoes),
    path('cadastrar/', views.cadastrarLocacao),
    path('<id>/', views.editarLocacao),
    path('atualizar/<int:id>', views.atualizarLocacao),
    path('deletar/<int:id>', views.deletarLocacao),
]