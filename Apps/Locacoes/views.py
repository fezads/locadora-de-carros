from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import Locacao
from Apps.Carros import models as carro_models
from Apps.Clientes import models as cliente_models

# Create your views here.

# Abre a tela de lista de locacoes
def listarLocacoes(request):
    listaDeLocacoes = Locacao.objects.all()
    listaDeCarros = carro_models.Carro.objects.all()
    listaDeClientes = cliente_models.Cliente.objects.all()

    return render(request, 'locacoes/index.html', {
        'locacoes': listaDeLocacoes,
        'carros': listaDeCarros,
        'clientes': listaDeClientes,
    })

# Salva a locacao no banco de dados
# e redireciona para a lista de locacoes
def cadastrarLocacao(request):
    try:
        carro = request.POST['carro']
        cliente = request.POST['cliente']
        data_retirada = request.POST['data_retirada']
        data_devolucao = request.POST['data_devolucao']
        valor = request.POST['valor']
        observacoes = request.POST['observacoes']

        carro = carro_models.Carro.objects.get(id=carro)
        cliente = cliente_models.Cliente.objects.get(id=cliente)

        # transforma as datas em datetime
        data_retirada = datetime.strptime(data_retirada, '%d/%m/%Y').date()
        data_devolucao = datetime.strptime(data_devolucao, '%d/%m/%Y').date()

        Locacao.objects.create(
            carro=carro,
            cliente=cliente,
            data_retirada=data_retirada,
            data_devolucao=data_devolucao,
            valor=valor,
            observacoes=observacoes
        )

        messages.success(request, 'Locação cadastrada com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/locacoes')

# Abre a tela de edição com os dados da locacao selecionada
def editarLocacao(request, id):
    locacao = Locacao.objects.get(id=id)
    listaDeLocacoes = Locacao.objects.all()
    listaDeCarros = carro_models.Carro.objects.all()
    listaDeClientes = cliente_models.Cliente.objects.all()

    return render(request, 'locacoes/index.html', {
        'locacao': locacao,
        'locacoes': listaDeLocacoes,
        'carros': listaDeCarros,
        'clientes': listaDeClientes,
    })

# Atualiza os dados da locacao no banco de dados
# e redireciona para a lista de locacoes
def atualizarLocacao(request, id):
    try:
        carro = request.POST['carro']
        cliente = request.POST['cliente']
        data_retirada = request.POST['data_retirada']
        data_devolucao = request.POST['data_devolucao']
        valor = request.POST['valor']
        observacoes = request.POST['observacoes']

        carro = carro_models.Carro.objects.get(id=carro)
        cliente = cliente_models.Cliente.objects.get(id=cliente)

        # transforma as datas em datetime
        data_retirada = datetime.strptime(data_retirada, '%d/%m/%Y').date()
        data_devolucao = datetime.strptime(data_devolucao, '%d/%m/%Y').date()
        
        locacao = Locacao.objects.get(id=id)
        locacao.carro = carro
        locacao.cliente = cliente
        locacao.data_retirada = data_retirada
        locacao.data_devolucao = data_devolucao
        locacao.valor = valor
        locacao.observacoes = observacoes
        locacao.save()

        messages.success(request, 'Locação atualizada com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/locacoes')

# Deleta a locacao do banco de dados
def deletarLocacao(request, id):
    try:
        locacao = Locacao.objects.get(id=id)
        locacao.delete()

        messages.success(request, 'Locação removida com sucesso!')
    except:
        messages.error(request, 'Ocorreu um erro. Por favor tente novamente.')

    return redirect('/locacoes')