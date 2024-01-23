# CONTA

'''
Crie uma classe chamada Pessoa com os seguintes atributos: nome, idade e profissao. 
Em seguida, crie um objeto da classe Pessoa e defina os valores dos atributos.
Por fim, exiba os valores dos atributos utilizando a função print.
'''

class Pessoa():
    
    def __init__(self,nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao


pessoa_1 = Pessoa('Francisco',28,'Técnico em Biblioteconomia')
print(f'Nome: {pessoa_1.nome}\nIdade: {pessoa_1.idade}\nProfissão: {pessoa_1.profissao}')