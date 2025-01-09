

'''
Exercício - unir listas.
Crie uma função zipper(como o zipper de roupas)
listas na ordem.
use todos os valores da menor lista.
Ex:
    ["salvador", "Ubatuba", "Belo Horizonte"]
    ["BA", "SP", "MG", "RJ" ]
resultado:
    [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

'''


# realizando o exercício na mão. antes de aprender a funcao ziper
# definir a função
def zipper(l1, l2):
    # função min retorna a menor lista
    intervaloMaximo = min(len(l1), len(l2))

    # retorna uma listcomprehension
    # pegando o indice de cada linha e colocando em uma tupla
    return [(l1[i], l2[i]) for i in range(intervaloMaximo)]

novaLista = ...

cidade = ["salvador", "Ubatuba", "Belo Horizonte"]
estado = ["BA", "SP", "MG", "RJ" ]

# print(zipper(cidade, estado))

'''
O python já tem uma função que faz exatamente isso !
A função ZIP
'''
from itertools import zip_longest
print(list(zip(cidade, estado)))
# temos tbm a funcao zip_longest
'''
zip_longest faz exatamente o inverso, ele usa a lista com o maior indice
'''

print(list(zip_longest(cidade, estado, fillvalue= "não tem cidade")))