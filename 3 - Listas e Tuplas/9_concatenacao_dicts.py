#CONCATENAÇÃO DE DICTS

'''

Essa função irá recebr uma lista de dicts e retornará um único dict que combine todas as chaves e
valores. 
Caso ela apareça em mais de um argumento, o valor deve ser uma lista contendo todos os
valores dos argumentos.

'''

lista_dicts = [
    {'A':1},
    {'B':2},
    {'C':3},
    {'D':4},
    {'E':5},
    {'E':6},
    {'E':7}
]

def concatena_dict(lista_dicts):
    
    resultado = {}
    
    for dicionario in lista_dicts:
        for chave, valor in dicionario.items():
            if chave in resultado:
                resultado[chave].append(valor)
            else:
                resultado[chave] = [valor]
    
    return resultado


print(concatena_dict(lista_dicts))
