'''
REVENDO : 

Listas dentro de listas

explicação -

quando temos listas dentro de lista(iteráveis dentro de iteráveis), temos 
os índices das listas internas e o índice dos elementos internos de dentro das listas = [] []
EX:

'''
salas = [
    # 0         1
    ["Marcos", "Ana Caroline", ], # 0 
    # 0
    ["Andressa", ], # 1
    # 0 
    ["Jonatas", "João", "Emanuel", (10, 20, 30, 40)], # 2
]

print(salas[2][3][1])

# >> 20 Indice de minha tupla dentro da minha lista.

# >> Jonatas

'''
Aqui acessamos a lista do indice 2 e passamos o índice que queremos acessar da lista 2, que é o nome "jonatas"
'''
# Agora faremos um for 

for sala in salas:
    print(f"A sala é {sala}\n")
    for aluno in sala:
        print(aluno)
# >> A sala é ['Marcos', 'Ana Caroline']
# Marcos
# Ana Caroline
# A sala é ['Andressa']
# Andressa
# A sala é ['Jonatas', 'João', 'Emanuel', (10, 20, 30, 40)]
# Jonatas
# João
# Emanuel
# (10, 20, 30, 40)