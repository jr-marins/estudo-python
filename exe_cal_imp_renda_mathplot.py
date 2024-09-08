# importando a lib
import matplotlib.pyplot as plt

# criando o dict
cargo_salario = {
    "Engenheiro": 18000.0,
    "Gerente": 10000.0,
    "Desenvolvedor": 5000.0,
    "Design": 3000.0,
    "Estagiario": 800.0,
}

# função que retorna o cargo com o maior salário
def encontrar_maior_salario(cargo_salario):
    maior_salario = 0  # Variável para armazenar o maior salário
    cargo_maior_salario = ""  # Variável para armazenar o cargo com maior salário

    # Percorrendo o dicionário
    for cargo, salario in cargo_salario.items():
        if salario > maior_salario:  # Se o salário atual for maior que o maior salário
            maior_salario = salario  # Atualiza o maior salário
            cargo_maior_salario = cargo  # Atualiza o cargo correspondente

    return cargo_maior_salario, maior_salario

# Encontrar o cargo com o maior salário
cargo, salario = encontrar_maior_salario(cargo_salario)
print(f"O cargo com o maior salário é '{cargo}' com salário de R$ {salario:.2f}")

# Gerando o gráfico de salários
def gerar_grafico(cargo_salario):
    cargos = list(cargo_salario.keys())  # Nomes dos cargos
    salarios = list(cargo_salario.values())  # Valores dos salários

    # Criando gráfico de barras
    plt.bar(cargos, salarios, color='skyblue')
    plt.xlabel('Cargos')
    plt.ylabel('Salários (R$)')
    plt.title('Salários por Cargo')
    
    # Exibir o maior salário no gráfico
    plt.text(cargos[salarios.index(max(salarios))], max(salarios), f'R$ {max(salarios):.2f}', 
             ha='center', va='bottom', color='red', fontsize=12)

    # Exibindo o gráfico
    plt.show()

# Chamando a função para gerar o gráfico
gerar_grafico(cargo_salario)
