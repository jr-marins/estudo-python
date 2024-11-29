# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

set1 = {'marcos', 1, 2, 3}  # com dados
#for em sets
for numero in set1:
    print(numero, "\n")

# Métodos úteis:
# add, update, clear, discard
set1.add("marins")

set1.update(('sets',)) 
print(set1)

set1.discard('sets')
print(set1)
print()

# Operadores úteis:
set2 = {1, 2, 3}
set3 = {2, 3, 4}

# união | união (union) - Une
set4 = set2 | set3
print(set4) #{1, 2, 3, 4}

# intersecção & (intersection) - Itens presentes em ambos
set4 = set2 & set3
print(set4) #{1, 2, 3, 4}

# diferença - Itens presentes apenas no set da esquerda
set4 = set2 - set3 
print(set4) #[1]

# diferença simétrica ^ - Itens que não estão em ambos
set4 = set2 ^ set3
print(set4) #{1, 4}

# Exemplo de uso

letras = set()
while True:
    letra = input("Digite: ")
    letras.add(letra)

    if 'l' in letras:
        print("parabens")

    print(letras)