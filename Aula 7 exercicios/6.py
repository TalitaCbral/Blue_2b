# Um professor, muito legal, fez 3 provas durante um semestre, 
#mas só vai levar em conta as duas notas mais altas para calcular a média.
# Faça uma aplicação que peça o valor das 3 notas, mostre como seria
#a média com essas 3 provas, a alta média com as 2 notas mais,
#bem como sua nota mais alta e sua nota mais baixa.

def calculo_nota (n1, n2, n3):
    maior = n1
    medio = n2
    menor = n3
#verificando a maior nota 
    if n2 > maior:
        maior = n2
    elif n3 > maior:
        maior = n3
#verificando a segunda maior nota 
    if maior >= n2 > n3:
        medio = n2
    elif maior >= n3 > n2:
        medio = n3
    elif maior >= n1 > n2:
        medio = n1
#verificando a menor nota das 3 
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    media_notas = (n1 + n2 + n3)/ 3
    media_mais_altas = (maior + medio)/ 2
    print(f'Média com as tres notas: {media_notas}')
    print(f'Médias com duas melhores notas: {media_mais_altas}')
    print(f'Sua nota mais alta: {maior}')
    print(f'Sua nota mais baixa: {menor}')

calculo_nota(10, 5, 9)