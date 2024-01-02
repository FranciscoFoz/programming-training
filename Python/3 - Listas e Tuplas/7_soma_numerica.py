#SOMA NUMÉRICA
'''
Essa função irá somar todos os itens numéricos que ela receber, independente se for uma string ou não.
Caso seja uma string com letras ou uma lista ela irá imprimir uma mensagem informando que elas foram ignoradas.
'''

def soma_numerica(*itens):
    total = 0
    for item in itens:
        try:
            total += int(item)
        except (ValueError):
            print('Esse argumento continha uma string com letras e foi ignorado')
            pass
        except (TypeError):
            print('Esse argumento continha uma lista e foi ignorada')
            pass
    return itens, total

print(soma_numerica(10, 20, 30, 40))
print(10*'-')
print(soma_numerica(10, 20, 30,'a', 40))
print(10*'-')
print(soma_numerica(10, 20, 30,'20', 40))
print(10*'-')
print(soma_numerica(10, 20, 30,[20], 40))
