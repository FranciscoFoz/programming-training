# VALORES - APARTAMENTOS

'''
Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla
caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:
'''

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

print([i[1] for i in aluguel if i[0] == 'Apartamento'])
