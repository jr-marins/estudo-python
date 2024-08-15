'''
args - argumentos não nomeados

* - *args (empacotamento e desempacotamento)
'''

def soma(*args):
    # crio um controlador, para armazenar os valores que são iterados
    total = 0 

    # para cada numero em args
    for numero in args:
        # some-o com o proximo e guarde o valor no meu controlador.
        total = total + numero
        # só para conferir o valor de cada iteração
        print("total", total)
    print()
    # imprimir o valor total.
    print(total)

    # Retornar o valor total para possível reutilização no futuro
    return total

# Passando os argumetos e armazenando o resultado em uma variavel.
total1 = soma(1, 2, 3, 4, 5, 6)

# acessando o valor armazenado na variável. 
print(total1)


