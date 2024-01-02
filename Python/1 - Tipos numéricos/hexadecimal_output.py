#HEXADECIMAL OUTPUT
'''
Essa função irá converter um número hexadecimal em um número decimal.
'''


'''
#Número hexedacimal de do número decimal 6549
0x1995

#Em base 10
9 * 10**0 + 4* 10**1 + 5 * 10**2 + 6 * 10**3 

#Em base 16
5 * 16**0 + 9* 16**1 + 9 * 16**2 + 1 * 16**3 

'''

    
def hex_output():
    total = 0
    hexnum = input('Entre com um número hexadecimal para converter: ')
    for potencia, digito in enumerate(reversed(hexnum)):
        total += int(digito,16) * (16** potencia)
    print(total)
        
hex_output()

