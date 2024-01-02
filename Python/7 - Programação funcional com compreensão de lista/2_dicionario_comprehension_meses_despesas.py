# DICIONARIO COMPREHENSION MESES DESPESAS

'''
Crie um dicionário usando o dict comprehension em que as 
chaves estão na lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] 
e os valores estão na lista despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
'''


lista_meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
lista_despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

dicionario = {mes: valor for mes, valor in zip(lista_meses, lista_despesa)}

for i in dicionario.items():
    print(i)