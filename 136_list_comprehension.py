'''
lista comprehension é uma forma de criar lista de forma rápida
# print(list(range(10)))
'''

# lista vazia
lista = []
print(lista, "\n",5*"#") #printa lista vazia
print()

lista = [
        numero
        for numero in range(10)
        ] # agora minha lista tem 10 itens

print(lista, "\n\n")

# caso eu queira usar uma logica em que na minha lista receba apenas valores multiplicado por 2 ou qualquer ooutro valor

l1 = [
    numero * 2
    for numero in range(10)
]

print(l1) # saida será 10 valores multiplicados por 2. isso é um mapeamento.
# quando o parametro estiver a esquerda do for é um mapeamento, quando estiver à esquerda, é um filtro.

