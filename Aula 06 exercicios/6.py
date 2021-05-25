#6.	Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F).

nota = int(input('Digite a nota do aluno: '))
if nota == 0 and nota >= 1:
    print('F')
elif nota >= 2 and nota <= 3:
    print('E')
elif nota >= 4 and nota <= 5:
    print('D')
elif nota >= 6 and nota <= 7:
    print('C')
elif nota >= 8 and nota <= 9:
    print('B')
else:
    print('A')