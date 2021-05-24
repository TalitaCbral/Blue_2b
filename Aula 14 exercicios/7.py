#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que 
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []]
for item in range(1, 8):
    num1 = int(input(f'Digite o valor{item}: '))

    if num1 %2 == 0:
        num[0].append(num1)
    else:
        num[1].append(num1)

num[0].sort()
num[1].sort()
print(f'Os numeros pares informados foram: {num[0]}\nOs números ímpares informados foram:: {num[1]}')