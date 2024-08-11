'''
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja enviado
para o parâmetro, o valor padrão será usado.

Refatorar: editar o código
'''

def soma(x, y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=} ", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)

'''
 Explicando o if: se for passado um argumento para o paremetro z, exiba-o
Se não for passsado um argumento para o parametro z, não exiba-o.
O parametro z pode tbm ter o valor padrão como None:

if z is not None:
        print(f"{x=} {y=} {z=} ", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)
EXPLICANDO ::
 se z não for none, exiba-o

'''

soma(10, 10, 10)
# >> x=10 y=10 z=10  30

soma(10, 10) # Como o z tem valor padrão, mesmo eu não passando um argumento para o parâmetro o código não da erro.
# >> x=10 y=10 20

'''
OUTRA REGRA :

TDOO PARâMETRO VINDO DEPOIS DE UM PARâMETRO COM O ARGUMENTO PADRÃO,
É OBRIGATÓRIO QUE ESSES PARÂMETROS TAMBÉM SEJAM DEFINIDOS COM UM ARGUMENTO PADRÃO. EX:
    def soma(x, z=None, y=None):
O parâmetro z esta com um argumento padrão, sendo assim,
todos os parâmetros vindos deposi dele tbm terão que ter um
argumento padrão.
'''