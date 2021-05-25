#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente
# além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para
# se aposentar.

from datetime import date

trab = {}

trab['nome'] = input('Seu nome é: ')
trab['nasc_ano'] = int(input('Você nasceu no ano de: '))
trab['CTPS'] = input('Número da sua CTPS: ')
trab['idade'] = date.today().year - trab['nasc_ano']

if trab['CTPS'] != '0':
    trab['contratacao'] = int(input('Ano de contratação: '))
    trab['salario'] = float(input('Valor do salário: R$ ')).replace(',','.')
    trab['aposent'] = 35 - (date.today().year - trab['conrtatacao'])
else:
    print('CTPS não cadastrada em nosso sistema! infelizmente não seguiremos com o programa')
print()
for key, values in trab.items():
    print(f'{key}: {values}')