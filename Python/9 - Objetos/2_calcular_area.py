# CALCULAR AREA


'''
Crie uma classe chamada Retangulo com os seguintes atributos: base e altura.

Em seguida, crie um método chamado calcular_area que calcula e retorna a área do retângulo (base * altura).

Por fim, crie um objeto da classe Retangulo, defina os valores dos atributos e 
chame o método calcular_area para exibir a área do retângulo.

'''


class Retangulo:
    
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        area = self.base * self.altura
        print(f'A área do retangulo é de {area} m²')
        
Retangulo(5,10).area()
Retangulo(7,7).area()
Retangulo(9,10).area()