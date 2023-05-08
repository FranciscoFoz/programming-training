#SOMA ELEMENTOS DA PILHA
'''
Essa função irá receber uma lista de elementos numéricos e retornará uma impressão com a soma de todos os elementos pares e 
ímpares.
'''

def primeiro_ultimo(x):
    
    elementos_pares = []
    elementos_impares = []
    
    for elemento in x:
        if elemento % 2 == 0:
            elementos_pares.append(elemento)
        else:
            elementos_impares.append(elemento)
    
    soma_pares = sum(elementos_pares)
    soma_impares = sum(elementos_impares)
    
    return print(f'Soma elementos pares: {soma_pares}\nSoma elementos impares: {soma_impares}')

primeiro_ultimo([10,10,10,5,5,5])
print(10*'-')
primeiro_ultimo([1,2,3,4,5,6])
print(10*'-')
primeiro_ultimo(range(1,101))
print(10*'-')