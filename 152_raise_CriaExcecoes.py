"""
Raise = lançando exceções (erros)
"""

def divide(n, d):
    if d == 0:
        raise ZeroDivisionError("Não pode dividir por zero!")
    return n/ d
print(divide(8, 0))