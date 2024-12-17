'''
isinstance = Para saber se objeto é de determinado tipo

'''

lista = [
    'a', 1, 1.1, True, [0, 2, 1], 
    (1, 2), {0,1}, {'nome': 'Marcos'},
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        # conferindo os set's que tem. 
        print(item, isinstance(item, set)) 