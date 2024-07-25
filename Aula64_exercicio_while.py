# você dev iterar uma string com while

nome = "marcos"
cnt_str = 0
novo_nome = " "

while cnt_str < len(nome):
    letra = nome[cnt_str]
    novo_nome += f"*{letra}"

    cnt_str += 1
print(novo_nome)
