#2.	Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

palavra = input('Informe a palavra: ').lower()
palavra_oculta = ''
chances = 0
for letra in range(len(palavra)):
    palavra_oculta = palavra_oculta + '_'
for i in range(len(palavra)+6):
    if i == 7:
        print('Você não conseguiu completar a palavra!')
        print('Ops, você foi enforcado!')
    elif '_' not in palavra_oculta:
        print('Você conseguiu!')
        print(f'Palavra: {palavra_oculta}')
        break
    else:
        print(f'Você tem {6-i} chances!')
        print('Palavra a ser adivinhada: ')
        print(palavra_oculta)
        jogue = input('Informe uma letra e tente descobrir a palavra: ').lower()
        for index in range(len(palavra)):
            if palavra[index] == jogue:
                palavra_oculta = list(palavra_oculta)
                palavra_oculta[index] = jogue
                string = ''.join(palavra_oculta)
                palavra_oculta = string
