#DESAFIO - As empresas @.com resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
'''Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

• salários até R$ 280,00 (incluindo) : aumento de 20%

• salários entre R 280,00eR  700,00 : aumento de 15%

• salários entre R 700,00eR  1500,00 : aumento de 10%

• salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:

• o salário antes do reajuste;

• o percentual de aumento aplicado;

• o valor do aumento;

• o novo salário, após o aumento."'''

#Parte 1 

salario = float(input('Salario do colaborador: '))
if salario <= 280.00:
  percentual = 20
elif salario >= 280.00 and salario <= 700.00:
  percentual = 15
elif salario >=700.01 and salario <= 1500.00:
  percentual = 10
else:
  percentual = 5

print('Salario original do Colaborador: R$ ', salario)
print('Percentual: ', percentual, '%')

percentual = percentual/100.0
aumento = percentual * salario
salario_reajustado = salario + aumento

print('Aumento: R$', aumento)
print('Salário Reajustado em: R$', salario_reajustado)

#Parte 2
salario = float(input('Salario do colaborador: '))
print('Salario original do Colaborador antes do aumento: R$ ', salario)

if salario <= 280.00:
  percentual = 20
elif salario >= 280.00 and salario <= 700.00:
  percentual = 15
elif salario >=700.01 and salario <= 1500.00:
  percentual = 10
else:
  percentual = 5
print('Percentual de Aumento: ', percentual, '%')

percentual = percentual/100.0
aumento = percentual * salario
salario_reajustado = salario + aumento

print('O valor do aumento é: R$', aumento)
print('Novo salario após o aumento: R$', salario_reajustado)