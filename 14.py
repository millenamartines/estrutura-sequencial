peso = float(input('Qual o peso do produto em Kg? '))
print(f'O peso do produto é de {peso}Kg')
if peso > 50:
    print('\033[31mVocê excedeu o limite de 50kg!')
    multa = (peso - 50) * 4
    print(f'\033[31mDeverá pagar uma multa de R${multa:.2f}')
else:
    print(f'Está dentro limite.')
