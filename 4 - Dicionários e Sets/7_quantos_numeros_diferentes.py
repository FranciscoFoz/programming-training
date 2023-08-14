# QUANTOS NUMEROS DIFERENTES
"""
Crie uma função que identifique a quantidade de números diferentes em uma lista.
"""


def quantos_numeros_diferentes(numeros):
    numeros_unicos = set(numeros)
    return len(numeros_unicos)

numeros = [1,2,3,4,4,3,2,1]

print(quantos_numeros_diferentes(numeros))