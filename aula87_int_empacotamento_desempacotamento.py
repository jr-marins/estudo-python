'''
INTRODUÇÃO :

Empacotamento desemapcotamento

Dada a seguinte lista :

>> minha_lista = ["Marcos", "Desenvolvedor", "Arquiteto"]

Vamos supor que eu queira retirar esses valores de dentro da lsita e armazena-los em variáveis ... "Desempacotar a lista" ...

'''

minha_lista = ["Marcos", "Desenvolvedor", "Arquiteto"]

nome, funcao, profissao = minha_lista

print("\n", nome)
# >> Marcos
print("\n", funcao)
# >> Desenvolvedor
print("\n", profissao)
# >> Arquiteto

'''
Seguindo o a mesma lógica (Desempacotar), vamos supor que eu queira desempacotar somente o primeiro valor para uma variável. E oque acontece com o resto dos valores ? Veremos ...

'''

nova_lista = ["Marcos", 1998, 11, 11]

name, *dt_nasc = nova_lista # para armazenar o restante dos valores, eu uso um ( * ) antes da nova variável
print("\n", name)
# >> Marcos
print("\n", dt_nasc)
# >> [1998, 11, 11]

'''
#desempacotar somente o primeiro valor#
Isso ^ foi feito, mas agora, vamos supor que eu queira pegar um valor mais para o meio da lista, como fazer isso ??

'''

_, mes, _ = dt_nasc
print("\n", mes)
# >> 11

'''
Quando usamos o ( _ ) deixamos bem claro que os demais valores não serão ultilizados para absolutamente nada
''' 