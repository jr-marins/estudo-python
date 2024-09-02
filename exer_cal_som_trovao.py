''' Neste projeto, você criará um programa que calcula a que distância, em pés, um ouvinte
está da queda de um relâmpago. O som viaja a aproximadamente 1.100 pés por
segundo pelo ar. Logo, conhecer o intervalo entre o momento em que você viu um
relâmpago e o momento em que o som o alcançou lhe permi�rá calcular a distância do
relâmpago. '''

# O som viaja pelo espaço em velocidade de 1.100

# Entrada de tempo pelo usuário

tempo = float(input("Insira o o tempo : \n"))
velocidade = float(1.100)

distancia = velocidade * tempo

print(f"A distância em pés em que o ouvinte está da queda do trovão é de : {distancia:.2f} pés.")