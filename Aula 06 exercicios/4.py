#4.	Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas
#  trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def calculo_salario (horas_trabalhadas, salario_hora):
    if horas_trabalhadas <= 40:
        salario_base = salario_hora * horas_trabalhadas
        return print('Salário no total R$ {0: .2f}' . format (salario_base))
    else:
        salario_base = ((salario_hora * (horas_trabalhadas - 40)) * 1.5) + (horas_trabalhadas * salario_hora)
        return print('Salário no total com 50% fica R$ {0: .2f}' . format (salario_base))
horas = int(input('Digite as horas trabalhadas: '))
salario = float(input('Digite qual o valor por hora trabalhada: '))
calculo_salario (horas,salario)