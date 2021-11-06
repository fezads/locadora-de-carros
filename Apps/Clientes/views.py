from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.

# Abre a tela de lista de clientes
def listarClientes(request):
    listaDeClientes = Cliente.objects.all()

    return render(request, 'clientes/index.html', {'clientes': listaDeClientes})

# Salva a cliente no banco de dados
# e redireciona para a lista de clientes
def cadastrarCliente(request):
    nome=request.POST['nome']
    cpf=request.POST['cpf']
    email=request.POST['email']
    telefone=request.POST['telefone']

    Cliente.objects.create(
        nome=nome,
        cpf=cpf,
        email=email,
        telefone=telefone
    )

    return redirect('/clientes')

# Abre a tela de edição com os dados da cliente selecionada
def editarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    listaDeClientes = Cliente.objects.all()

    return render(request, 'clientes/index.html', {
        'cliente': cliente,
        'clientes': listaDeClientes
    })

# Atualiza os dados da cliente no banco de dados
# e redireciona para a lista de clientes
def atualizarCliente(request, id):
    nome=request.POST['nome']
    cpf=request.POST['cpf']
    email=request.POST['email']
    telefone=request.POST['telefone']

    cliente = Cliente.objects.get(id=id)
    cliente.nome = nome
    cliente.cpf = cpf
    cliente.email = email
    cliente.telefone = telefone
    cliente.save()

    return redirect('/clientes')

# Deleta a cliente do banco de dados
def deletarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()

    return redirect('/clientes')