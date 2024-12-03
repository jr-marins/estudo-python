"""
A função lambda é uma função como qualquer outra
porém, são funções anonimas que contém apenas uma linha.
Ou seja tudo deve ser contido dentro de uma única expressão.

"""

lista = [
    {'nome': 'Marcos', 'sobrenome': 'Marins'},
    {'nome': 'ana', 'sobrenome': 'Marins'},
    {'nome': 'emanuel', 'sobrenome': 'Marinss'},
    {'nome': 'joao', 'sobrenome': 'junior'},
]

# lista.sort(key=lambda item: item) mexe diretamente na lista
l1 = sorted(lista, key=lambda item: item['nome']) # faz uma copia da lista original
for item in l1:
    print(item)

# funçãço que recebe uma função e a executa
def executa(func, *args):
    return func(*args)

print(
    executa(
        lambda x, y: x + y, 10, 5
    )
)