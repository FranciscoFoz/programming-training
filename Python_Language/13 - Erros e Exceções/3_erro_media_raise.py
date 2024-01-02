# ERRO MÉDIA RAISE
'''
Exercício para tratamento de erros, com "try", "except", "finally" e "except".
'''

def media(lista: list=[0]) -> float:
    ''' 
    Função para calcular a média de notas passadas por uma lista

    lista: list, default[0]
    Lista com as notas para calcular a média
    return calculo: float
    Média calculada
    '''

    calculo = sum(lista) / len(lista)
    
    for i,nota in enumerate(lista):
        if nota > 10:
            raise ValueError(f'A nota deve ter um valor máximo de 10.\nReveja a nota "{nota}" de posição "{i}"')

    return calculo


try:
    notas = [1,2,5,8,10,12]
    resultado = media(notas)
except TypeError:
    print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")
except ValueError as e:
    print(e)
else:
    print(resultado)
finally:
    print(10*'-',"A consulta foi encerrada!",10*'-')
