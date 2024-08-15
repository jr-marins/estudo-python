'''
Split e join com list e str

- split = divide uma string

- join = une uma string

- replace = substitui caracter

- count = contar uma string
'''

# split
minha_frase = "     Tamo aí,   sempre na atividade   "

# o split recebe um argumento, que corresponde aonde ele vai separar a palavra ou string.
lista_palavra = minha_frase.split(",")

# para não alterar a lsita original, criei uma lista vazia para armazenar a frase formatada
lista_nova = []
print(lista_palavra)
# aqui ele cortou o ","
# >> ['     Tamo aí', '   sempre na atividade   ']
print()

# usando o for
for i, frase in enumerate(lista_palavra):
    print(lista_palavra[i].strip())
# strip corta os espaços de ambos os lados
'''Tamo aí
sempre na atividade'''
# rstrip corta os espaços da direita
# lstrip corta os espaços da esquerda

print()

for i, frase in enumerate(lista_palavra):
    lista_nova.append(lista_palavra[i].strip())

print()
print(lista_nova)

# join = une string
frase_unida = "-".join(lista_palavra)
print(frase_unida)
# >> Tamo aí-   sempre na atividade   
# o join uniu meus dois iteráveis e separou por um -

# usanddo o replace
meu_cpf = "471.555.555.55"
print(meu_cpf)
# >> 471.555.555.55

usei_replace = meu_cpf \
    .replace(".", "") \
    .replace("-", "")
# Estou retirando os caracteres . e - usando o método replace.

print(usei_replace)
# >> 47155555555

# método count
# O método count é um método para strings, ele conta a quantidade de um determinado caracter em uma string, e para isso ele recebe a variável seguido da chamada do método e um parâmetro, ou seja, o caracter que se deseja contar. 
print("Quantas vezes o caracter 5 aparece ? : ", usei_replace.count("5"),"X")
# >> Quantas vezes o caracter 5 aparece ? :  8 X