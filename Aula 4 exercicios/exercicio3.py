#Exercício 03
#Elabore um programa que recebe o nome de uma pessoa do terminal e mostra a seguinte mensagem: Olá {nome}! Seja bem vindo ao fantástico mundo da programação

nome = input("digite seu nome: ")
print('Olá', nome, 'Seja bem vindo ao fantástico mundo da programação')

# e também :

print('Olá', nome + '! Seja bem vindo ao fantástico mundo da programação')

#ou

print(f'Olá {nome} !seja bem vindo ao fantático mundo da programação')

#e até mesmo

print('Olá {} !seja bem vindo ao fantástico mundo da programação' .format(nome))