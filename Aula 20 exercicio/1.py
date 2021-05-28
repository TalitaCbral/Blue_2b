'''Classe Bomba de Combustível
a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
i. tipoCombustivel.
ii. valorLitro.
iii. quantidadeCombustivel.
b. A classe deve possuir no mínimo esses métodos:
i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que
foi colocada no veículo.
ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor
a ser pago pelo cliente.
iii. alterarValor( ) – altera o valor do litro do combustível.
iv. alterarCombustivel( ) – altera o tipo do combustível.
v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.'''

class BombaDeCombustivel:
    def __init__(self, tipoCombustivel, valorlitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorlitro = valorlitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def alterarValor(self, valorlitro):
        self.valorlitro = valorlitro
        
    def alterarCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel
        
    def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel
            
    def abastecerPorValor(self, valor):
        temp = valor/self.valorlitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel -temp)
        return temp

    def abastecerPorLitro(self, qtd):
        temp2 = qtd * self.valorlitro 
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel -qtd) 
        return temp2
            
a1 = BombaDeCombustivel("Gasolina", 5, 500)
print(a1.abastecerPorValor(150))
print(a1.quantidadeCombustivel)
print(a1.abastecerPorLitro(30))
print(a1.quantidadeCombustivel)