'''
Criando um gerador de cpf com o random

'''
# importando o modulo 
import random

for _ in range(10):

    # crinaod a variavel para armazenar os digitos gerados
    nove_dg = ''

    for i in range(9):

    # gerando 1 digito a cada loop
        nove_dg += str(random.randint(0, 9))
    print("Digitos gerados: ", nove_dg)

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


    ##################### Segundo Exercicio ##########################

    '''
    Calcuando o segundo digito.
    '''
    # cpf2 = "61300646080"

    # pegando os 10 primeiros digitos
    dez_dg = nove_dg + str(digito1)

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

    print("Segundo digito: ", digito2)
    # concatenando os resultados os digitos gerados
    cpf_gerado = f"{nove_dg}{digito1}{digito2}"

    print("CPF Gerado: ", cpf_gerado)
    print()