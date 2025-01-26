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

# -------- Filtro com listcomprehension ---------
novosProdu = [
    produto for  produto in produtos
    if produto['preco'] > 10
]
#  ----------------------------

# -------------- Filtro com filter -----------------
''' Primeiro parâmetro é um funcao
    Segundo é um iterável '''

novosProduFilter = filter(
    lambda produto: produto['preco'] > 10,
    produtos
)


# para comparar vou fazer uma funcao que filtra 
def filtrarPreco(produto):
    return produto['preco'] > 100

novosProduFuncaoFiltrar = filter(
    filtrarPreco,
    produtos
)

# ----------------------------------------------

print("com listconprehension'")
print(*novosProdu, sep='\n')

print()

print("Com filter")
printIteravel(novosProduFilter)

print()

print("com a funcao filtrar preco")
print(*novosProduFuncaoFiltrar, sep='\n')