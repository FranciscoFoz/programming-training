#ORDENANDO NOMES

'''
Essa função irá recebr uma lista de dicts e retornará um único dict que combine todas as chaves e
valores. 
Caso ela apareça em mais de um argumento, o valor deve ser uma lista contendo todos os
valores dos argumentos.
'''

import operator

pessoas = [
    {'nome': 'Luiz Inácio', 'sobrenome': 'Lula da Silva', 'email': 'lula@example.com.br'},
    {'nome': 'Jair', 'sobrenome': 'Bolsonaro', 'email': 'jair@example.com.br'},
    {'nome': 'Michel', 'sobrenome': 'Temer', 'email': 'temer@example.com.br'},
    {'nome': 'Dilma', 'sobrenome': 'Rousseff', 'email': 'dilma@example.com.br'},
    {'nome': 'Luiz Inácio', 'sobrenome': 'Lula da Silva', 'email': 'lula@example.com.br'},
    {'nome': 'Fernando Henrique', 'sobrenome': 'Cardoso', 'email': 'fhc@example.com.br'},

]


def ordenacao_alfabetica(lista_dicts):
    
    pessoas = sorted(lista_dicts,key=operator.itemgetter('sobrenome', 'nome'))

    return pessoas

pessoas_ordenada = ordenacao_alfabetica(pessoas)

print('\n')
print(30*'-','Sem ordenação',30*'-')
print([pessoa['sobrenome'] for pessoa in pessoas])
print('\n')
print(30*'-','Com ordenação',30*'-')
print([pessoa['sobrenome'] for pessoa in pessoas_ordenada])
print('\n')