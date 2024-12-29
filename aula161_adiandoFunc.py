"""
Adiando funções com clouser
"""

def criaFunc(func, x):
    def interna(y):
        return func(x, y)
    return interna

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

somar = criaFunc(soma, 10)
print(somar(5))

multiplicar = criaFunc(multiplica, 10)

print(multiplicar(15))
