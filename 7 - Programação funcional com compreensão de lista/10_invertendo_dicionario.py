# INVERTENDO UM DICIONÁRIO

def invertendo_dicionario(a_dict):
    return {valor: chave
            for chave, valor in a_dict.items()}


print(invertendo_dicionario({'a':1, 'b':2, 'c':3}))
