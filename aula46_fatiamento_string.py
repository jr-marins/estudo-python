"""
 Fatiamento de string
  Fatiamento [inicio:fim:passo]
  obs: a função "len" retorna a quantidade 
  de caracters da str ou qualquer outro objeto.
"""

# EX:
nome = "Me chamo Marcos Marins"

nome1 = nome[5:9:2] # aqui eu passo inicio, final e o passo

nome2 = nome[-1:0:-2]# se o passo for um valor negativo ele irá iniciar de traz para frente.

print(len(nome)) # Aqui eu confiro quantos caracters tenho na minha variavel e os epaças tbm contam.

print(nome1)
#  --> ao 

print(nome2)
# --> sia orMoace