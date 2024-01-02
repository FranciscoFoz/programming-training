# MAIOR ELEMENTO
'''
Essa função irá receber um tipo iteravel e retornará o maior elemento dele.

'''

def encontrar_maior_elemento(iteravel):
    maior = None
    for elemento in iteravel:
        if maior is None or elemento > maior:
            maior = elemento
    return maior

print(encontrar_maior_elemento('0'))
print(encontrar_maior_elemento('python'))
print(encontrar_maior_elemento([1,2,3,4,5,6,7,8,9,10]))
print(encontrar_maior_elemento((1,5)))
