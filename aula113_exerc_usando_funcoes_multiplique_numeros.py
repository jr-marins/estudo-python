'''
Exercício com funções:
1 >> Crie uma função que multiplique todos os valores 
não nomeados recebidos

2 >> Crie uma função que fala se um número é par ou ímpar
'''

# criando uma função que receba argumentos não nomeados

def multiplicar(*args):
# recebendo e trabalhando os valores

    total = 1

    for valor in args:
# armazenando o valor de cada multiplicação e somando com o valor guardado a cada iteração
        total *= valor

    return total

    
resultado = multiplicar(2, 3, 4, 5)

print("a soma da multipicação é ", resultado)
print(2 * 3 * 4 * 5) # conferindo o valor

print()

# criando uma função que recebe uma argumento não nomeado
def confere(numero1):
# trabalhando o valor com base em condições
# Usei um if ternário para simplificar o código
    par_impar = "é PAR" if numero1 %2 == 0 else "é ÍMPAR"
    
    return f"O valor > {numero1}, {par_impar}"

qual_e = confere(5)

print(qual_e)

print()

'''
Outra forma de ser resolvido, tratando uma simples exceção de valor...

método: Try-Except
'''

def qual_e(numero2):

    try:
        numero2 = int(numero2)
          
        if type(numero2) is int:

            par_impar = "PAR" if numero2 %2 == 0 else "ÍMPAR"
    
    except ValueError:
        return "Please, insert a int value and try again...."
        
    return f"O {numero2}, é {par_impar}"

valor = qual_e("a")
print(valor)
# >> Please, insert a int value and try again....