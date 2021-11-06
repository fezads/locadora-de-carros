from django.shortcuts import render, redirect
from .models import Marca

# Create your views here.

# Abre a tela de lista de marcas
def listarMarcas(request):
    listaDeMarcas = Marca.objects.all()
    return render(request, 'marcas/index.html', {'marcas': listaDeMarcas})

# Salva a marca no banco de dados
# e redireciona para a lista de marcas
def cadastrarMarca(request):
    nome=request.POST['nome']
    descricao=request.POST['descricao']

    Marca.objects.create(nome=nome, descricao=descricao)

    return redirect('/marcas')

# Abre a tela de edição com os dados da marca selecionada
def editarMarca(request, id):
    marca = Marca.objects.get(id=id)
    listaDeMarcas = Marca.objects.all()

    return render(request, 'marcas/index.html', {'marca': marca, 'marcas': listaDeMarcas})

# Atualiza os dados da marca no banco de dados
# e redireciona para a lista de marcas
def atualizarMarca(request, id):
    nome = request.POST['nome']
    descricao = request.POST['descricao']
    
    marca = Marca.objects.get(id=id)
    marca.nome = nome
    marca.descricao = descricao
    marca.save()

    return redirect('/marcas')

# Deleta a marca do banco de dados
def deletarMarca(request, id):
    marca = Marca.objects.get(id=id)
    marca.delete()

    return redirect('/marcas')