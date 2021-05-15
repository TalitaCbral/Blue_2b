#Exercício 2 - Faça um programa que peça dois números e imprima o maior deles

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

maior = num1

if num2 > num1:
  maior = num2
print('maior: ', maior)