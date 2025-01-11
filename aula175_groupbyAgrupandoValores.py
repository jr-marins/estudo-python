'''
Groupby - agrupando valores (itertools)
'''
from itertools import groupby

alunos = [
    {'nome': 'marcos', 'nota': 'A'},
    {'nome': 'marisn', 'nota': 'B'},
    {'nome': 'joana', 'nota': 'A'},
    {'nome': 'lucio', 'nota': 'C'},
    {'nome': 'junior', 'nota': 'D'},
    {'nome': 'francine', 'nota': 'A'},
    {'nome': 'leandro', 'nota': 'B'},
    {'nome': 'carla', 'nota': 'A'},
    {'nome': 'denise', 'nota': 'C'},
    {'nome': 'leticia', 'nota': 'D'},
]

# devemos tratar os dados antes de agrupa-los e ordenados
# ordenando os dicionários internos da lista pela nota
# criando a funcao que ordena
def ordena(aluno):
    return aluno['nota']

alunosAgrupados = sorted(alunos, key=ordena)
# conferindo a ordenação
# for aluno in alunosAgrupados:
#     print(aluno)

grupos = groupby(alunosAgrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    
    for aluno in grupo:
        print(aluno)
    

