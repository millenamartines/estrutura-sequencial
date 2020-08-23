'''
a) homens:   (72.7 * altura) - 58
b) mulheres: (62.1 * altura) - 44
'''
alt = float(input('Qual a sua altura? '))
sexo = str(input('Qual o seu sexo? [M/F] '))

if sexo in 'Mm':
    peso = (72.7 * alt) - 58
    print(f'Seu peso ideal é {peso:.2f}Kg')
elif sexo in 'Ff':
    peso = (62.1 * alt) - 44
    print(f'Seu peso ideal é {peso:.2f}Kg')
else:
    print('Digito errado! Comece novamente!')

