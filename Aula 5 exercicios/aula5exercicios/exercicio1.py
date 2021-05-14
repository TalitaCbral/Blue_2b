#Exercício 1: "Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles."

num1 = int(input('Digite o primeiro número: '))
num2= int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

maior = num1

if num2 > num1:
  maior = num2
if num3 > num2:
  maior = num3
print('Maior: ', maior)

menor = num1 
 
if num2 < num1: 
  menor = num2 
if num3 < num2:
  menor = num3 
print('Menor: ', menor)