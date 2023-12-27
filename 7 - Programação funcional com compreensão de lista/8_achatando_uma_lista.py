# ACHATANDO UMA LISTA

def achatando_lista(minha_lista):
    return [
        um_elemento
        for uma_sublista in minha_lista
        for um_elemento in uma_sublista
        ]
    
print(achatando_lista([[1,2], [3,4],[5,6,7]]))