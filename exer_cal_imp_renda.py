'''
Desafio: 
Criar um algoritmo que, com base em um salário, calcule
o valor que deverá ser descontado para o imposto de renda
'''

sal_base = float(input("Digite o salario base: \n"))
gratificacao = float(input("Digite a gratificação, caso não tenha inserira o valor zero: \n"))

sal_bruto = sal_base + gratificacao

imp_renda = sal_bruto * 0.20 if sal_bruto > 1.000 else sal_bruto * 0.15

sal_liquido = sal_bruto - imp_renda

print(f"O valor descontado para o imposto de renda é de : {imp_renda :.2f}. O salário líquido é de : {sal_liquido :.2f}")


