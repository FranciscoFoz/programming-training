# LENDO ARQUIVO E SOMANDO

'''
Leia o e-mail ('text_sample_2_with_numbers.txt') e some a receita total.
'''

with open('/home/franciscofoz/Documents/GitHub/python-training/5 - Arquivos/text_sample_2_with_numbers.txt') as t:
    for linha in t.readlines():
        print(linha)