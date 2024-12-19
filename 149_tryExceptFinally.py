# Try, except, else e Finally

a= 18
b= 0
c = 'a'

try:
    divide = a / b
    maisStr = b - c
except ZeroDivisionError as erro:
    print("cheguei aqui\n", erro)

except TypeError as erro:
    print("str não faz operação:\n",erro)

except NameError as erro:
    print("parametro(variável) não definida.\n", erro)

######################### Parte 2 ##############################

d= 18
e= 0
f = 'a'

'''
tratando erros nomeados e a Exception que engloba qualquer erro em python.
'''

try:
    divide = d / e
    maisStr = e - f
except ZeroDivisionError as erro:
    print("cheguei aqui\n", erro)

except (TypeError, IndexError) as erro:
    print("TypeError + IndexError:\n",erro)

    # para ver o nome do erro...
    print("Nome: ", erro.__class__.__name__)

except NameError as erro:
    print("parametro(variável) não definida.\n", erro)

except Exception:
    print("Erro desconhecido.")

############ Parte 3 ############

# >> finally : bloco que sempre será executado, sempre.
# bloco finally para fializar o try except. 
"""
Ex: 
ao processar um aquivo, caso ao abri-lo dê um erro, vc deve fecha-lo. o finally é responsável por essa operação. 
"""

g = 18
h = 0
i = 'a'

try:
    # divide = g / h
    # maisStr = g - i
    # na = b + l
except ZeroDivisionError as erro:
    print("cheguei aqui\n", erro)

except (TypeError, IndexError) as erro:
    print("TypeError + IndexError:\n",erro)

    # para ver o nome do erro...
    print("Nome: ", erro.__class__.__name__)

except NameError as erro:
    print("parametro(variável) não definida.\n", erro)

except Exception:
    print("Erro desconhecido.")

finally:
    print("Sempre vou ser executado!")