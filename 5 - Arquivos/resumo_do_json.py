# RESUMO E CONCATENAÇÃO DO JSON
from zipfile import ZipFile

def processar_arquivo(zip_file, nome_arquivo):
    with zip_file.open(nome_arquivo) as json_file:
        content = json_file.read().decode('utf-8')

        linhas = content.split('\n')

        resultados = []

        for linha in linhas:
            if len(linha) > 0:
                assunto = linha.split()[0][:-1]
                min_value = int(linha.split()[2][:-1])
                max_value = int(linha.split()[4][:-1])
                media = float(linha.split()[6])

                dicionario = {'assunto': assunto, 'min': min_value, 'max': max_value, 'media': media}

                resultados.append(dicionario)

        return resultados

arquivos = ['scores/9b.json', 'scores/9a.json']

resultados_combinados = []

with ZipFile('scores.zip', 'r') as zip:
    print('Nomes dos arquivos: ', zip.namelist())

    for arquivo in arquivos:
        resultados_arquivo = processar_arquivo(zip, arquivo)
        resultados_combinados.extend(resultados_arquivo)


for resultado in resultados_combinados:
    print(resultado)

     
     
   #  ['scores/', 'scores/9b.json', 'scores/9a.json']