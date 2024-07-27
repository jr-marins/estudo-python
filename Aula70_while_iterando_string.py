'''
Irei criar uma frase e usando while, atrvés da iteração,
vamos contar as letras da frase e calcular a ocorrência de cada uma.
Assim, retornando a que mais aparece.

Para isso usaremos um método chamado de Count
'''

frase = "Python é uma linguagem de programação"\
"multiparadigma"\
"python foi crido por Guido van Rossun."

i = 0

qnt_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ""

while i < len(frase):

    letra_atual = frase[i]

    if letra_atual == " " :
        i += 1
        continue

    qnt_atual = frase.count(letra_atual)

    if qnt_apareceu_mais_vezes <= qnt_atual :
        qnt_apareceu_mais_vezes = qnt_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1

print(f"a letra que mais apareceu foi : {letra_apareceu_mais_vezes}, e apareceu > {qnt_apareceu_mais_vezes} vezes ")
print(letra_apareceu_mais_vezes)