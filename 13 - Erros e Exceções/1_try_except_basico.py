# TRY EXCEPT BASICO

while True:
    try:
        x = int(input("Por favor, entre com um número: "))
        break
    except ValueError:
        print("Oops!  Isso não é um número válido.  Tente novamente...")
        