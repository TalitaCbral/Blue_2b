#2.	 Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
#  se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def pn(n):
    if n > 0:
        print('P')
    elif n == 0:
        print('0')
    else:
        print('0')
n = int(input('Informe um numero inteiro:'))
print('Este número é: ', end=' ')
pn(n)