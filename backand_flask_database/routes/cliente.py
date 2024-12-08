from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

"""
    Rotas de clientes

    - /clientes/ (GET) - listar os clientes
    - /clientes/ (POST) - inserir o cliente no servidor
    - /clientes/new (GET) - renderizar o formulário para criar um cliente
    - /clietes/<id> (GET) - obter os dados de um cliente
    - /clientes<id>/edit (GET) - renderizar um formulário para editar um cliente
    - /cliente/<id>/update (PUT) - atualizar os dados de um cliente
    - /cliente/<id>/delete (DELETE) - deleta um registro do usuário
"""

@cliente_route.route('/')
def lista_clientes():
    """ lISTAR CLIENTES """
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Inserir os dados do cliente"""
    
    data = request.json

    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email'],
    )
    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
    """ Formulário para cadastrar um cliente"""
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Exibir edetalhes do cliente"""

    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ formulário para editar um cliente"""
    cliente = Cliente.get_by_id(cliente_id)

    return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ atualizar informações de um cliente"""
    # obter dados do usuário pelo formulário
    data = request.json


    cliente_editado =  Cliente.get_by_id(cliente_id)

    # obter usuário por id
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()

    # editar usuário
    return render_template('item_cliente.html', cliente=cliente_editado)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """ deletar informações de um cliente"""
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {"deleted": 'ok'}



