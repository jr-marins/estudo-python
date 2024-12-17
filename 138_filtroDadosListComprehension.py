import pprint 
'''
Filtro de dados é caracterizado pelo if ao lado direito do for.
Ou seja: 
    para um conjunto de itens exiba um item se(if) ele for [...]

'''

# criandno uma lista qualquer com list comprehension
lista = [n for n in range(10)]

pprint.pprint(lista)

lista_filtrada = [
    n for n in range(20) if n < 15
]

pprint.pprint(lista_filtrada)
# >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
