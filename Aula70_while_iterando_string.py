'''
Irei criar uma frase e usando while, atrvés da iteração,
vamos contar as letras da frase e calcular a ocorrência de cada uma.
Assim, retornando a que mais aparece.

Para isso usaremos um método chamado de Count
'''

# primeiro cria a frase
frase = input("Insira uma frase: \n")

#criando o controlador
i = 0

# as variaveis que armazenaram o valo final
qnt_da_letra_atual = 0
letra_que_mais_teve_ocorrencia_na_frase = ''

# enquanto o i for menor que o tamanho da frase
while i < len(frase): 

# pegando a letra atual em que o python está neste momento.
    letra_atual = frase[i]

# Ignorando espaços
    if letra_atual == " ":
        i+=1
        continue
    
# criando uma variavel que conte a ocorrencia da letra atual na frase toda
    qnt_letra_atual_na_frase = frase.count(letra_atual)

# trabalhando os dados
    # o if faz a comparação com a qnt atual que está fora do loop, que neste caso aindo é 0, e o loop ja começou sendo assim a qnt letra atual na frase é maior que a qnt atual 0, e quando o python voltar neste trecho de código ele irá comparar a qnt da letra atual na frase com a quantidade atual que foi armazenado do loop anterior. se a qnt atual(que ele armezenou do ultimo loop) for menor que a qnt da letra atual na frase(do loop atual), ele ira entrar no bloco if para alterar os valores das variáveis.

    if qnt_da_letra_atual <= qnt_letra_atual_na_frase:

        # sendo a qnt atual menor que a quantidade da letra atual da frase, a qnt atual passa a ter o valor da qnt da letra atual na frase, pois a letra atual aparece mais que a anterior
        qnt_da_letra_atual = qnt_letra_atual_na_frase
        
        # a letra que será armazenada na variavel (letra que mais teve ocorrencia), é a letra que deu a origem a ultima modificação do valor da variavel qnt atual. 
        letra_que_mais_teve_ocorrencia_na_frase = letra_atual
    i+=1

print(
    f"A letra que mais apareceu foi ({letra_que_mais_teve_ocorrencia_na_frase.upper()}) e aparece : ({qnt_da_letra_atual})X"
    )