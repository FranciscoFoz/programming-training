
class Conta:
    
    def __init__(self,numero, titular, saldo, limite):
        print('Construindo objeto... {}'.format(self))
        
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta(123,'Francisco',55.5,1000.0)
conta.saldo

conta2 = Conta(124,'Tadeu',65.0,1000.0)

def cria_conta(numero, titular, saldo, limite):
   conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
   return conta

def deposita(conta, valor):
    conta['saldo'] += valor
    

def saca(conta, valor):
    conta['saldo'] -= valor
    
def extrato(conta):
    print(f"Saldo é {conta['saldo']}")