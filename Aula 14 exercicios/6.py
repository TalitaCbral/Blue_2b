#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

   # "Telefonou para a vítima?"

   # "Esteve no local do crime?"

   # "Mora perto da vítima?"

   # "Devia para a vítima?"

   # "Já trabalhou com a vítima?" 

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 

   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",

   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 

   # Caso contrário, ele será classificado como "Inocente".

P = ["Telefonou para a vítima?",  "Esteve no local do crime?",
     "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
sim = 0
for i in P:
    print(i)
    c = input(((("Sim ou Não?").lower()).replace("ã", "a")).strip())
    if c == "sim":
        sim = sim + 1
if sim == 2:
    print("Suspeita")
elif 3 <= sim <= 4:
    print("Cumplice")
elif sim == 5:
    print("Assassino!! cxx]====> ")
else:
    print("inocente")