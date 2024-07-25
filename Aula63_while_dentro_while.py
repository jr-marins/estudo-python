'''
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
'''

qnt_linha = 5
qnt_coluna = 5

linha = 1

while linha <= qnt_linha:
    
    coluna = 1 
    while coluna <= qnt_coluna:
        print(f"linha={linha}, coluna={coluna}")
        coluna += 1
    
    linha += 1

'''
linha vai continuar sendo 1 até que op while mais interno seja executado por completo,
após o while mais interno for completado a linha passa a ser 2 e assim entramos novamente 
no while interno.
''' 