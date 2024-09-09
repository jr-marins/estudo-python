'''
manipulando dicionário, crinado chave e valor para dicionário.
'''
# dicionário vazio
pessoa = {}

# criando chave e atribuindo um valor
pessoa["nome"] = "Marcos Marins"
pessoa["sobrenome"] = "Junior"

# imprimindo somente o valor da chave=nome
print(
    pessoa["nome"], 
    pessoa["sobrenome"]
    )

# imprimindo o dicionário completo
print(pessoa)

# excluindo uma chave
del pessoa["sobrenome"]
print("\n", pessoa)

## ALGUNS MÉTODOS PARA DICIONÁRIOS ##
# get tenta obter uma chave, se a chave não existir ele retorna none
# print(pessoa.get("sobrenome")) >> none

# usando o get para verificar a existência de chaves
if pessoa.get("sobrenome") is None:
    print("Chave não existe.")
else:
    print(pessoa["sobrenome"])
