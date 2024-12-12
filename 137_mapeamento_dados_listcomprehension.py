'''
mapeamennto de dados com list comprehension
'''

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]


novos_produtos = [
    produto
    for produto in produtos
]

lista_mapeada = [
    {**produto, "preco": produto["preco"] * 1.05}
    for produto in produtos
]

print(*lista_mapeada, sep="\n")