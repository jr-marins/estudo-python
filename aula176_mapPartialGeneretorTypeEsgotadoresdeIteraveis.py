'''

'''
from functools import partial
# partial é uma função que recebe uma função

# map - para mapear dados
def printIteravel(iterador):
    # desempacota e esgota-o em uma lista
    print(*list(iterador), sep='\n')

# lista de dicionários
produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]

# --------- mapeamento com list comprehension --------------------
novosProdutos = [
    {**produto, 'preco': produto['preco'] * 1.05}
     for produto in produtos 
]


# ---------------------------------------------------------

# --------- Fazendo uma função que aumenta a % -------------
''' A função recebe o valor e a porcentagem que de deseja aumentar '''
def aumentarPorcentagem(valor, porcentagem):

    ''' round faz operações matemáticas exatas '''
    return round(valor * porcentagem)

''' partial recebe uma funcao'''
aumentarDezPorCento = partial(
    # primeiro argumento e a funcao aumentarPorcentagem, o segundo é o argumento nomeado
    aumentarPorcentagem,
    porcentagem=1.1
)

novosProdutosComPartial = [
    {**produto,
    'preco': aumentarDezPorCento(produto['preco'])}
     for produto in produtos 
]



# ----------------- funcao map -------------------------
# a outra funcao
def mudaPrecoProd(produto):
    return {
        **produto,
        'preco': aumentarDezPorCento(
            produto['preco']
            )
    }

''' ela precisa de outra funcao. Essa outra funcao que vai fazer oque eu quero'''
novosProdutosMap = map(
    mudaPrecoProd,
    produtos
)

# ----------- com lambda e map ---------------
''' quero exibir os numeros de uma lista multiplicados por x '''
print('com map e lambda\n',
   list( map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
    )


print()
print("com listconprehension")
print(*novosProdutos, sep='\n')
print()
print("com partial")
print(*novosProdutosComPartial, sep='\n')
print()
print("Com map")
printIteravel(novosProdutosMap)