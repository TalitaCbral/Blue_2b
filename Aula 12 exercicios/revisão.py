#Revisão de Função 
def calc(a, b, operador):
    print('O primeiro numero é:', a)
    print(f'O segundo numero é: {b}')
    if operador == '+':
        resultado = a + b
        print('O resultado dos dois numeros com o operador escolhido é: ', resultado)
    elif operador == '-':
        resultado = a - b
        print('O resultado dos dois numeros com o operador escolhido é: ', resultado)
    elif operador == '*':
        resultado = a * b
        print('O resultado dos dois numeros com o operador escolhido é: ', resultado)
    elif operador == '/':
        resultado = a / b
        print('O resultado dos dois numeros com o operador escolhido é: ', resultado)
    else:
        print('Ops, esse operador não é valido!') 
    


n1 = float(input('Informe o número: '))
n2 = float(input('Informe outro número: '))
op = input('Digite o operador: +, -, * ou /: ')
calc(n1, n2, op)
