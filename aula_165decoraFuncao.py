
# função que recebe uma função
def criaFuncao(func):
    # função interna que recebe argumentos
    def interna(*args, **kwargs):
        print("Vou decorar")
        for arg in args:
            # a função ESTRING recebe os argumentos
            estring(arg)

        # o resultado é a função passada como parâmetro e os argumentos são passados para a função que foi passada como parâmetro.
        resultado = func(*args, **kwargs)

        print(f"O seu resultado foi {resultado}.")
        print("Ok. agora vc foi decorada")
        return resultado
    return interna

def invertString(string):
    return string[::-1]

def estring(param):
    if not isinstance(param, str):
        raise TypeError("param deve ser uma string")
    

invertString_checandoParam = criaFuncao(invertString)
invertida = invertString_checandoParam(123)
print(invertida)
