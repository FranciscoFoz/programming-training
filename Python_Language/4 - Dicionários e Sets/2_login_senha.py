# LOGIN E SENHA

'''
Crie um dicionário no qual as chaves são nomes de usuário e os valores são senhas, ambos representados
como strings. 
Crie um minúsculo sistema de login, no qual o usuário deve inserir um nome de usuário e
senha. 
Se houver uma correspondência, indique que o usuário fez login com sucesso. 
Caso contrário,recuse a entrada.
'''

SISTEMA_LOGIN = {'franciscofoz': 'foz1234','chriscornell':'cornell2521'}

def login():
    while True:
        usuario = input("Digite seu login...\n(ou 'sair' para sair): ")

        if usuario.lower() == "sair":
            print("Saindo do sistema de login...")
            break 
        
        if usuario in SISTEMA_LOGIN.keys():
            print("Usuário validado!")
        else:
            print("Usuário incorretos. Tente novamente.")

        while True:
            senha = input("Digite sua senha: ")

            if senha == SISTEMA_LOGIN[usuario]:
                print("Login realizado com sucesso!")
                break  
            else:
                print("Senha incorreta. Tente novamente.")
        break
    
login()