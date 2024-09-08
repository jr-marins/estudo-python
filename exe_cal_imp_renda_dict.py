'''
Desafio :

criar um dicionário contendo cargos e salários e calcular o valor pago para 
o imposto de renda de cada cargo
'''

# criando o dict
cargo_salario = {
    "gerente": 1000.0,
    "desenvolvedor": 5000.0,
    "estagiario": 800.0,
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


# crianod o dict que vai guarda os valores do impostos
imposto_por_cargo = {}

def cal_imposto(sal_bruto):
    if sal_bruto > 1000:
        return sal_bruto * 0.20 # 20% de imposto
    else:
        return sal_bruto * 0.15

for cargo, salario in cargo_salario.items():
    imposto = cal_imposto(salario)
    imposto_por_cargo[cargo] = imposto

print("##impostos pagados por cargos## \n".upper())
for cargo, imposto in imposto_por_cargo.items():
    print(f"{cargo} - imposto pago: R$ {imposto:.2f}")

# Encontrar o cargo com o maior salário
cargo, salario = encontrar_maior_salario(cargo_salario)
print(f"\nO cargo com o maior salário é '{cargo}' com salário de R$ {salario:.2f}")

