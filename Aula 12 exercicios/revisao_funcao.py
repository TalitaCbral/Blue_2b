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

#versão 2 (outra solução)

def calc2(a, b, operador):
    print('O primeiro numero é:', a)
    print(f'O segundo numero é: {b}')
    if operador in "+-*/":
        if operador == '+':
            resultado = a + b
        elif operador == '-':
            resultado = a - b
        elif operador == '*':
            resultado = a * b
        elif operador == '/':
            resultado = a / b
        print('O resultado dos dois numeros com o operador escolhido é:', resultado)
    else:
        print('Ops, esse operador não é valido!') 
    return resultado
# exit: nem sempre recomendando, sai do programa em caso de erro

n1 = float(input('Informe o número: '))
n2 = float(input('Informe outro número: '))
op = input('Digite o operador: +, -, * ou /: ')
qnt_macas = calc2(n1, n2, op)
compras = {"Maçã":qnt_macas}
print(compras)

#nessa versão, foi feito o return para guardar o resultado em qnt_macas e transferir para compras 
#como se o resultado fosse a quantidade de mação 'compradas'