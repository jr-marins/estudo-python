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