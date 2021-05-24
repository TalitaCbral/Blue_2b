#criar função = def
def faz_tudo():
    #num1 = float(input('Digite num1: '))
    #num2 = float(input('Digite num2: '))
    if num1 > num2:
        print(f'O número {num1} é maior!')
    elif num2 > num1:
        print(f'O número {num2} é maior!')
    else:
            print(f'Os números {num1} e {num2} são iguais!')
    global soma
    soma = num1 + num2
    print('Os numeros somados resultam em:',soma) 
num1 = float(input('Digite num1: '))
num2 = float(input('Digite num2: '))
print(num1,num2)
faz_tudo()
print(soma)

#global = serve para usar variavéis dentro e fora da função 
#( tomar cuidado pois pode gerar troca de valores) nem sempre recomendada!
