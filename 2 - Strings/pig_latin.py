#PIG LATIN
'''
Essa função irá verificar se uma string começa com um vogal.
Se começar, ele irá inserir ao final dela a palavra "way".
Se não, irá colocar a primeira letra dela ao final e incluir a palavra "ay".
'''

def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'

    return f'{word[1:]}{word[0]}ay'

palavras  = ['eat','car','computer','love','peace','hippie']

for palavra in palavras:
    print(pig_latin(palavra))



