'''
Operação ternária = (Condicional de uma linha)
<valor> if <condição> else < outro valor>

'''

condicao = 10 == 10
variavel = 'valor' if condicao else 'outro valor'
# variável for igual "valor" condição verdadeira, senão ela tem "outro valor"
print(variavel)

###


# se meu digito for igual menor ou igual a 9, digito é == a digito senão, é 0
digito = 10
novo_digito = digito if digito <= 9 else 0
#invertido agr. meu novo digito é = 0 se digito for maior que 9, senão continua sendo 9.
novo_dg = 0 if digito > 9 else digito
print(novo_digito)
print(novo_dg)

