'''Faça um programa que peça ao usuário digitar um número inteiro,
informe se este numro é ímpar ou par. Caso o usuário não digite um
númenro inteiro, informe que não é um número inteiro.'''

#pedindo para o usuário inserir um valor
nmr_entrada = input("Digite uma valor: ")

try:
    entrada_int = int(nmr_entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_txt = "ímpar"

    if par_impar:
        par_impar_txt = "par"

    print(f"O numero {nmr_entrada} é {par_impar_txt}")
except:
    print("Você não digitou um número inteiro.")


'''
Faça um programa que pegunte a hora ao usuário e, basseado no horario 
descrito, exiba a saudação apropriada. EX:
Bom dia 0-11, Boa tarde 12-17 e boa noite 18-23
'''

ent_usuario = input("Insira um horario: ")

try:
    hora = int(ent_usuario)

    if hora >= 0 and hora <= 11:
        print("Bom dia !")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde !")
    elif hora >= 18 and hora <= 0:
        print("Boa noite !")
    else:
        pirnt("Não conheço esta hora.")
except:
    print("Você não digitou um número inteiro.")


'''
faça um programa que peça ao usuário o seu primeiro nome. se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; se tiver entre 5 e  6 "seu nome é normal";
maior que 6 "seu nome é grande".
'''
nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome <=4:
    print("Seu nome é curto.")
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é grande.")