from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarLocacoes, name='locacoes'),
    path('<int:id>/', views.editarLocacao, name='locacoes'),
    path('cadastrar/', views.cadastrarLocacao),
    path('atualizar/<int:id>', views.atualizarLocacao),
    path('deletar/<int:id>', views.deletarLocacao),
]