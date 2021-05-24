import math 
import random

vida_do_monstro = random.randint(10, 50)
ataque_do_jogador = int(input('Informe o valor de ataque do jogador por turno (entre 5 e 10): '))

turnos_necessarios = math.ceil(vida_do_monstro / ataque_do_jogador)
print(f'vida do monstro: {vida_do_monstro}')
print(f'O jogador precisara de {turnos_necessarios} turnos para derrotar o monstro!')