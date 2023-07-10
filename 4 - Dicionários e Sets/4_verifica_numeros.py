# VERIFICA NUMEROS
'''




'''


def verificar_numeros(dicionario):
    for chave, valor in dicionario.items():
        if isinstance(valor, str):
            if valor.isdigit():
                print('\n.isdigit()')
                print(f'O valor "{valor}" na chave "{chave}" é composto apenas por dígitos.')
            elif valor.isnumeric():
                print('\n.isnumeric()')
                print(f'O valor "{valor}" na chave "{chave}" é um número, mas pode conter caracteres especiais.')
            elif valor.isdecimal():
                print('\n.isdecimal()')
                print(f'O valor "{valor}" na chave "{chave}" é um número decimal.')
            else:
                print(f'O valor "{valor}" na chave "{chave}" não é um número válido.')
        else:
            print(f'O valor na chave "{chave}" não é uma string.')


meu_dicionario = {
    'chave1': '123',
    'chave2': '10.5',
    'chave3': 'ABC',
    'chave4': '1000',
    'chave5': '①②③',
    'chave6': '1.5',
    'chave7': '١٢٣'
}

verificar_numeros(meu_dicionario)
