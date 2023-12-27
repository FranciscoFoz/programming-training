# PIG LATIN TRADUCAO

def plword(word):
    if word[0] in 'aeiou':
        return word + 'way'
    return word[1:] + word[0] + 'ay'

def plfile(filename):
    return ' '.join(
        plword(one_word)
        for one_line in open(filename)
        for one_word in one_line.split()
        )
    
print(plfile('/home/franciscofoz/Documents/GitHub/python-training/5 - Arquivos/arquivo_linhas_inversas_convertido.txt'))