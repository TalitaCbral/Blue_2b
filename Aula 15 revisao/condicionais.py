#exemplo simples
nome = input('Digite um nome: ')

if nome == 'Paulo':
    print('você é o Paulo! que bom')
    print('Nós gostamos muito do Paulo')
elif nome == 'Ricardo':
     print('você não é o Paulo! Você é o Ricardo')
else:
    print('Você não é o Paulo nem o Ricardo!')
print('Nós também gostamos de você',nome,'Bem vindo(a)!')
'''
#Exemplo com numeros!
numero = input('Digite um número: ')
if numero >= 50:
    print('Maior que 50!')
elif numero >= 30:
    print('Maior que 30!')
elif numero >= 10:
    print('Maior que 10!')
else:
    print('Menor que 10!')
''''''
#if dentro de if 
viaja = input('Você viaja de avião? [S / N] ')
if viaja == 'S':
    opcao = input('Posso te mostrar promoções?')
    if opcao == 'S':
        print('vá até nossa agência mais próxima')
    else:
        print('Tá bom né, fazer oque!')
else:
    print('Até a próxima!')
'''
