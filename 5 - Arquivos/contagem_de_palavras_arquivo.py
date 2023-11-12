# CONTAGEM DE PALAVRAS ARQUIVO

contagem = {'linhas':0,'caracteres':0,'palavras':0,'palavras_unicas':0}

with open('arquivo_contagem_de_palavras.txt') as arquivo:
    for linha in arquivo:
        print(linha,linha.split())
        contagem['linhas'] += 1
        contagem['caracteres'] += len(linha)
        contagem['palavras'] += len(linha.split())
        contagem['palavras'] += len(linha.split())

print(contagem)


# COLOCAR CONTAGEM DE PALAVRAS ÚNICAS