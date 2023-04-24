#PRIMEIRO ULTIMO
'''
Essa função irá receber um objeto e retornará o primeiro e último elemento dela.
'''

def primeiro_ultimo(x):
    
    return x[:1]+x[-1:]

primeiro_ultimo('abc')
primeiro_ultimo([1,2,3,4,5])
primeiro_ultimo([i for i in range(1,100)])
primeiro_ultimo(('Francisco','Tadeu','Foz'))


