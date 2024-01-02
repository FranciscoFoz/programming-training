# MAP E LIST COMPREHENSION
import timeit
from memory_profiler import profile


numeros = list(range(1, 1000000))


def cubo(x):
    return x**3

def eh_par(x):
    return x % 2 == 0

print(20*'+-','COMPARAÇÃO COM CONDIÇÃO DE FILTRO',20*'+-')

@profile
def usando_map():
    numeros_pares = filter(eh_par, numeros)
    cubos_map = map(cubo, numeros_pares)
    return list(cubos_map)

@profile
def usando_list_comprehension():
    cubos_lista_comp = (cubo(x) 
                        for x in numeros 
                        if eh_par(x))
    return cubos_lista_comp

# Tempo
tempo_map = timeit.timeit(usando_map, number=1)
tempo_lista_comp = timeit.timeit(usando_list_comprehension, number=1)

print(f'Tempo usando map: {tempo_map} segundos')
print(f'Tempo usando list comprehension: {tempo_lista_comp} segundos')

# Memória

'''
Tempo usando map: 1.8650726240002768 segundos
Tempo usando list comprehension: 0.0008711179998499574 segundos

Medição de memória usando map:
Filename: /home/franciscofoz/Documents/GitHub/python-training/7 - Programação funcional com compreensão de lista/6_map_list_comprehesion.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    16     84.4 MiB     84.4 MiB           1   @profile
    17                                         def usando_map():
    18     84.4 MiB      0.0 MiB           1       numeros_pares = filter(eh_par, numeros)
    19     84.4 MiB      0.0 MiB           1       cubos_map = map(cubo, numeros_pares)
    20    108.1 MiB     23.6 MiB           1       return list(cubos_map)



Medição de memória usando list comprehension:
Filename: /home/franciscofoz/Documents/GitHub/python-training/7 - Programação funcional com compreensão de lista/6_map_list_comprehesion.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    22     88.1 MiB     88.1 MiB           1   @profile
    23                                         def usando_list_comprehension():
    24     88.1 MiB      0.0 MiB           2       cubos_lista_comp = (cubo(x) 
    25     88.1 MiB      0.0 MiB           1                           for x in numeros 
    26                                                                 if eh_par(x))
    27     88.1 MiB      0.0 MiB           1       return cubos_lista_comp




'''
print(20*'+-','COMPARAÇÃO SEM CONDIÇÃO DE FILTRO',20*'+-')


@profile
def usando_map():
    cubos_map = map(cubo, numeros)
    return list(cubos_map)


@profile
def usando_list_comprehension():
    cubos_lista_comp = [cubo(x) for x in numeros]
    return cubos_lista_comp

# Tempo
tempo_map = timeit.timeit(usando_map, number=1)
tempo_lista_comp = timeit.timeit(usando_list_comprehension, number=1)

print(f'Tempo usando map: {tempo_map} segundos')
print(f'Tempo usando list comprehension: {tempo_lista_comp} segundos')


'''
Tempo usando map: 1.3616459410000061 segundos
Tempo usando list comprehension: 68.20322773299995 segundos

Medição de memória usando map:
Filename: /home/franciscofoz/Documents/GitHub/python-training/7 - Programação funcional com compreensão de lista/6_map_list_comprehesion.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    76     92.7 MiB     92.7 MiB           1   @profile
    77                                         def usando_map():
    78     92.7 MiB      0.0 MiB           1       cubos_map = map(cubo, numeros)
    79    134.4 MiB     41.8 MiB           1       return list(cubos_map)



Medição de memória usando list comprehension:
Filename: /home/franciscofoz/Documents/GitHub/python-training/7 - Programação funcional com compreensão de lista/6_map_list_comprehesion.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    81     92.7 MiB     92.7 MiB           1   @profile
    82                                         def usando_list_comprehension():
    83    134.4 MiB     41.6 MiB     1000002       cubos_lista_comp = [cubo(x) for x in numeros]
    84    134.4 MiB      0.0 MiB           1       return cubos_lista_comp





'''