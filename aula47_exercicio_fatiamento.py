# EXERCÍCIO

# Peça para o usuário digitar seu nome
nome = input("Digite seu nome: ")
# Peça para o usuário digitar sua idade
idade = input("Qual a sua idade? ")
# Se o nome e idade for digitados:

def nome_invertido(nome):
    return print(f"Seu nome invertido é {nome[::-1]}")

if nome and idade:
#       Exiba:
#           Seu nome é
    print(f"Seu nome é {nome}")

#           Seu nome invertido é(criei uma função na linha 9 que recebe como paremetro um nome e o inverte)
    nome_invertido(nome)

#           Seu nome contem espaços ou não
    if " " in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")

#           Seu nome tem N letras
    print(f"Seu nome tem {len(nome)} letras !")

#           A primeira letra do seu nome é
    print(f"A primeira letra do seu nome é {nome[0]}") #Quando quero um item específico eu passo somente seu indice

#           A última é
    print(f"A ultima letra é {nome[-1]}")  #Quando quero um item e não qnts tem no total, eu passo o negativo para começar do final.
# se nada for digitado exiba " desculpa, você deixou campos vazios"
else:
    print(" Desculpa, você deixou campos vazios ".upper()) #Usei o método upper direto no print para converter em maiúscula

 
