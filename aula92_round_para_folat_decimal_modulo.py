'''
Round = formata numeros de preferência float

ao invés de usar f'string, usamos round
- o f'styring retorna uma string e round retorna oque realmente queremos, um float.

'''

numero_1 = 0.1
numero_2 = 0.7

numero_3 = numero_1 + numero_2

print(numero_3)
# >> 0.7999999999999999
print(f"{numero_3:.2f}, ", type(numero_3))
# >> 0.80,  <class 'float'>
print(round(numero_3, 2), type(numero_3))
# >> 0.8 <class 'float'> round arredonda as casas decimais

print()
'''
Modulo Decimal

'''
import decimal

numero_4 = decimal.Decimal(0.1)
numero_5 = decimal.Decimal(0.7)
numero_6 = numero_4 + numero_5

print(f"{numero_6:.2f}")
# >> 0.80 mesmo com f'string ele retorna um float
