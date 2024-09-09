
# Métodos úteis dos dicionários em Python #

# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

##############################################

pessoa = {
    'nome': 'Marcos Marins',
    'sobrenome': 'Junior',
    'idade': 26,
}

# setdefault insere um valor padrão quando a chave não existe
pessoa.setdefault('idade', 0)
print(pessoa['idade'])

print("Quantidade de chaves: ", len(pessoa)) 

print("As chaves do dicioonário são: ", list(pessoa.keys()))

print("Os valores da chaves: ", list(pessoa.values()))

print("Suas chaves e valores: ", list(pessoa.items()))

print()

# Iterando os valores do meu dicionário
print("Os valores das sua chaves são: ".upper())
for valor in pessoa.values():
    print(valor)

print()

print("Suas chaves e valores: ".upper())
for chave, valor in pessoa.items():
    print(chave, valor)