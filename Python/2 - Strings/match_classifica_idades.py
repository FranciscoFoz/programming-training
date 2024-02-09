# MATCH - CLASSIFICAR IDADES

idade = int(input('Qual a sua idade?'))

match idade:
    case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11:
        print('Criança')
    case 12 | 13 | 14 | 15 | 16 | 17:
        print('Adolescente')
    case _:
        print('Adulto')
    