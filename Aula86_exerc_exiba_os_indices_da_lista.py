'''
EXERCÍCIO

Exiba o indice dos ítens de uma lista

range = gera números
'''


minha_lista = ["Marcos", "Marins", "Santos"]

# Usando range para gerar números até o tamanho da minha_lista
indices = range(len(minha_lista))

# iterando sobre os índices criado com o range
for indice in indices:
    print( indice, minha_lista[indice] )

########## proxima aula, entenderemos sobre empacotamento #########