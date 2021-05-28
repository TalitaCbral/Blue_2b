# 
class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.salario = 0
        self.horas_trabalhadas = 0

    def registra_hora_trabalhada(self):
        self.horas_trabalhadas += horas

    def calcula_salario(self):
        self.salario = self.horas_trabalhadas * self.valor_hora_trabalhada

funcionario = Funcionario("Talita", "Atendente", 35)
print(f'Salario atual: {funcionario.salario}')
print(f'Horas trabalhadas: {funcionario.horas_trabalhadas}')
horas = float(input('Digite quantas horas trabalhadas: '))
funcionario.registra_hora_trabalhada()
funcionario.calcula_salario()
print(f'Salario atual: {funcionario.salario}')
print(f'Horas trabalhadas: {funcionario.horas_trabalhadas}')