from conta import Conta


conta = Conta(123,'Francisco',55.5,1000.0)

conta.extrato()

conta.deposita(15)
conta.extrato()

conta.saca(20)
conta.extrato()


conta2 = Conta(321,'Isis',1001.0,1000.0)

conta.transfere(50,conta2)

conta.extrato()
conta2.extrato()


print(conta.limite)