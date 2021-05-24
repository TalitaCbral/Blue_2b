#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar 
# seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a
# seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número inteiro 
# entre 0 e 20. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do
# usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final
# mostre quantos palpites foram necessários para vencer.


senha = 12345
opc = 0
entrada = int(input('Digite a senha numérica: '))
while entrada != senha and opc < 3:
    entrada = int(input('Digite a senha numérica: '))
    print('Errou a senha!')
    if entrada == 654321:
        print('Essa senha não pode!')
        continue #encerra e retorna do início 
    opc += 1
    if opc == 3:
        print('Tentativas esgotadas')
        exit()
if entrada == senha:
    print('A senha está correta, bem vindo ao jogo de adivinhação!')
print('Iremos sortear um número inteiro de 0 a 20')

import math
import random

numero = random.randint(1, 20)
numero_usuario = tentou = 0

while numero != numero_usuario:
    tentou += 1
    numero_usuario = int(input('Tente adivinhar qual o número escolhido: '))
    if numero_usuario > numero:
        print('Está quente, tente um número menor!')
    elif numero_usuario < numero:
        print('Está quente, tente um número maior!')
    else:
        print(f'Parabéns você acertou, O número era: {numero}')
print(f'Você precisou {tentou} tentativas para adivinhar o número!')