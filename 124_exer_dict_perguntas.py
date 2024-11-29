'''
    Crie um algoritmo em que use uma lista de dicionários,
    contendo perguntas e respostas. Objetivo, criar um jogo de perguntas e respostas
'''

# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

#acumulador de acertos
qtd_acerto = 0

# iterando sobre a lista, pegando as perguntas do dicionários
for pergunta in perguntas:
    print('Pergunta', pergunta['Pergunta']) #passo a chave 'pergunta'
    print()
    
    opcoes = pergunta['Opções'] #opcoes guarda os valores contidos na chave opções

    for i, opcao in enumerate(opcoes): #exibir as opções e os índices
        print(f"{i})", opcao)    
    print()

    escolha = input("Escolha um opção:\n")

    escolha_int = None
    acertou = False
    qnt_opcoes = len(opcoes)

    if escolha.isdigit(): #digitou um numero ?
        escolha_int = int(escolha) # converta para int se possível

    if escolha_int is not None:

        #confere se a opção existe[indice]
        if escolha_int >= 0 and escolha_int < qnt_opcoes:

            #confere a resposta
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou=True
    #valida o acerto            
    if acertou:
        print("Acertou")
        qtd_acerto +=1
    else:
        print("Errou")


print("\nVocê acertou: ", qtd_acerto)
print("de", len(perguntas), 'perguntas.')