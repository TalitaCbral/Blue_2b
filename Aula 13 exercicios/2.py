#2. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
#programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
#quantidade de gols feito em cada partida. No final tudo isso será guardado em um
#dicionário, incluindo o total de gols feitos durante o campeonato.
lista1 = []
nome = input('Nome do jogador: ')
partidas = input('Quantidade de partidas: ')
for item in partidas:
    lista1.append(input('Qantidade de gols: ' * 1))
    print(f'O jogador {nome}, fez {lista1} gols em {partidas} partida(s) jogadas!')
#print(lista1)