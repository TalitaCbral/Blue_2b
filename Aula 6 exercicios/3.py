#3.	 Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros 
# formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
#  que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir 
# o imposto sobre vendas.

def somaimposto (taxaimposto, custo):
    return (1 + taxaimposto/100)*custo
t = float(input('Digite o imposto: '))
c = float(input('Custo do item: '))
print('O valor atualizado com imposto: ', somaimposto(t,c))

