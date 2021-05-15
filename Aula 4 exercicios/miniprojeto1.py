#Mini Projeto 01 - Conversor de Moeda
#Vamos construir um programa que irá converter moedas do real para o dólar e do dólar para o real. Vamos considerar que $ 1,00 = R$ 5,75

'''Parte 1
Faça o conversor de moeda receber o valor em real e mostrar o valor convertido para dólar no formato $ XXXX.XX

Exemplo:

Valor em R$ = 1000
Valor em $ = $ 173.91
Parte 2
Altere o conversor de moedas para receber o valor em dólar, converter para real e mostrar o resultado no formato R$ XXXX.XX

Exemplo:

Valor em $ = 1000
Valor em R$ = R$ 5750.00'''


#parte 1

dolar = float(input('Informe a quantidade de dólar para conversão: US$'))
cotacao = 5.75
print(dolar * cotacao)

#parte 2

real = float(input('Informe a quantidade de real para conversão: R$'))
cotacao = 5.75
print(real / cotacao)