class Pessoa:
    def __init__(self, nome, sobrenome, dtnascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dtnascimento = dtnascimento

class PessoaFisica(Pessoa):
    def __init__(self, cpf, rg):
        self.cpf = cpf
        self.rg = rg

p1 = Pessoa("marcos", "marins", "11/11/1998")
# print(p1.nome, p1.sobrenome, p1.dtnascimento)

print()

p2 = PessoaFisica("marcos", "xx.xx.xx", "yyy.yyy.yyy.")
print(p2.nome, p2.cpf, p2.rg)

