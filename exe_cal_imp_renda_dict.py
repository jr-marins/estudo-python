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

print("##impostos pagados por cargos##".upper())
for cargo, imposto in imposto_por_cargo.items():
    print(f"{cargo} - imposto pago: R$ {imposto:.2f}")

