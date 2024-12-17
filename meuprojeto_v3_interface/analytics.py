import matplotlib.pyplot as plt

def cliente_top_faturamento(clientes):
    """
    Analisa os clientes e cria um gráfico de pizza para os clientes que geraram faturamento.
    :param clientes: Lista de dicionários contendo os dados dos clientes.
    :return: String informando o cliente com maior faturamento e gráfico de pizza gerado.
    """
    if not clientes:
        return "Nenhum cliente cadastrado."

    total_faturamento = 0
    faturamento_por_cliente = {}

    # Cálculo de faturamento total e por cliente
    for cliente in clientes:
        historico = cliente.get("Histórico", [])
        faturamento_cliente = sum(venda["Valor"] for venda in historico)
        faturamento_por_cliente[cliente["Nome"]] = faturamento_cliente
        total_faturamento += faturamento_cliente

    if total_faturamento == 0:
        return "Nenhum faturamento registrado."

    # Identifica o cliente com maior faturamento
    cliente_top = max(faturamento_por_cliente, key=faturamento_por_cliente.get)
    faturamento_top = faturamento_por_cliente[cliente_top]
    porcentagem = (faturamento_top / total_faturamento) * 100

    # Exibe gráfico de pizza
    labels = faturamento_por_cliente.keys()
    valores = faturamento_por_cliente.values()

    plt.figure(figsize=(8, 6))
    plt.pie(valores, labels=labels, autopct="%.1f%%", startangle=90, colors=plt.cm.tab20.colors)
    plt.title("Faturamento por Cliente")
    plt.show()

    return (
        f"O cliente com maior faturamento foi: {cliente_top}\n"
        f"Faturamento: R$ {faturamento_top:.2f} ({porcentagem:.2f}% do total de R$ {total_faturamento:.2f})"
    )
