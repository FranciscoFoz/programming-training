# LINHAS INVERSAS

def linhas_inversas(input, output):
    with open(input) as infile, open(output, 'w') as outfile:
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]}\n')
            
linhas_inversas('arquivo_linhas_inversas.txt','arquivo_linhas_inversas_convertido.txt')