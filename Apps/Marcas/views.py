from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Marca

# Create your views here.

# Abre a tela de lista de marcas
def listarMarcas(request):
    listaDeMarcas = Marca.objects.all()
    return render(request, 'marcas/index.html', {'marcas': listaDeMarcas})

# Salva a marca no banco de dados
# e redireciona para a lista de marcas
def cadastrarMarca(request):
    try:
        nome=request.POST['nome']
        descricao=request.POST['descricao']

        Marca.objects.create(
            nome=nome,
            descricao=descricao
        )

        messages.success(request, 'Marca cadastrada com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/marcas')

# Abre a tela de edição com os dados da marca selecionada
def editarMarca(request, id):
    marca = Marca.objects.get(id=id)
    listaDeMarcas = Marca.objects.all()

    return render(request, 'marcas/index.html', {
        'marca': marca,
        'marcas': listaDeMarcas
    })

# Atualiza os dados da marca no banco de dados
# e redireciona para a lista de marcas
def atualizarMarca(request, id):
    try:
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        
        marca = Marca.objects.get(id=id)
        marca.nome = nome
        marca.descricao = descricao
        marca.save()

        messages.success(request, 'Marca atualizada com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/marcas')

# Deleta a marca do banco de dados
def deletarMarca(request, id):
    try:
        marca = Marca.objects.get(id=id)
        marca.delete()

        messages.success(request, 'Marca removida com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/marcas')