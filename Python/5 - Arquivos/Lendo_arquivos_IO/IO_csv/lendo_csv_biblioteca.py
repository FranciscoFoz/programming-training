#Lendo Arquivo CSV

import time

caminho = '/home/franciscofoz/Documents/GitHub/python-training/4 - Arquivos/Lendo_arquivos_IO/IO_csv/dados_exemplo_biblioteca.csv'

# MÉTODO 1
'''
Leitura do arquivo inteiro armazenado na memória com ".readlines()"
'''
def metodo_1():
    tempo_total = 0

    for _ in range(1000):
        tempo_inicial = time.time()
        with open(caminho, 'r') as arquivo_csv:
            conteudo = arquivo_csv.readlines()

            for linha in conteudo:
                print(linha, end='')

        tempo_final = time.time()
        tempo_execucao = tempo_final - tempo_inicial
        tempo_total += tempo_execucao

    tempo_medio = tempo_total / 1000
    print(f'\n\nTEMPO MEDIANO DE EXECUÇÃO: {tempo_medio}') #0.0014434764385223388

# MÉTODO 2
'''
Leitura direta do arquivo, iterando sobre ele para não precisar carregar todo o documento na memória com 
o ".readline()" ou ".readlines()"
'''
def metodo_2():
    tempo_total = 0

    for _ in range(1000):
        tempo_inicial = time.time()
        with open(caminho, 'r') as arquivo_csv:
            for linha in arquivo_csv:
                print(linha, end='')

        tempo_final = time.time()
        tempo_execucao = tempo_final - tempo_inicial
        tempo_total += tempo_execucao

    tempo_medio = tempo_total / 1000
    print(f'\n\nTEMPO MEDIANO DE EXECUÇÃO: {tempo_medio}') #0.0014796361923217773

# PROGRAMA DE LEITURA

print('+-' * 10, 'LEITURA DE ARQUIVO CSV', '-+' * 10, '\n')

escolha_de_metodo = int(input('Escolha o método:\n\n-> Método 1: Digite 1\n\n-> Método 2: Digite 2\n\n'))

while True:
    if escolha_de_metodo == 1:
        metodo_1()
        break
    elif escolha_de_metodo == 2:
        metodo_2()
        break
    else:
        print('ESCOLHA UM NÚMERO: 1 OU 2')
        escolha_de_metodo = int(input('Escolha o método:\n\n-> Método 1: Digite 1\n\n-> Método 2: Digite 2\n\n'))
        continue

print('\n', '+-' * 10, 'FIM DO PROGRAMA', '-+' * 10)
