'''
Listas em python

Tipo lista - Mutável
Suporta varios valores
Conhecimentos reutilizáveis - índices e fatiamento

Métodos úteis em lista :
> append = adiciona um item no final da lista
> insert = Adiciona um ítem no índice escolhido
> pop = Remove o último ítem da lisita ou o índice escolhido e retorna o valor
> del = apaga um índice
> clear = limpa a lista
> extend = estende a lista + concatena listas
> Copy = copia a lista criando um novo espaço na memória 
> e etc ...

'''

# Criação de uma lista
minha_lista = ["dados", "código", "lógica"]

# Usando conhecimento que já vimos = acessando por índice
print(minha_lista[2])
# >> "lógica"

print()

# Alterando ítem pelo índice
minha_lista[2] = "Lógica de programação"
print(minha_lista)
# >> ['dados', 'código', 'Lógica de programação']

print()

# Pegando um valor da lista pelo índice e jogando dentro de uma variável
base = minha_lista[0]
print(base)
# >> Dados
# OBS: o valor enviado para a variável, continua existindo na minha_lista

print()

# append = adicionando novo ítem
minha_lista.append("python")
print(minha_lista)
# >> ['dados', 'código', 'Lógica de programação', 'python']

print()

# pop = removendo um ítem
# minha_lista.pop()

# Podemos ver o valor que foi removido guardando-o em uma variável
removido = minha_lista.pop()
print(minha_lista, "Removido: ", removido)
# >> ['dados', 'código', 'Lógica de programação'] Removido:  python

# Com pop podemos também remover multiplos ítens por vez QUANDO FOR UMA LISTA PEQUENA
# EX minha_lista.pop([])

# Del = deleta um ítem
minha_lista.append(123)
print("\n", minha_lista)
# >> ['dados', 'código', 'Lógica de programação', 123]

del minha_lista[-1] # Removendo o último ítem por meio de um índice invertido
print("\n", minha_lista)
# >> ['dados', 'código', 'Lógica de programação']

# Insert = adicionando um ítem em um índice escolhido.
minha_lista.insert(0, "Base de Dados")
# O insert recebe dois parametros, um se refere ao local em que você irá alterar o outro é o valor que você vai adicionar
print("\n", minha_lista)
# >>  ['Base de Dados', 'dados', 'código', 'Lógica de programação']

# Extend = 
lista_a = ["Developer", "Software"]
lista_a.extend(minha_lista)
print("\n", lista_a)
# >> ['Developer', 'Software', 'Base de Dados', 'dados', 'código', 'Lógica de programação']
# o extend não retorna nada, somente altera a lista silenciosamente.

# Conacatenando = lista + lista
lista_b = ["Eu sou"]
lista_mae = lista_b + lista_a
print("\n", lista_mae)
# >>  ['Eu sou', 'Developer', 'Software', 'Base de Dados', 'dados', 'código', 'Lógica de programação']

# Copy = copia a lista criando um novo espaço na memória
lista_c = lista_mae.copy() # copiou a lista e criou um novo local na memória
# para confirmar, vou alterar a lista original e veremos que a cópia não será afetada.
lista_mae[0] = "Eu serei" # Alterei um ítem pelo índice
print("\n", lista_mae)
# >>  ['Eu serei', 'Developer', 'Software', 'Base de Dados', 'dados', 'código', 'Lógica de programação']
print("\n", lista_c)
# >> ['Eu sou', 'Developer', 'Software', 'Base de Dados', 'dados', 'código', 'Lógica de programação']
# A lista gerada através da cópia não foi afetada pela alteração.

# sort
lista.sort(key=lambda item: item) #mexe diretamente na lista

# sorted
l1 = sorted(lista, key=lambda item: item['nome']) # faz uma copia da lista original


# função para unir duas listas zip
cidade = ["salvador", "Ubatuba", "Belo Horizonte"]
estado = ["BA", "SP", "MG", "RJ" ]
print(list(zip(cidade, estado)))

# zip longest unir duas listas
from itertools import zip_longest
print(list(zip_longest(cidade, estado, fillvalue= "não tem cidade")))