from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarCarros, name='carros'),
    path('<int:id>/', views.editarCarro, name='carros'),
    path('cadastrar/', views.cadastrarCarro),
    path('atualizar/<int:id>', views.atualizarCarro),
    path('deletar/<int:id>', views.deletarCarro),
]