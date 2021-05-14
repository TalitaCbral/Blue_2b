#Exercício 06
#Elabore um programa que recebe o seu nome, endereço e hobby e mostra cada uma das informações da seguinte forma:

'''Nome -> Letra maiúscula
Endereço -> Letra minúscula
Hobby -> Primeira letra maiúscula
Exemplo Entrada:

Nome: bruno fabri
Endereço: Rua ABC
Hobby: jogar cs
Exemplo Saída:

Nome: BRUNO FABRI
Endereço: rua abc
Hobby: Jogar cs'''

nome = input('Digite seu nome: ')
endereço = input('Digite seu endereço: ')
hobby = input('Digite seu hobby: ')

print(nome.upper())
print(endereço.lower())
print(hobby.title())

#forma 2

nome = input('Digite seu nome: ').upper()
endereço = input('Digite seu endereço: ').lower()
hobby = input('Digite seu hobby: ').title()
print('''
nome: {}
  endereço: {}
  hobby: {}
    '''. format(nome, endereço, hobby))
