#C
'''
Essa função irá receber uma palavra e traduzir ela para Ubby Dubbi.
Ela irá verificar se cada string da palavra possuiu uma vogal e irá 
substituí-la pelo conjunto "ub".
Retornando a palavra modificado como output.
'''

def replace(palavra):
    for vogal in 'aeiouAEIOU':
        palavra = palavra.replace(vogal, 'x')
        
    return palavra

palavras  = ['eat','car','computer','love','peace','hippie','WINE','Wind','YESTERDAY','test']

for palavra in palavras:
    print(replace(palavra))

#TRANSLATE
#FOR 
# - > COMPARAR TEMPO

#Cifra césar