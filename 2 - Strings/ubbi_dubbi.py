#UBBY DUBBI
'''
Essa função irá receber uma palavra e traduzir ela para Ubby Dubbi.
Ela irá verificar se cada string da palavra possuiu uma vogal e irá 
substituí-la pelo conjunto "ub".
Retornando a palavra modificado como output.
'''

def ubbi_dubbi(palavra):
    output = []
    for letra in palavra:
        if letra in 'aeiou':
            output.append(f'ub{letra}')
    
        else:
            output.append(letra)

    return ''.join(output)

palavras  = ['eat','car','computer','love','peace','hippie','WINE','Wind','YESTERDAY','test']

for palavra in palavras:
    print(ubbi_dubbi(palavra))
