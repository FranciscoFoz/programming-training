#SOMA ITENS
'''
Essa função irá somar todos os itens que ela receber, independente do seu tipo.
Entretanto, todos os itens devem ser do mesmo tipo.

'''

def soma_itens(*itens):
    if not itens: 
        return itens
    output = itens[0]
    for item in itens[1:]:
        output += item  
    return output

print(soma_itens())
print(soma_itens(10, 20, 30, 40))
print(soma_itens('a', 'b', 'c', 'd'))
print(soma_itens([10, 20, 30], [40, 50, 60], [70, 80]))
print(soma_itens([1], [2], [3]))