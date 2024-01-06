from conta import cria_conta, deposita, saca, extrato

conta = cria_conta(123,'Francisco',10.0,1000)


extrato(conta)

deposita(conta,9)

extrato(conta)

saca(conta,1000)

extrato(conta)