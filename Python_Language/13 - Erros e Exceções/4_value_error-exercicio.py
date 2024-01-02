# VALUE ERROR - EXERCÍCIO

'''
Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses números. 
O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.

'''

def divisao():
    try:
        num_1 = float(input("Digite o primeiro número: "))
        num_2 = float(input("Digite o segundo número: "))
        
        resultado = num_1 / num_2
        
        print(f"O resultado da divisão é: {resultado}")
    
    except ValueError:
        print("Erro: Digite números válidos.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except Exception as e:
        print(f"Erro desconhecido: {e}")
        
divisao()