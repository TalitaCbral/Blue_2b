#1.	Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
'''
a.	tamanho da lista.
b.	maior valor da lista.
c.	menor valor da lista.
d.	soma de todos os elementos da lista.
e.	lista em ordem crescente.
f.	lista em ordem decrescente.'''

lista = [5, 7, 2, 9, 4, 1, 3]
print(f'Tamanho da lista: {len(lista)}')
print(f'Maior valor: {max(lista)}')
print(f'Menor valor: {min(lista)}')
print(f'Soma de todos valores: {sum(lista)}')
lista.sort()
print(f'Lista em ordem crescente: {lista}')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')