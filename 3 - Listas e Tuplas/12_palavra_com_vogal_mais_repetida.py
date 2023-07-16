#PALAVRA COM A VOGAL MAIS REPETIDA

'''
Esse script receberá uma lista de strings no qual, no qual irá contar a quantidade de vogais que mais repetem em cada uma
e depois retornará a string que tiver a maior quantidade de vogais repetidas.
'''
from collections import Counter

palavras = ['Eucalipto', 'Carvalho', 'Bordo', 'Jacarandá', 'Cipreste']


def contador_de_letra_que_mais_repete(palavra):
    
    palavra = palavra.lower()
    
    return sum(Counter(letra for letra in palavra if letra in 'aeiou').values())

def palavra_com_letras_que_mais_repetem(palavras):
    
    return max(palavras,key=contador_de_letra_que_mais_repete)



for palavra in palavras:
    print(f'{palavra}: {contador_de_letra_que_mais_repete(palavra)}')


print(f'\n----> A palavra que tem a vogal que mais repete é: {palavra_com_letras_que_mais_repetem(palavras)}\n')


        


