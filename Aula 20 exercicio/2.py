#Criando classe Hereditária

class Pessoa:
    def __init__(self, Nome, Idade, CPF, Telefone):
        self.__Nome = Nome 
        self.__Idade = Idade
        self.__CPF = CPF
        self.__Telefone = Telefone
        '''self.__contadornome = 0'''

    def __str__(self): #retorna oq foi pedido quando chamar apenas o objeto (n um atributo ou método)
        return f'nome: {self.__Nome}, idade: {self.__Idade}, CPF: {self.__CPF}, telefone: {self.__Telefone}'
   
    #get = pegar, receber > Defino o método que vai passar o valor do atributo para fora 
    def getNome(self):
        '''self.__contadornome += 1'''
        return self.__Nome
        
    def getIdade(self):
        return self.__Idade
    
    def getCPF(self):
        return self.__CPF

    def getTelefone(self):
        return self.__Telefone

    def saudacao(self):
        print('Seja bem vindo!')
    
    '''
    def getContadorNome(self):
        print(f'O nome {self.__Nome} foi pesquisado {self.__contadornome} vezes!')
    '''
    #set > Altera o valor do atributo

    def setNome(self,Nome):
        self.__Nome = Nome
    
    def setIdade(self,Idade):
        self.__Idade = Idade
    
    def setCPF(self,CPF):
        '''senha = input('Informe senha:')
        if senha == '040506':
            print('Senha correta, cpf alterado para: ')'''
        self.__CPF = CPF
        '''else:
            print('Senha incorreta!')'''
        
    def setTelefone(self,Telefone):
        self.__Telefone = Telefone
        
class Advogado(Pessoa):
    def __init__(self, Nome, Idade, CPF, Telefone, OAB):
        self.__OAB = OAB
        super().__init__(Nome, Idade, CPF, Telefone)
    
    def saudacao(self):
        print('Seja bem vindo ao meu escritório de Advocacia!')


class Medico(Pessoa):
    def __init__(self, Nome, Idade, CPF, Telefone, CRM):
        self.__CRM = CRM
        super().__init__(Nome, Idade, CPF, Telefone)
    
    def saudacao(self):
        print('Seja bem vindo ao meu Consultório!')


advogado = Advogado('Pedro', 30, '488762544-88', '11951668574', 'Cassada')
print(vars(advogado))
medico = Medico('Leandra', 20, '48876245570', '11 976343360', '001234')
print(vars(medico))
'''
Medic = ('Paulo', 30, '422085741', '1159836204', 'crm-000123') 
Medic2 = ('Jonas', 30, '466378257', '118543200', 'crm-123456')

Advog = ('Vania', 37, '429988551', '1122117744', 'oab-733856')
Advog2 =('Tania', 25, '49978257', '11999999', 'oab-458760')

lista = [Medic, Medic2]
lista2 =  [Advog, Advog2]
for item in lista:
    print(item)
for item in lista2:
    print(item)'''

advogado.saudacao()
medico.saudacao()
#people1 = Pessoa('Lenadra', 20, '48876245570', '11 976343360')
#people2 = Pessoa('Talita', 21, '49976245588', '11 951389936')
#print(Pessoa.getNome())
#Pessoa.setNome('Talita')
#print(Pessoa.getNome())

#exemplos get e set