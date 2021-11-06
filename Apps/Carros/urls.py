from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarCarros),
    path('cadastrar/', views.cadastrarCarro),
    path('<id>/', views.editarCarro),
    path('atualizar/<int:id>', views.atualizarCarro),
    path('deletar/<int:id>', views.deletarCarro),
]