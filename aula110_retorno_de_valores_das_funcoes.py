'''
Aula :
retornando valores de funções(retunr)
'''


# digamos que eu queira criar uma função que some dois valores ...
def somar(a, b):
    print(a + b)

somar(10, 10)
# ok ! função criada e soma realizada
# >> 20

# mais agora digamos que eu queira armazenar esse valor, ou a cada execução e somas realizadas pela função, eu deseja guardar os resultados em variáveis para usar futuramente.

resutado1 = somar(10, 10)
resultado2 = somar(20, 20)
# armazenei os resultados, mais tem um porem. a minha função não retorna nada ! 
print(resutado1) # pela função não retornar nada eu não consigo usar os valores, e o resultado vai ser None(typeNone)
# >> None

print()

# pra isso usamos o return, para retornar os valores e disponibilizar para uso.

def somar_e_retornar(x, y):
    return x + y

# agora sim posso usar esses valores, pois a minha função retorna um valor.
vlr_retornado1 = somar_e_retornar(10, 10)
vlr_retornado2 = somar_e_retornar(20, 20)

print(vlr_retornado1 + vlr_retornado2)
# >> 60