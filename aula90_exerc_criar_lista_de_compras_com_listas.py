'''
EXERCÍCIO :

- Faça uma lista de compras com lista;

- O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista;

- Não permitir que o programa quebre com erros de índices
inexistentes.

'''

# criando a lista
lista_compras = []




while True:
# Dando as opções de ação para o usuário
    opcao = input("Escolha a opção desejada: [1]Adicionar ítem, [2]Apagar ítem, [3]Listar ítens \n > ")

# Checando se a entrada do usuário está correta
    if len(opcao) > 1: 
        print("ERRO ! Você só pode efetuar uma ação por vez. Tente novamente\n")
        continue

# Conferindo opção
    if opcao == "1": 
        item = input("Qual ítem deseja inserir na lista ? \n > ")
        # Adicionando item
        lista_compras.append(item)
        continue
    
    elif opcao == "2":
        # pegando o indice para que seja apagado
        valor = input("escolha o indice para apagar: \n >")
        #tratamento de exceções
        try:
            indice = int(valor) # convertendo para int
            del lista_compras[indice] # apagando
            print("Item apagado")
        except ValueError:
            print("\nPor favor digite um numro inteiro.\n")
        except IndexError:
            print("Por favor digite um índice válido\n")
        except Exception:
            print("Erro desconhecio\n") 
        
    
    elif opcao == "3":
        if len(lista_compras) == 0: # se lista estiver vazia
            print("Nada para mostar\n")
        for indice, produto in enumerate(lista_compras): # criando os índices com enumerate

            print(f"Sua lista contem :\n {indice, produto}")
        continue
    
    else:
        print("\nVocê não digitou uma opção correta, tente novamente.\n")
        continue