'''
Closure e funções que retornam outra função

Uma closure em Python é uma maneira de criar funções que podem se lembrar de variáveis e do ambiente onde foram criadas, mesmo depois que a função externa termina. Isso é útil para manter um "estado" ou para encapsular um comportamento com dados específicos, como no exemplo acima.

'''

def saudacao_generica(saudacao):

    def saudacao_especifica(nome):
        return f"{saudacao} {nome}"
    
    return saudacao_especifica

bom_dia = saudacao_generica("Bom dia")

boa_noite = saudacao_generica("boa noite")

# print(bom_dia("marcos"))
# print(boa_noite("Junior"))

for nome in ['marcos', "junior"]:
    print(boa_noite(nome))
    print( bom_dia(nome))


