# MODIFICA TUPLA

'''
A partir da lista_de_tuplas, crie um código para gerar uma lista de tuplas em que cada tupla tenha o
primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.

'''

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

tuplas_de_nomes = []
for i in lista_de_tuplas:
    tupla_de_nomes.append((i[0],i[0]))
    
print(tuplas_de_nomes)