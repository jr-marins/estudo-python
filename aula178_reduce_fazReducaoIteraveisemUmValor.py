# Reduce

'''
Reduce faz a redução de um itervel em um valor,
por ex:

resumir o valor de uma lista.
'''

from functools import reduce

produtos = [
    {'nome': 'produto 5 ', 'preco': 10.00},
    {'nome': 'produto 1 ', 'preco': 22.32},
    {'nome': 'produto 3 ', 'preco': 10.11},
    {'nome': 'produto 2 ', 'preco': 105.87},
    {'nome': 'produto 4 ', 'preco': 69.90},
]

def funcaoDoReduce(acumulador, produto):
    print("acumulador", acumulador)
    print("produto", produto)
    print()
    return acumulador + produto['preco']

total = reduce(
    funcaoDoReduce,
    produtos,
    0
)

# ------------   Usando lambda ---------------------

total1 = reduce(
    lambda acumulador, produto: acumulador + produto["preco"],
    produtos,
    0
)

print("Total é:", total)
print()
print("Total com lambda:", total1)
