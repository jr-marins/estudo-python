'''
EXERCÍCIO:
Crie uma função que duplica, triplica e quadriplica um valor
'''

def duplica(valor):
    return valor * 2

def triplicar(valor):
    return valor * 3

def quaduplicar(valor):
    return valor * 4

dobro = duplica(6)
# print(dobro)
# ^^ modo mais extenso de se fazer

# agora usando os conceitos de closure, a solução fica assim ...

def _multiplicador(multiplicador): # Criando a função que cria o multiplicador
    def multiplicar(numero): # função que recebe o multiplicador
        return numero * multiplicador 
    return multiplicar # retornando a função, de forma adiada. sem que ela se precipite

duplicar = _multiplicador(2)
triplica = _multiplicador(3)
quaduplica = _multiplicador(4)

print(
    duplicar(1),
    triplica(2),
    quaduplica(3)
    ) # >> resultado: 2 6 12