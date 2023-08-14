# TRY EXCEPT E FINALLY

while True:
    try:
        x = int(input("Por favor, entre com um número: "))
        print(20*'-','NÚMERO INSERIDO',20*'-')
        break
    except ValueError:
        print("Oops!  Isso não é um número válido.  Tente novamente...\n")
    finally:
        print(10*'-','Programação exige treino... nunca pare de treinar.',10*'-')
