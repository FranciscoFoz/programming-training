#SOMA DE NÚMEROS
'''
Esta função irá receber uma quantidade variável de números, realizará a soma deles e retornará 
o resultado final.

'''

def soma(*numeros):

    resultado = 0

    for i in numeros:
        resultado += i

    return resultado



soma(10,20,5,5,10,*[25,25])

