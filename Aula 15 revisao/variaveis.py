var_1 = 'Blue'
var_2 = 500
var_3 = '500'
var_4 = ' -=- '
print(type(var_1))
print(type(var_2))
print(type(var_3))

#for item in range(var_2):
    #print(item)
#uso de for + range

#Enfeite com var e *
print()
print(8 * var_4)
print('      Bem vindo ao meu programa!')
print(8 * var_4)
print()

soma = var_2 + int(var_3)
print('Soma de int com str(usando int na operação soma para converter a str em int) = ', soma)
print('mostre o tipo var_3:',type(var_3))
#não a mudança da str var_3 para int 

#testando se um valor está em uma str
#testandoo not, and,
print('5' in var_3)
print()
print('5' not in var_3)
print()
print('B' and 'e' in var_1)
print()
print('B' and 'w' in var_1)
print()
#print('B' or 'e' in var_1) não da certo testando direto, pode ser usado em (if)!
print()


#teste aleatório com input e f durante aula
numero = float(input('Digite um número no formato x.xx: ').replace(',','.'))
nome = input('Digite seu nome: ')
print(f'O usuário {nome} digitou: {numero:.2f} Obrigada por usar o programa!')
#ou
print(nome, 'escolheu o número:',numero,'Obrigada por usar o programa!')

