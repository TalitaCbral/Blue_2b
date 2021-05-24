##01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:

   # A soma deles;

   # A multiplicação entre eles;

   # A divisão inteira deles;

   # Mostre na tela qual é o maior;

   # Verifique se o resultado da soma
   #  é par ou impar e mostre na tela;

   # Se a multiplicação entre eles for maior que 40,
   #  divida pelo resultado da divisão inteira e mostre
   #  o resultado na tela. Se não, mostre que a multiplicação
   #  não foi maior que 40.

def maior (num1, num2):
    if num1 > num2:
        print('O maior valor é:', num1)
    elif num2 > num1:
        print('O maior valor é:', num2)
num1 = int(input('Digite num1: '))
num2 = int(input('Digite num2: '))
soma = num1 + num2
print('A soma entre eles é:', soma)
mult = num1 * num2
print('Multiplicando eles temos:', mult)
divisao = num1 // num2
print('A divisão deles é:', divisao)
maior (num1, num2)
# > que 40 :

if mult > 40:
    mult_div = mult // divisao
    print(f'O número {mult} dividido por {divisao} é: {mult_div}')
else:
    print(f'A multiplicação dos numeros {num1} e {num2} é menor que 40!')

#impar ou par 
if soma % 2 == 0:
    print(f'A soma dos números é: {soma}, o resultado é par!')
else:
    print(f'A soma dos números é: {soma}, o resultado é impar!')
