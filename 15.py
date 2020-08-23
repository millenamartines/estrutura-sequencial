'''
Imposto de Renda = - 11%
INSS = - 8%
Sindicato = -5%
'''

sal = float(input('Quanto você ganha por hora? R$'))
horas = float(input('Número de horas trabalhadas: '))
tot = sal * horas
inss = tot * (15 / 100)
sind = tot * (5 / 100)
ir = tot * (11 / 100)
descs = inss + sind + ir

print('-' * 30)
print(f'Salário Bruto: R${(tot + descs):.2f}')
print(f'Descontos: {descs:.2f}')
print(f'IR: R${ir:.2f}')
print(f'INSS R${inss:.2f}')
print(f'Sindicato: R${sind:.2f}')
print('-' * 30)
print(f'Salário Líquido: R${tot:.2f}')
print('-' * 30)
