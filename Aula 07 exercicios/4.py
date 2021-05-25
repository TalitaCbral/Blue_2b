#Exercício 4 - Crie um programa que tenha uma função chamada voto () que vai receber como 
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma 
# pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse exercício,
# pesquise sobre a função date da biblioteca Datetime.
import datetime

def voto(idade):
    condition = 2020 -idade
    if condition <= 16:
        return f'Com {condition} anos: [ não vota ]'
    elif 16 <= condition < 18 or condition > 65:
        return f'Com {condition} anos: [ voto opcional ]'
    else:
        return f'Com {condition} anos: [ voto obrigatorio ]'
idade = int(input('Ano de nascimento: '))
print(voto(idade))
