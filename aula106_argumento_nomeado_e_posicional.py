'''
Argumentos nomeados e não nomeados em funções
Argumento nomeado tem o nome com o sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

'''

# na definição da função vai os parametros
# na chamada da função eu passo os argumento (valores)
def soma(x, y):
    print(f"{x=} {y=} # x+y ", x+y)

soma(3,2) # passando os argumentos de forma posicional, pois a ordem é x e y então 3 vai para x e 2 para y
# >> x=3 y=2 # x+y  5

soma(y=5, x=3) # usando os parametros nomeado para passar os arguemntos(valores)
# >> x=3 y=5 # x+y  8


'''
Supondo que eu tenho tres parametros na minha função, x, y, z
e ao chamar a fnção eu desejo chamar a função com parametros nomeado (x=, y=, z=)
mais eu quero chamar só o y= :
soma(2, y=4, ...) uma regra é que apartir do momento que eu coloquei um argumento nomeado,
todos os argumentos que vierem depois desse argumento são obrigatorio qe tbm seja nomeado :
soma(2, y=4, z=2) é obrigatório nomear os argumentos seguintes.

'''