'''
Calculadora com while
'''


while True:

# Pedir o primeiro numero para o usuário
    valor1 = input("Digite um número: ")

# pedir o segundo numero para o usuário
    valor2 = input("Digite um número: ")
    
    operador = input("insira a operação desejada: ")
    operadores_validos = "+-*/"

# flag de numeros validos
    numeros_validos = None

    numero1_float = 0
    numero2_float = 0
# convertendo para float    
    try:
    
        numero1_float = float(valor1)
        numero2_float = float(valor2)
        numeros_validos = True
    except:
        numeros_validos = None

# Verificando se os valores inseridos são válidos
    if numeros_validos is None:
        print("Um ou ambos dos valores são inválidos !")
        continue

# Pedir qual a operação o usuárioquer fazer
    
    if operador not in operadores_validos:
        print("Você não digitou um operador válido. Tente novamente.")
        continue

# conferindo se o operador foi inserido corretamente
    if len(operador) > 1 :
        print("Você não pode inserir mais de um operador por vez.")
        continue

    if operador == "+":
        print(f"Adição = ", numero1_float + numero2_float)
    elif operador == "-":
        print(f"Subtração = ", numero1_float - numero2_float)
    elif operador == "*":
        print(f"Multiplicação = ", numero1_float * numero2_float)
    elif operador == "+":
        print(f"Divisão = ", numero1_float / numero2_float)

# Dar a opção para ousuário encerrar o loop
# Aceitar somente letras minusculas
# startswith confere se a primeira letra é 's'
    sair = input("Quer sair ? [s]im : ").lower().startswith("s")
    if sair is True:
        break