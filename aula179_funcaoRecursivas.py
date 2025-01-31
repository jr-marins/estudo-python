'''
Funções recursivas e recursividade

- funções que podem se chamar de volta,
útel p/ dividir problemas grandes em partes menores.
- Um caso recursivo que resolve o pequeno problema
- Um caso base que para a recursão

# fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

'''

def recursiva(inicio=0, fim=10):
    # caso base
    if inicio >= fim:
        return fim
    
    print(inicio, fim, sep='-')
    # Caso recursivo
    # contar até chegar ao fim

    inicio += 1 
    return recursiva(inicio, fim)

# print(recursiva())

# recursiva resolvendo um problema

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))