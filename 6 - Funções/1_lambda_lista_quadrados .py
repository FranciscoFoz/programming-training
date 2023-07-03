# LAMBDA - LISTA QUADRADOS

'''
Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

'''

def quadrado_lista(lista):
    
    quadrado = lambda x: x ** 2
    
    lista_quadrados = list(map(quadrado,lista))
    
    return lista_quadrados

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(quadrado_lista(lista))

