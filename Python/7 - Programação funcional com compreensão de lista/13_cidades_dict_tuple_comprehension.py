# CIDADES DICT TUPLE COMPREHENSION
import requests as r
from collections import Counter


url = 'https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json'

cidades = r.get(url).json()

dict_cidade = {cidade['city']: cidade['population'] for cidade in cidades}

print(f'Quantidade de cidades no dicionário: {len(dict_cidade.keys())}')


tupla_cidade = tuple((cidade['city'], cidade['population']) for cidade in cidades)

print(f'Quantidade de cidades no dicionário: {len(tupla_cidade)}')

nomes_cidades = sorted([cidade['city'] for cidade in cidades])



contador = Counter(nomes_cidades)

itens_duplicados = {item: count for item, count in contador.items() if count > 1}

print(f'Quantidade de cidades duplicadas = {len(itens_duplicados.keys())}\nQuantidade de items duplicados = {sum(itens_duplicados.values())}')
print(f'137 - 62 = {137-62}')
for item, quantidade in itens_duplicados.items():
    print(f"{item:<{13}}{15*'-'} está duplicado {quantidade} vezes na lista.")

