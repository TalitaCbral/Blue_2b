class Ingresso:
    def __init__(self,valor):
        self.valorIngresso = valor

    def imprimirValor(self):
        print(self.valorIngresso)
        return self.valorIngresso 

class ingressoVip(Ingresso):
    def __init__(self, valor, add):
        self.valoradd = add
        super().__init__(valor)
    
    def Imprimirvalorvip(self):
        print(self.valorIngresso + self.valoradd)
        return self.valorIngresso + self.valoradd

ingresso = Ingresso(50)
ingresso.imprimirValor()
vip = ingressoVip(50, 100)
vip.Imprimirvalorvip()