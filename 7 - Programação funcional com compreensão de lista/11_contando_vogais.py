# CONTANDO VOGAIS

# CONTANDO VOGAIS

def contando_vogais(texto):
    return {palavra: sum(1 for letra in palavra.lower() if letra in 'aeiou') 
            for palavra in texto.split()}

frase = 'A beleza da vida está nas pequenas alegrias que encontramos todos os dias.'
print(contando_vogais(frase))
