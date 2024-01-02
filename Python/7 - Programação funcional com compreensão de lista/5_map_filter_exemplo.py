# MAP FILTER EXEMPLOS

# map: plica uma função a cada elemento de uma sequência e retorna uma nova sequência com os resultados.
palavras = 'this is a bunch of words'.split()
print('Palavras: ',palavras)

x = map(len, palavras)
print(sum(x))

# filter: filtra os elementos de uma sequência com base em uma função que retorna.
def isso_eh_uma_palavra_longa(uma_palavra):
    return len(uma_palavra) > 4

x = filter(isso_eh_uma_palavra_longa, palavras)
print(' '.join(x))