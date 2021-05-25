#1.	Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.


def valor(a,b,c):
    soma = a + b + c
    return soma
a = int(input('Infome o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))

print('A soma dos valores informados é: ', valor (a,b,c))