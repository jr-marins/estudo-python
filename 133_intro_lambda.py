"""
A função lambda é uma função como qualquer outra
porém, são funções anonimas que contém apenas uma linha.
Ou seja tudo deve ser contido dentro de uma única expressão.

"""

lista = [
    {'nome': 'Marcos', 'sobrenome': 'Marins'},
    {'nome': 'Marco', 'sobrenome': 'Marins'},
    {'nome': 'emanuel', 'sobrenome': 'Marinss'},
    {'nome': 'joao', 'sobrenome': 'junior'},
]

# vamos criar um filtro usando lambda
def executa(funcao, *args):
    return funcao, *args


# lista.sort(key=lambda item: item) mexe diretamente na lista
l1 = sorted(lista, key=lambda item: item['nome']) # faz uma copia da lista original

print(l1)