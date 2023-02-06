#ADIVINHACAO

import random 

def adivinhacao():
    nome = input('Digite seu nome: ')
    print(f'Olá {nome}')

    numero = random.randint(0, 100)
    print(numero)


    while True:
        palpite = int(input('Adivinhe um número entre 1 a 100 '))
        if palpite == numero:
            print(f'Você acertou! :D')
            break
        if palpite > 100:
            print('Digite um número menor que 100')
        if palpite < 0:
            print('Digite um número maior que 0')
        if palpite < numero:
            print(f'Seu palpite de {palpite} está abaixo!')
        if palpite > numero:
            print(f'Seu palpite de {palpite} está acima!')

            
adivinhacao()