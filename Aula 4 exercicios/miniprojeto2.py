#Mini Projeto 02 - Calculadora de aumento de aluguel
#Vamos construir um programa que irá calcular o aumento anual do seu aluguel em duas partes:

'''Parte 1
A sua calculadora vai receber o valor do aluguel e calcular o aumento baseado no IGPM de 31%. A calculadora deve apresentar o aluguel reajustado no formato R$ XXXX.XX

Exemplo:

Valor do aluguel = 1000
Valor do aluguel reajustado = R$ 1310,00
Parte 2
Agora, altere sua calculadora para receber além do valor do aluguel, o percentual do reajuste no formato XX%.

Dica: Descubra uma forma de transformar o percentual recebido em um número para efetuar o cálculo.

Exemplo:

Valor do aluguel = 1000
Percentual do reajuste = 31%
Valor do aluguel reajustado = R% 1310,00'''

#parte 1
aluguel = float(input('Informe o valor do aluguel: '))
percentual_reajuste = 1.31
valor_aluguel_reajustado = aluguel * percentual_reajuste
print(f'R${valor_aluguel_reajustado:.2f}') 

#parte 2
aluguel = float(input('Informe o valor do aluguel: '))
percentual_reajuste = input('Informe o percentual de reajuste: ')
percentual_reajuste_decimal = (float(percentual_reajuste.replace("%", "")) / 100) + 1
valor_aluguel_reajustado = aluguel * percentual_reajuste_decimal 
print(f"R$ {valor_aluguel_reajustado:.2f}")