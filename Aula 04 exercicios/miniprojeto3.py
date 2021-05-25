#Mini Projeto 03 - Calculadora de dano
#Vamos implementar a calculadora de dano de RPG!!

'''Parte 1
O programa vai receber a vida e um monstro (entre 10 e 50) e o valor do ataque do jogador por turno (entre 5 e 10)

Baseado nos valores, exiba a quantidade de turnos que o jogador irá demorar para conseguir derrotar o monstro.

Exemplo:

Vida de um monstro (entre 10 e 50): 26
Valor do ataque do jogador por turno (entre 5 e 10): 5
Resultado: O jogador irá precisar de 6 turnos para derrotar o monstro.
Parte 2
Altere o programa para ao invés de receber a vida do monstro, gerar aleatoriamente um valor entre 10 e 50.'''

#parte 1
import math 
vida_do_monstro = int(input('Informe a vida do monstro (entre 10 e 50): '))
ataque_do_jogador = int(input('Informe o valor de ataque (entre 5 e 10): '))

turnos_necessarios = math.ceil(vida_do_monstro / ataque_do_jogador)
print(f'O jogador precisara de {turnos_necessarios} turnos para derrotar o monstro!')

#parte 2 
import math 
import random

vida_do_monstro = random.randint(10, 50)
ataque_do_jogador = int(input('Informe o valor de ataque do jogador por turno (entre 5 e 10): '))

turnos_necessarios = math.ceil(vida_do_monstro / ataque_do_jogador)
print(f'vida do monstro: {vida_do_monstro}')
print(f'O jogador precisara de {turnos_necessarios} turnos para derrotar o monstro!')

#part 3 (experimento todo automatizado)
import math
import random

vida_do_monstro = random.randint(10, 50)
ataque_do_jogador = random.randint(5,10)

turnos_necessarios = math.ceil(vida_do_monstro / ataque_do_jogador)
print(f'vida do monstro: {vida_do_monstro}')
print(f'Ataque do jogador: {ataque_do_jogador}')
print(f'O jogador precisara de {turnos_necessarios} turnos para derrotar o monstro!')