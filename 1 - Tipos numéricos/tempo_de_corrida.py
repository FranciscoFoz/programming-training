#TEMPO DE CORRIDA

'''
Esta função irá:
* receber o tempo médio de "corridas" do usuário;
* calcular o tempo médio das "corridas", convertendo em formato decimal;
* após não inserir mais nenhuma corrida ela retornará com o tempo médio das corridas e o número total de corridas.

'''
from decimal import *

def tempo_corrida():

    numero_corridas = 0
    tempo_total = 0
    
    while True:
        primeira_corrida = input('Entre com o tempo (em minutos) da sua corrida de 10 km: ')
        if not primeira_corrida:
            break
        numero_corridas += 1
        tempo_total += float(Decimal(primeira_corrida))
    
    average_time = tempo_total / numero_corridas
    
    print(f'O tempo médio foi de {average_time} minutos, para um total de {numero_corridas} corridas')
    
tempo_corrida()
