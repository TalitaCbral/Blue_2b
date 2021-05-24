#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma 
# string no formato D de mesPorExtenso de AAAA. Valide a data e retorne NULL caso a data seja inválida.

def mesextenso (dados):
    dd = dados [0:2]
    dia = int (dd)
    mm = dados [3:5]. replace ('0', ' ')
    nummes = int(mm)
    aaaa = dados [6 :]
    ano = int (aaaa)
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    extenso = meses [nummes - 1]
    if ano % 4 == 0 and ano % 100 != 0:
        if extenso == 2:
            dia >= 1 and dia <= 29
            return f'{dd} de {extenso} de {aaaa}.'
    else: 
        if extenso == 2:
            dia >= 1 and dia <= 28
            return f'{dd} de {extenso} de {aaaa}.'
data = input('Digite a data desejada: ')
print(mesextenso)