'''
Considerando dusa listas de inteiros ou floats
Some os valores nas listas retornando uma nova lista com os valores somados.

se uma lista for maior que a outra, a soma só vai considerar o tamanho da lista menor.

EX:
l1 = [1,2,3,4,5,6,7]
l2 = [1,2,3,4,]
######################
nova_lista = [2,4,6,8]
'''


lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4,]

# agora usando a função zip
nova_lista = [ x + y for x, y in zip(lista_a, lista_b) ]

print(nova_lista)

# primeor vamos fazer na forma procedural

# for indice in range(len(lista_b)):
#     nova_lista.append(lista_a[indice] + lista_b[indice])

# print(nova_lista)


# for indice, _ in enumerate(lista_b):
#     nova_lista.append(lista_a [indice] + lista_b [indice])

# print(nova_lista)