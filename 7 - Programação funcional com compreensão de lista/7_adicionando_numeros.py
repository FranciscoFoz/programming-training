# ADICIONANDO NÚMEROS

def adiciona_numeros(numeros):
    return sum(
                int(numero)
                for numero in numeros.split()
                if numero.isdigit()
                )
    
    
print(adiciona_numeros('1 2 3 a b c 4'))