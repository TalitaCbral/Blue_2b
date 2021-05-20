#tupla dentro da lista, como um dos elementos
lista = [1, 2, 3, "String", "String2"]
tupla = ("Nome","123-456")
lista3 = [("Nome","123-456"), 2, 3, "String", "String2"]

# Criando lista com tuplas
lista_contatos = [("Ana Paula","123-456"),("Joao","456-789"),("Fabricio","444-777"),("Ricardo","777-888"),("Bruno","999-888")]
print(len(lista_contatos))
print(type(lista_contatos))
print(lista_contatos)
print(lista_contatos[0])
print(lista_contatos[0][0])
print()

# Criando um dicionário a partir da lista acima com a função dict()
contatos = dict(lista_contatos) # dicionario = dict(lista_a_ser_convertida)
print(contatos)
print("Type de contatos:")
print(type(contatos))
print()

# Acessando um valor dentro de um dicionário
print('Acessando o valor da chave "Ana Paula"')
print(contatos.get("Ana Paula"))
print(contatos["Ana Paula"])

# print(contatos["Eurico"]) # KeyError - A chave não existe

print(contatos.get("Eurico","Nome não encontrado")) # Retorna um valor padrão caso a chave não seja encontrada

nome = input("Digite o nome: ") # Recebendo uma entrada para procurar o valor
print(contatos.get(nome,"Nome não encontrado")) 


#Criando um dicionario "na mão"
"""
dicionario_contatos = {"Alexandre":"555-444", "Talita":"111-222", "Nadja":"666-333"}
print(dicionario_contatos)
print(len(dicionario_contatos))
"""
# criando dicionario (mais exemplos, aula 13)

lista1 = [('Eurico', '123-456'), ['Marco', '133-788']]
dic1 = dict(lista1)
print(dic1)

# como alterar valores e +

lista0 = [('Eurico', '123-456'), ['Marco', '133-788']]
dic2 = dict(lista0)
dic2['Eurico'] = {'Endereço':'Rua abc', 'Telefone': '123-456'}
print(dic2)
print(dic2.get('Eurico', 'Não encontrado'))
print('Eurico' in dic2.values())

#adicionando novos valores 
dic2 ['Novo Endereço'] = 'Rua ABCD'
print(dic2)

#treino de sintax : inserir novos valores
vingadores = {"Chris Evans": "Capitão América", "Mark Ruffalo": "Hulk", "Tom Hiddleston": "Loki",
"Chris Hemworth": "Thor", "Robert Downey Jr": "Homem de Ferro", "Scarlett Johansson": "Viúva Negra"}

vingadores ['Tom Hardy'] = 'Venom'
vingadores ['Jason Momoa'] = 'Aquaman'
vingadores ['Ben Affleck'] = 'Demolidor'
vingadores ['Halle Berry'] = 'Tempestade'
vingadores ['Nicolas Cage'] = 'Motoqueiro Fantasma'
print(vingadores)

#para deletar valores
del vingadores ['Ben Affleck'] # não vantajoso se a chave não existir
print(vingadores.pop('Jason Momoa', 'Ator não encontrado')) # remove a chave e retorna uma mensagem caso a chave não exista
print(vingadores.pop('Heath Ledger', 'Ator não encontrado'))
print()
print(vingadores)
print()
excluido0 = vingadores.pop('Tom Hardy')
#remove o ultimo valor e retorna a chave como tupla
excluido = vingadores.popitem() 
#exclui o valor indicado e armazena
excluido1 = vingadores.pop('Nicolas Cage') 
print(excluido) 
lista_excluidos = []
lista_excluidos.append(vingadores.pop('Chris Evans'))
lista_excluidos.append(vingadores.pop('Chris Hemworth'))
print(lista_excluidos)
print(vingadores) 

#treino
vingadores = {"Chris Evans": "Capitão América", "Mark Ruffalo": "Hulk", "Tom Hiddleston": "Loki",
"Chris Hemworth": "Thor", "Robert Downey Jr": "Homem de Ferro", "Scarlett Johansson": "Viúva Negra"}

del vingadores['Chris Evans']
print(vingadores.pop('Mark Ruffalo', 'Ator não localizado'))
treino = vingadores.popitem()
print(vingadores)

# Unindo Dicionários
vingadores = {"Chris Evans": "Capitão América", "Mark Ruffalo": "Hulk", "Tom Hiddleston": "Loki",
"Chris Hemworth": "Thor", "Robert Downey Jr": "Homem de Ferro", "Scarlett Johansson": "Viúva Negra"}

#Novo

animais = {'cachorro': 'Vira lata Caramelo', 'Cavalo': 'Manga Larga', 'Gato': 'Siamês'}
for itens in animais:
    print(itens)
    vingadores[itens] = animais[itens]
    input()
#vingadores[itens] = animais[itens] / adiciona elementos novos no dicionário 'Vingadores'
#input(), é como um enter, ele para meu programa e continua só aprtando enter
print(vingadores)

#treino de união, exercitando o uso de 'for com dicionario' 
viloes = {"CGI":"Thanos","Cavera":"Vermelha","Miranha":"Negro do Espaço"}
for hero in viloes:
    print(hero)
    vingadores[hero] = viloes[hero]
print(vingadores)

#outro método de união - simplificado
#método update(), forma simples de união
vingadores.update(viloes)
print(vingadores)