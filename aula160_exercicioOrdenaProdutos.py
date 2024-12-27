import pprint

# copy, sorted, produtos.sort

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
prod_aumento = [
    {**produto, "preco": produto["preco"] * 1.05}
    for produto in produtos
]

# Gere novos_produtos por deep copy (cópia profunda)
pprint.pprint(prod_aumento)

print("Lista origin\n".upper())
pprint.pprint(produtos)
print()


# Ordene os produtos por nome decrescente (do maior para menor)

print("Ordenado por nome(ordem decrescente)".upper())
prod_orden_nome = sorted(produtos, key=lambda item: item["nome"])
for item in prod_orden_nome:
    print(item)
print()

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)

print("Produto ordenado por preço.".upper())
prod_orden_preco = sorted(produtos, key=lambda item: item["preco"])
for item in prod_orden_preco:
    print(item)

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)