# ERROR - EXERCÍCIO 3


'''
Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um das listas, 
formando uma lista de tuplas de 3 elementos, no qual o primeiro e segundo elemento da tupla 
são os valores na posição i das listas e o terceiro elemento é a soma dos valores na posição i das listas.

A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar como resultado a lista de tuplas. 
Caso as listas enviadas como parâmetro tenham tamanhos diferentes,
a função deve retornar um IndexError com a frase: 'A quantidade de elementos em cada lista é diferente.'

Valores sem erro:
lista1 = [4,6,7,9,10]
lista2 = [-4,6,8,7,9]

Listas com tamanhos diferentes:
lista1 = [4,6,7,9,10,4]
lista2 = [-4,6,8,7,9]

Listas com valores incoerentes:
lista1 = [4,6,7,9,'A']
lista2 = [-4,'E',8,7,9]

'''


def agrupar_listas(lista1,lista2):
    
    try:

        resultado = [(lista1[i], lista2[i], lista1[i] + lista2[i]) for i in range(len(lista1))]
                
        print(resultado)
        
    except IndexError as ie:
        print(ie.__class__,f'\nMensagem: {ie}',"\nA quantidade de elementos em cada lista é diferente.")
        
    except Exception as e:
        print(e.__class__,f'\nErro desconhecido: {e}')


#lista1 = [4,6,7,9,10]
#lista2 = [-4,6,8,7,9]

#agrupar_listas(lista1,lista2)

#lista1 = [4,6,7,9,10,4]
#lista2 = [-4,6,8,7,9]

#agrupar_listas(lista1,lista2)

#lista1 = [4,6,7,9,'A']
#lista2 = [-4,'E',8,7,9]

#agrupar_listas(lista1,lista2)