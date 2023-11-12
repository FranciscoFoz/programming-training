# CONTAGEM DE PALAVRAS ARQUIVO

contagem = {'linhas':0,'caracteres':0,'palavras':0,'palavras_unicas':0}

palavras_unicas = set()

with open('arquivo_contagem_de_palavras.txt') as arquivo:
    for linha in arquivo:
        palavras_unicas.update(linha.split())
        contagem['linhas'] += 1
        contagem['caracteres'] += len(linha)
        contagem['palavras'] += len(linha.split())
        
    contagem['palavras_unicas'] = len(palavras_unicas)
        
print(contagem)


