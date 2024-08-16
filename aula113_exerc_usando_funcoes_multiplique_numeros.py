'''
Exercício com funções:
1 >> Crie uma função que multiplique todos os valores 
não nomeados recebidos

2 >> Crie uma função que fala se um número é par ou ímpar
'''

# criando uma função que receba argumentos não nomeados

def multiplicar(*args):
# recebendo e trabalhando os valores

    total = 0

    for valor in args:
# armazenando o valor de cada multiplicação e somando com o valor guardado a cada iteração
        total += valor * valor

    return total

    
resultado = multiplicar(2, 3, 4, 5)

print("a soma da multipicação é ", resultado)


# criando uma função que recebe uma argumento não nomeado
def confere(numero):
# trabalhando o valor com base em condições
# Usei um if ternário para simplificar o código
    par_impar = "é PAR" if numero %2 == 0 else "é ÍMPAR"
    
    return f"O valor > {numero}, {par_impar}"

qual_e = confere(5)

print(qual_e)