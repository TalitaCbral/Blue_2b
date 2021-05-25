#Exercício Treino 2 - Escreva uma função que recebe dois números (a e b) 
# como parâmetro e retorna True caso a soma dos dois seja 
# maior que um terceiro parâmetro, chamado limite.

def comparador_de_resultados (a, b, c):
    soma = a + b
    return soma > c
a = int(input('Informe um número: '))
b = int(input('Informe outro número: '))
c = int(input('Informe um limite: '))
print(comparador_de_resultados(a, b, c))