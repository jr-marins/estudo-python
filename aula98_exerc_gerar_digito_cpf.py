'''
cpf :    746.824.890 - 70

- colete a soma dos 9 primeiros digítos do cpf
multiplicando cada um dos valores por uma contagem regressiva
começando por 10.

Ex:  746.824.890 - 70 (47682489070)
     10 9 8 7 6 5 4 3 2
   *  7 4 6 8 2 4 8 9 0   
   = 70 36 48 56 12 20 32 27 0

somar todos os resltados: 

multiplicar o resultado anterior por 10
301*10 = 3010

Obter resultado o resto da divisão da conta interior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    o resultado é 0 else = resultado

O primeiro digito é : 7

'''
cpf = "74682489070"

# Fatiando para pegar apenas os nove primeiro digitos
nove_dg = cpf[:9]
# conatador regressivo para somar
contador_regressivo1 = 10

# para guardar os digitos multiplicado por 10
resultado_dg1 = 0

for digito1 in nove_dg:
    # o cpf ta em str, temos que converter para int, e multiplicalo pelo contador regressivo 
    resultado_dg1 += int(digito1) * contador_regressivo1
    # print(resultado)
    contador_regressivo1 -= 1 # dizendo que o contador é para ser de 10 a 0

# somando o resultado da iteração da soma dos digitos por 10 e pegando o resto da divisão
digito1 = (resultado_dg1 * 10) % 11
# conferindo se o resto da divisão é <= a 9
digito1 = digito1 if digito1 <= 9 else 0
print("Primeiro digito : ", digito1)
# >> Primeiro digito :  7

print()

##################### Segundo Exercicio ##########################

'''
Calcuando o segundo digito.
'''
cpf2 = "74682489070"
# cpf2 = "61300646080"

# pegando os 10 primeiros digitos
dez_dg = cpf2[:10]

# aumentando + 1 no contador
contador = 11

# crinado a variavel que vai armazenar os resultados
resultado_dg2 = 0

for digito2 in dez_dg:
# Guaradndo os resultados já calcuados pelo contador
    resultado_dg2 += int(digito2) * contador

# Decrementando o contador
    contador -= 1

# somando cada resultado e pegando o resto da divisão
digito2 = (resultado_dg2 * 10) % 11

# usando if ternário para dar a condição que resultara no segundo digito
digito2 = digito2 if digito2 <= 9 else "é maior"
print(digito2)