'''
a) o produto do dobro do primeiro com metade do segundo
b) a soma do triplo do primeiro com o terceiro
c) o terceiro elevado ao cubo
'''

int1 = int(input('Digite um número inteiro: '))
int2 = int(input('Digite outro número inteiro: '))
real = float(input('Digite um número real: '))
a = (int1 * 2) + (int2 / 2)
b = (int1 * 3) + real
c = real ** 3

print(f'O Cálculo do exercício a = {a}')
print(f'O Cálculo do exercício b = {b}')
print(f'O Cálculo do exercício c = {c:.2f}')
