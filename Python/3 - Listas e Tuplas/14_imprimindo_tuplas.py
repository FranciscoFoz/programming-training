# IMPRIMINDO TUPLAS

'''
Esse script irá receber uma lista de tuplas com nome, sobrenome e tempo de chegada de pessoas.
Ordenará pelo sobrenome e imprimirá, com um espaço igual entre cada um dos elementos deles, 
alinhado à direita, arredondando o tempo para duas casas decimais.
'''

import operator
pessoas = [('Donald', 'Trump', 7.85), ('Vladimir', 'Putin', 12.626), ('Jinping', 'Xi', 10.603)]


def formatar_lista_tuplas(lista_de_tuplas):

    template = '{1:10} {0:10} {2:5.2f}' #5 alinha o valor à direita
    
    for pessoa in sorted(lista_de_tuplas,key=operator.itemgetter(1, 0)):
        
        print(template.format(*pessoa)) # "*" desempacota a tupla
    


formatar_lista_tuplas(pessoas)
