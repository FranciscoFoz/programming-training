# RESTAURANTE

'''
Esse script irá simular um pedido em um cardápio de um restaurante.

'''

MENU = {'sanduiche': 10, 'chá': 7, 'salada': 9}

def restaurante():
    print(5*'-','CARDÁPIO',5*'-')
    print("{:<15s}{:<10s}".format('PRODUTO','PREÇO'))
    print(20*'-')
    for chave,valor in MENU.items():
        print("{:<15s}{:<10d}".format(chave, valor))
    

    total = 0
    while True: 
        pedido = input('\nEscolha um produto: ').strip() 

        if not pedido: 
            break

        if pedido in MENU: 
            preco = MENU[pedido]
            total += preco
            print(f'{pedido} é {preco}, o total do seu pedido até agora: {total}')

        else:
            print(f'Nós não temos {pedido} hoje.')

    print(f'O seu total é {total}')



restaurante()