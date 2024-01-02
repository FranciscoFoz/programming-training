#PALAVRA COM A LETRA MAIS REPETIDA

'''
Esse script receberá uma lista de strings no qual, no qual irá contar a quantidade de letras que mais repetem em cada uma
e depois retornará a string que tiver a maqior quantidade de letras repetidas.
'''
from collections import Counter

palavras = ['algoritmo', 'dados', 'inteligência artificial', 'criptografia', 'segurança']


def contador_de_letra_que_mais_repete(palavra):
    
    return Counter(palavra).most_common(1)[0][1]

def palavra_com_letras_que_mais_repetem(palavras):
    
    return max(palavras,key=contador_de_letra_que_mais_repete)



for palavra in palavras:
    print(f'{palavra}: {contador_de_letra_que_mais_repete(palavra)}')


print(f'\n----> A palavra que tem a letra que mais repete é: {palavra_com_letras_que_mais_repetem(palavras)}\n')