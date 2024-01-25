#CALCULAR IMPOSTO


from freedonia import calcular_imposto


imposto_as_12am = calcular_imposto(100, 'Harpo', 12)
imposto_as_9pm = calcular_imposto(100, 'Harpo', 21)

print(f'O total de imposto em Harpo às 12h é de : {imposto_as_12am}')
print(f'O total de imposto em Harpo às 9h é de : {imposto_as_9pm}')

imposto_as_9pm = calcular_imposto(100, 'Harpo', -1)