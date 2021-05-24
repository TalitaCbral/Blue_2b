#1. Crie um programa onde você cadastre a data de nascimento (dd/mm/aa) de algumas
#celebridades em um dicionário. Ao escolher uma celebridade, seu programa deve
#retornar a data completa. Não esqueça de validar se a celebridade escolhida está
#presente em seu dicionário.

celebs = {'Selena Gomez': '1998',
            'Card B': '1997',
             'Ariana Grande': '2000',
              'Normani': '1990',
              'Justin Bieber': '2000'}
print('Bem vindo(a) ao calendário Celebs, verifique nossos Famosos: ')
for itens in celebs:
    print(itens)
nome = input('Informe de qual celebridade gostaria de ver a data de nascimento: ').title()
print(celebs.get(nome, f'O nome {nome} não foi encontrado em nosso banco de dados!'))

idade = 2021 - int(celebs[nome])
print(f'A idade de {nome} é de {idade} anos!')

#sintax get: dicionario.get(chave) #retorna um valor específico