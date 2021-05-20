#1.- Exercício Treino - Crie um dicionário em que suas chaves serão os números 
#1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) e seus valores
#correspondentes aos quadrados desses números. 
#lista = [1, 4, 5, 6, 7, 9]

#exercico 6 // 12

idades = []
acima = []
mulheres = []
lista_final = []
media = ''
parada = ''
while parada != 'não':
    nome = input('\nDigite seu nome:')
    sexo = input('Digite seu sexo (M ou F):').upper()
    if sexo == 'M' or sexo == 'F':
        idade = int(input('Digite sua idade: '))

    else:
        print('Sexo inválido!!!')
        sexo= input('Digite seu sexo (M ou F):')
    if sexo == 'F':
        mulheres.append(nome)
    parada = input('Deseja continuar? (sim ou não)')
    if parada == 'sim' or parada == 'não': 
        dic ={'nome': nome, 'sexo': sexo, 'idade': idade }
        idades.append(dic.get('idade'))
        media = sum(idades)/ len(idades)
        if idade > media:
            acima.append([nome, idade])
        lista_final.append(dic)
    else:
        parada = input('Deseja continuar? (sim ou não)')
        media = sum(idades)/ len(idades)
        lista_final.append({'nome': nome, 'sexo': sexo, 'idade': idade })
        idades.append(dic.get('idade'))
        media = sum(idades)/ len(idades)
