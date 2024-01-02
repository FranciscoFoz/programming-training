# PRECIPITACAO

'''
Neste desafio, você será responsável por criar um programa em Python para registrar a quantidade de 
precipitação (chuva) por cidade. 

O programa permite que você insira o nome da cidade e a quantidade de milímetros de chuva registrados.
O código começa definindo a função pegue_precipitacao(), que inicializa um dicionário vazio chamado precipitacao.
Em seguida, entra em um loop infinito, onde você é solicitado a fornecer o nome da cidade. 
Se você deixar o campo em branco, o loop será interrompido.

Após fornecer o nome da cidade, você será solicitado a inserir a quantidade de milímetros de chuva registrados nessa cidade.
O valor inserido é somado ao valor existente no dicionário precipitacao para a cidade correspondente.

Depois que você terminar de inserir os dados, o programa exibirá as cidades e as respectivas quantidades de chuva registradas.
'''

def pegue_precipitacao():
    precipitacao = {}
    while True:
        nome_cidade = input('Entre com o nome da cidade: ')
        if not nome_cidade:
            break 
        
        try:
            chuva_mm = int(input('Entre com os mm da chuva: '))
        except ValueError:
            print('Você não inseriu um número inteiro.\nTente novamente....\n\n')
            continue
        
        precipitacao[nome_cidade] = precipitacao.get(nome_cidade,0) + int(chuva_mm)
        
    
    for cidade, chuva in precipitacao.items():
        print(f'{cidade}: {chuva}')


pegue_precipitacao()
