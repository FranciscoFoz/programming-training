# ERROR - EXERCÍCIO 2

'''
Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para int. 

A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a 
lista caso não tenha ocorrido nenhum erro. 

Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.
'''


def transformar_float_to_int(lista):

    try:
        lista_convertida = [int(round(i)) for i in lista]
        
        print(lista_convertida)
        
        return lista_convertida
            
    except ValueError:
        print(f"Erro de valor: {ValueError.__name__}")
        return lista
    
    except Exception:
        print(f"Erro desconhecido: {Exception.__name__}")
        return lista
        
    finally:
        print('\n',10*'-','Fim da execução da função',10*'-')

print('lista_teste')
lista_teste = [2.5,2.3,2.1,2.2,2.4,2.6,2.7,2.8,2.8,2.9]

transformar_float_to_int(lista_teste)

print('lista_erro')
lista_erro = ['a',2.3,2.1,2.2,2.4,2.6,2.7,2.8,2.8,2.9]

transformar_float_to_int(lista_erro)
