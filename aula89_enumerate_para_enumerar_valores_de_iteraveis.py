'''
ENUMERATE

Enumera iteráveis (cria indices)

lista_numerada = enumerate(nome)

'''

nome = ["Marcos", "Marins", "Santos"]

# criando índices e exibindo... 
for indice, nome in enumerate(nome):
    print(indice, nome)
# >> 0 Marcos
# >> 1 Marins
# >> 2 Santos

