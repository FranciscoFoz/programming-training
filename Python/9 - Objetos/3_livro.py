# LIVRO

'''
Crie uma classe chamada Livro com os seguintes atributos: titulo, autor e ano.

Em seguida, crie um método chamado informacoes que retorna uma string contendo 
as informações do livro no formato "Título: [titulo], Autor: [autor], Ano: [ano]". 

Por fim, crie um objeto da classe Livro, defina os valores dos atributos e 
chame o método informacoes para exibir as informações do livro.

'''

class Livro:
    
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        
    def informacoes(self):
        
        print(f'Título: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}')
        

Livro('Nosso Lar','Chico Xavier',1944).informacoes()