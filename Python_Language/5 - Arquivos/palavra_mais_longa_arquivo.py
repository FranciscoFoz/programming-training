# PALAVRA MAIS LONGA DO ARQUIVO

import os

def palavra_mais_longa(caminho):
    with open(f'{caminho}') as arquivo:
        palavra_mais_longa = ''
        for linha in arquivo:
            for palavra in linha.split():
                if len(palavra) > len(palavra_mais_longa):
                    palavra_mais_longa = palavra
        
        return palavra_mais_longa
    


def procurar_dir_palavra_mais_longa(nome_diretorio):    
    dicionario_palavras =  {filename:palavra_mais_longa(os.path.join(nome_diretorio,filename))
                            for filename in os.listdir(nome_diretorio)
                                if os.path.isfile(os.path.join(nome_diretorio,filename))}
    print(dicionario_palavras)
    
    

procurar_dir_palavra_mais_longa('sample_files_palavra_mais_longa')