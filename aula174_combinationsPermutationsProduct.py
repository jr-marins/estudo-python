'''
Combinations, Permutations e product - Itertools
combinação - Ordem não importa - iterável + tamanho do grupo
permutação - Ordem importa
Produto - Ordem importa e repete valores únicos.

'''

from itertools import combinations, permutations, product

# função para desenpacotar e printar de forma mais legível
def printIter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'joão', 'joana', 'luiz', 'leticia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino'],
    ['algodão', 'poliestes']
]

# combinations faz a combinação de dados, aqui passo o iterável e o tamanho do grupo(combinação de 2 itens)

# printIter(combinations(pessoas, 2))
# print()
# printIter(permutations(pessoas, 2))

printIter(product(*camisetas))
# saida:
'''
('preta', 'p')
('preta', 'm')
('preta', 'g')
('branca', 'p')
('branca', 'm')
('branca', 'g')
'''