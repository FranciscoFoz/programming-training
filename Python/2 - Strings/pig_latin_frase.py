#PIG LATIN FRASE
'''
Essa função irá receber um frase e traduzir ela para Pig Latin.
Ela irá verificar se cada string da palavra começa com um vogal.
Se começar, ele irá inserir ao final dela a palavra "way".
Se não, irá colocar a primeira letra dela ao final e incluir a palavra "ay".
'''

def pig_latin_sentence(sentence):
    output = []
    for word in sentence.split():       
        if word[0] in 'aeiouAEIOU':
            if word[-1].isupper():
                output.append(f'{word}WAY')
            else:
                output.append(f'{word}way')

        else:
            output.append(f'{word[1:]}{word[0]}ay')
            
    return output

pig_latin_sentence('Every reader his or her book')  


