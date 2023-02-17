#MÉDIA DE NÚMEROS
'''
Esta função irá receber uma quantidade variável de números, realizará a média deles e retornará 
como resultado final.

'''

def media(*numeros):

    soma = 0

    for i in numeros:
        soma += i
    
    media = round((soma / len(numeros)),2) 

    return media



media(10,20,5,5,10,*[25,25])