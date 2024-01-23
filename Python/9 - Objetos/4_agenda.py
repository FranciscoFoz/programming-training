# AGENDA

'''
Crie uma classe chamada Agenda que represente uma agenda de contatos. A classe deve ter os seguintes métodos:

adicionar_contato(nome, telefone): recebe o nome e o telefone de um contato e adiciona na agenda.
remover_contato(nome): recebe o nome de um contato e remove da agenda, se existir.
buscar_contato(nome): recebe o nome de um contato e retorna o telefone desse contato, se existir.
listar_contatos(): retorna uma lista com todos os contatos da agenda.

'''


class Agenda:
    def __init__(self):
        self.contatos = []
    
    def adicionar_contato(self, nome, telefone):
        self.contatos.append({nome:telefone})

    
    def remover_contato(self, nome,telefone):
        self.contatos.remove({nome:telefone})

    
    def buscar_contato(self, nome):
        for contato in self.contatos:
            if nome in contato.keys():
                print(f'{nome} - {contato.get(nome)}') 
                return contato.get(nome)

        
    def listar_contatos(self):
        print('\nLista de contatos:\n')
        for contato in self.contatos:
            print(f'->',list(*contato.items())[0],'-',list(*contato.items())[1])
        

agenda = Agenda()
agenda.adicionar_contato('João', '123456789')
agenda.adicionar_contato('Maria', '987654321')
agenda.remover_contato('João','123456789')


telefone_maria = agenda.buscar_contato('Maria')

agenda.adicionar_contato('Francisco', '991250338')
agenda.adicionar_contato('José', '991256989')
agenda.adicionar_contato('Paula', '991204978')
agenda.adicionar_contato('Luíza', '992584774')

contatos = agenda.listar_contatos()

