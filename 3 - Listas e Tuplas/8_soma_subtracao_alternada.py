#SOMA E SUBTRAÇÃO ALTERNADA
'''
Essa função irá receber uma lista de elementos numéricos e irá somar os elementos de índice par 
e subtrair os elementos de índice ímpar.

'''

def soma_subtracao_alternada(numeros):
    
    resultado = 0
    for i, num in enumerate(numeros):
        if i % 2 == 0:
            resultado += num
        else:
            resultado -= num
    return resultado

print(soma_subtracao_alternada([10,20,30,40,50,60])) # saída: 10 - 20 + 30 - 40 + 50 - 60 = 30
print(10*'-')
print(soma_subtracao_alternada([1,2,3,4,5,6,7,8,9,10]))
print(10*'-')
print(soma_subtracao_alternada(range(1,101)))
print(10*'-')