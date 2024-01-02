# TRANSFORMA TUPLAS EM DICIONÁRIOS

'''
Esse script irá transformar tuplas nomeadas em dicionários e imprimir cada um deles.
'''

import collections

Presidente = collections.namedtuple('Presidente', ['sobrenome', 'nome', 'tempo'])

presidentes = [
    Presidente('Biden', 'Joe', 7.85), 
    Presidente('Vladimir', 'Putin', 12.626), 
    Presidente('da Silva', 'Lula', 10.603)
]

for presidente in presidentes:
    print(presidente._asdict())
