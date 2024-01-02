# DICTUNION
"""
Crie uma função que receba dois dicionários e retorne a união entre eles.
    
"""


def dictunion(primeiro, segundo):
    output = {}
    todas_chaves = primeiro.keys() | segundo.keys()
    for chave in todas_chaves:
        if primeiro.get(chave) != segundo.get(chave):
            output[chave] = [primeiro.get(chave),segundo.get(chave)]
    
    output = dict(sorted(output.items())) 
            
    return output

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':2, 'b':4, 'd':4}

print(dictunion(d1,d2))

