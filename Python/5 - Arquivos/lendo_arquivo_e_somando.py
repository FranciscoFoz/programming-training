# LENDO ARQUIVO E SOMANDO

'''
Leia o e-mail ('text_sample_2_with_numbers.txt') e some a receita total.
'''

soma_receita_total = 0

with open('/home/franciscofoz/Documents/GitHub/python-training/5 - Arquivos/text_sample_2_with_numbers.txt') as t:
    for linha in t.readlines():
        if 'Receita total' in linha:
            valor = linha.strip().split(' ')[-1].replace('$','').replace(',','')
            soma_receita_total += int(valor)
            
soma_receita_total_formatada = "R$ {:,.2f}".format(soma_receita_total).replace(',','.')[::-1].replace('.',',',1)[::-1]
            
print(f'RECEITA TOTAL = {soma_receita_total_formatada}')
