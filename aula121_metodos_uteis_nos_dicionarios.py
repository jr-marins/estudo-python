
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

#len
print("Quantidade de chaves: ", len(pessoa)) 


#keys
print("As chaves do dicioonário são: ", list(pessoa.keys()))

# value
print("Os valores da chaves: ", list(pessoa.values()))

# item
print("Suas chaves e valores: ", list(pessoa.items()))

# setdefault insere um valor padrão quando a chave não existe
pessoa.setdefault('idade', 0)
print(pessoa['idade'])

# get
print(pessoa.get('nome'))

# pop
nome = pessoa.pop('nome')

# pop item
ultima_chave = pessoa.popitem()

# update
pessoa.update({
    'nome': 'novo',
    'idade': 30,
})

print()

# Iterando os valores do meu dicionário
print("Os valores das sua chaves são: ".upper())
for valor in pessoa.values():
    print(valor)

print()

print("Suas chaves e valores: ".upper())
for chave, valor in pessoa.items():
    print(chave, valor)