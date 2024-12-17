import json

def exibir_dados(clientes):
    """
    Exibe os dados de todos os clientes, incluindo o histórico formatado.
    """
    if not clientes:
        return "Nenhum cliente cadastrado."
    
    linhas = []
    for cliente in clientes:
        linhas.append(f"Codigo: {cliente['Codigo']}")
        linhas.append(f"Nome: {cliente['Nome']}")
        linhas.append(f"Endereco: {cliente['Endereco']}")
        linhas.append(f"Contato: {cliente['Contato']}")
        linhas.append(f"Histórico:{formatar_historico(cliente['Histórico'])}")
        linhas.append("-" * 20)
    
    return "\n".join(linhas)


def formatar_historico(historico):
    """
    Formata o histórico de vendas para uma exibição legível.
    """
    if not historico:
        return " Nenhuma venda registrada."
    
    linhas = []
    for i, venda in enumerate(historico, 1):
        linhas.append(f"\n  {i}. Descrição: {venda['Descrição']} | Valor: R$ {venda['Valor']:.2f}")
    
    return "".join(linhas)


def adicionar_cliente(lista_clientes, cliente):
    """ Adiciona um novo cliente à lista. """
    lista_clientes.append(cliente)


def atualizar_cliente(lista_clientes, codigo, novos_dados):
    """ Atualiza os dados de um cliente baseado no código. """
    for cliente in lista_clientes:
        if cliente["Codigo"] == codigo:
            cliente.update({k: v for k, v in novos_dados.items() if v})
            return True
    return False


def deletar_cliente(lista_clientes, codigo):
    """ Deleta um cliente pelo código. """
    for cliente in lista_clientes:
        if cliente["Codigo"] == codigo:
            lista_clientes.remove(cliente)
            return True
    return False


def salvar_dados(arquivo, dados):
    """ Salva os dados no arquivo JSON. """
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


def carregar_dados(arquivo):
    """ Carrega os dados do arquivo JSON. """
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def registrar_venda(clientes, codigo, venda):
    """ Registra uma venda para o cliente pelo código. """
    for cliente in clientes:
        if cliente["Codigo"] == codigo:
            cliente.setdefault("Histórico", []).append(venda)
            return True
    return False
