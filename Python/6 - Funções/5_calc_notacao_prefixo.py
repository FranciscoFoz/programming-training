#CALC COM NOTACAO PREFIXO

import operator

def calc(string):
    operacoes = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv,
                 '**': operator.pow,
                 '%': operator.mod}
       
    string_separada = string.split()

    operacao = string_separada[0]
    numeros = string_separada[1:]

    total = float(numeros[0])
    for i in numeros[1:]:
        total = operacoes[operacao](total,float(i))
    
    return total


print('+ 2 3    =   ',calc('+ 2 3'))
print('- 2 3    =   ',calc('- 2 3'))
print('* 2 3    =   ',calc('* 2 3'))
print('/ 2 3    =   ',calc('/ 2 3'))
print('** 2 3    =   ',calc('** 2 3'))
print('% 2 3    =   ',calc('% 2 3'))
print('+ 1 2 3 4 5 6 7 8 9    =   ',calc('+ 1 2 3 4 5 6 7 8 9'))




