#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma 
# string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e 
# mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = input("Digite uma frase: ")
vogais = []
cont = 0

for item in frase:
    if item in 'aeiou':
        # num_vogais += 1
        vogais.append(item)
        cont += 1
print(f'Vogais encontradas:{"".join(vogais)}')
print(f'Quantidade:{cont} vogais encontradas na frase!')

#segunda parte 
consoantes = []
cont = 0

for item in frase:
    if item not in 'aeiou':
        consoantes.append(item)
        cont += 1
print(f'Frase sem vogais:{"".join(consoantes)}')
print(f'Quantidade:{cont} consoantes na frase!')
