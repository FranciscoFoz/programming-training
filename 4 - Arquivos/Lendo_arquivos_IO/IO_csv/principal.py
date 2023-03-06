
#Método 1
'''
#Leitura do arquivo inteiro armazenado na memória com ".readlines()"


arquivo_spaceship_titanic_train = open('4 - Arquivos/Lendo_arquivos_IO/spaceship_titanic_train.csv')

conteudo = arquivo_spaceship_titanic_train.readlines()

for linha in conteudo:
    print(linha,end='')
'''


#Método 2

'''
#Leitura direta do arquivo, iterando ele para não precisar carregar todo o documento na memória com o ".readline()" ou ".readlines()"

arquivo_spaceship_titanic_train = open('4 - Arquivos/Lendo_arquivos_IO/spaceship_titanic_train.csv')

for linha in arquivo_spaceship_titanic_train:
    print(linha,end='')
'''
#Lendo Arquivo
'''

arquivo_contatos = open('4 - Arquivos/Lendo_arquivos_IO/spaceship_titanic_train_escrita.csv',mode='w')

'''

#Método 3

#Leitura com try-except
'''
try:
    with open('4 - Arquivos/Lendo_arquivos_IO/IO_csv/spaceship_titanic_train_escrita.csv', encoding='latin_1') as titanic_csv:
        for linha in titanic_csv:
            print(linha, end='')

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')
    
'''