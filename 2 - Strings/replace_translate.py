#REPLACE TRANSLATE
'''
Esse código irá testar o tempo de funções que trocam vogais pela letra x, utilizando replace(), 
maketrans()/tranlate() e um for simples. 
'''
import time
import numpy as np

def replace(palavra):
    for vogal in 'aeiouAEIOU':
        palavra = palavra.replace(vogal, 'x')
        
    return palavra

def translate_maketrans(palavra):
    vogais = 'aeiouAEIOU'
    trans_table = str.maketrans(vogais, 'x'*len(vogais))
    return palavra.translate(trans_table)

def replace_for(palavra):
    nova_palavra = ''
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            nova_palavra += 'x'
        else:
            nova_palavra += letra
    return nova_palavra

palavras  = ['eat','car','computer','love','peace','hippie','WINE','Wind','YESTERDAY','test']
palavras_aleatorias = np.random.choice(palavras,size=1000)


#Teste tempo replace
inicio = time.time()
lista_1 = []
for palavra in palavras_aleatorias:
    replace(palavra).append(lista_1)
fim = time.time()
tempo_replace = fim - inicio

#Teste tempo translate_maketrans
inicio_2 = time.time()
lista_2 = []
for palavra in palavras_aleatorias:
    translate_maketrans(palavra).append(lista_2)
fim_2 = time.time()
tempo_maketrans = fim_2 - inicio_2

#Teste tempo translate_maketrans
inicio_2 = time.time()
lista_2 = []
for palavra in palavras_aleatorias:
    translate_maketrans(palavra).append(lista_2)
fim_2 = time.time()
tempo_maketrans = fim_2 - inicio_2

#Teste tempo replace_for
inicio_3 = time.time()
lista_3 = []
for palavra in palavras_aleatorias:
    replace_for(palavra).append(lista_3)
fim_3 = time.time()
tempo_replace_for = fim_3 - inicio_3


print(f'Tempo replace:{tempo_replace}\nTempo maketrans: {tempo_maketrans}\nTempo replace_for: {tempo_replace_for}')
