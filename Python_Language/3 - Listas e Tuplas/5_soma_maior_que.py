#SOMA MAIOR QUE
'''
Essa função irá receber um número e elementos *args.
Irá somar o número com os elementos args, apenas se eles forem maiores do que ele.

A função irá funcionar independentemente se args for um número inteiro, lista ou tupla.
Além disso ela deverá retornar o tipo de dado que args contém.

'''

def soma_maior_que(numero,*args):
    
    soma = []
    
    tipo_args = str(type(args[0])).split("'")[1]
        
    if isinstance(args[0], (list,tuple)):
        args = args[0]
    else:
        args = list(args)
    
    for elemento in args:
        if numero <= elemento:
            soma.append(elemento)

        
    resultado = sum(soma,numero)
    
    return tipo_args,resultado

print(soma_maior_que(10, 5, 20, 30, 6))
print(soma_maior_que(10, [5, 20, 30, 6]))
print(soma_maior_que(10, (5, 20, 30, 6)))
print(soma_maior_que(10, (5, 6)))


