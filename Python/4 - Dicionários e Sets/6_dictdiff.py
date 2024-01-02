# DICTDIFF
"""
Crie uma função que receba dois dicionários e retorne a diferença entre eles.
Caso seja um valor None, retorne o outro valor, caso seja os dois valores None, retorne None.
    
"""

    
def calcular_diferenca(val1, val2):
    if val2 == None:
        return val1
    elif val1 == None:
        return val2
    elif val1 & val2 == None:
        return None
    return val2 - val1

def dictdiff(primeiro, segundo):
    dict_unido = {}
    
    for chave in primeiro.keys() | segundo.keys():
        if primeiro.get(chave) != segundo.get(chave):
            dict_unido[chave] = [primeiro.get(chave),segundo.get(chave)]
    
    dict_unido = dict(sorted(dict_unido.items())) 
    

    for chave, valor in dict_unido.items():
        valor_1, valor_2 = valor
        diferenca = calcular_diferenca(valor_1, valor_2)
        dict_unido[chave] = diferenca
    
            
    return dict_unido

d1 = {'a':1, 'b':2, 'c':3,'e':1}
d2 = {'a':2, 'b':4, 'd':4,'e':10,'f':11}

print(dictdiff(d1,d2))


    