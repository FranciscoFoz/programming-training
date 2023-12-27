# TRANSFORMAR VALORES

def transformar_valores(func, dicionario):
    return {key: func(value) for key,
            value in dicionario.items()}

d = {'a':1, 'b':2, 'c':3}
print(transformar_valores(lambda x: x*x, d))