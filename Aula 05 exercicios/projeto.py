#Resultado da primeira/segunda aula em Python:

'''• Escreva um programa que receba uma string digitada pelo usuário;

• Caso a string seja "medieval", exiba no console "espada";

• Caso contrário, se a string for "futurista", exiba no console "sabre de luz";

• Caso contrário, exiba no console "Tente novamente"

Continuação do PROJETO 1 • Escreva um programa que receba um ataque de espada ou sabre digitada pelo usuário;

• Caso o ataque seja "espada", exiba no console "VOCÊ AINDA NÃO MATOU O CHEFÃO";

• Caso contrário, se o ataque for "sabre", exiba no console "VOCÊ DERROTOU O CHEFÃO COM O SABRE DE LUZ";

• Caso contrário, exiba no console "ATAQUE NOVAMENTE"'''


#Parte 1

objeto = str(input('Indique seu ataque (Medieval ou Futurista): '))

if objeto == 'medieval':
  print('Sua arma é uma Espada!')
elif objeto == 'futurista':
  print('Sua arma é um Sabre de luz!')
else:
  print('Tente novamente!')

#Parte 2

arma = str(input('Indique sua arma (Espada ou Sabre de luz): ').upper())

if arma == 'ESPADA':
  print('Ops, você não matou o Chefão!')
elif arma == 'SABRE DE LUZ':
    print('Parabéns! Você derrotou o Chefão com o Sabre de luz!')
else:
  print('Ataque novamente!')