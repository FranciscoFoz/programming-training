# NUMEROS AO QUADRADO 
'''
Essa função irá receber um número (int ou float) e retornará o número ao quadrado dele.

'''

def numeros_ao_quadrado(x):
    
    lista_numeros = []
    
    lista_numeros.append(x)
    
    return [print(numero**2) for numero in lista_numeros]

print(numeros_ao_quadrado(2))
print(numeros_ao_quadrado(5))
print(numeros_ao_quadrado(5.5))