#TAMANHO DAS PALAVRAS
'''
Esta função irá:
* receber 3 palavras;
* contará a quantidade de letras em cada uma delas;
* somará o resultado de cada uma delas;
* retornará a impressão de cada uma delas com seu respectivo comprimento e ordenadas da maior para a menor.


'''
def comprimento_palavras(palavra_1,palavra_2,palavra_3):

    palavra_1 = str(palavra_1)
    palavra_2 = str(palavra_2)
    palavra_3 = str(palavra_3)

    lista_palavras = [palavra_1,palavra_2,palavra_3]
    lista_palavras.sort()

    for palavra in lista_palavras:
        print(palavra,len(palavra))
    

comprimento_palavras('cachorro','gato','cobra')
