#LEITURA USUARIOS UNIX

'''
Esse script imprimir os usuários de um sistema UNIX, em ordem alfabética, divididos por shell específico.
'''
from collections import defaultdict

shell_users = defaultdict(list)

with open('/etc/passwd', 'r') as passwd_file:
    lines = passwd_file.readlines()

for line in lines:
    fields = line.split(':')
    username = fields[0]
    shell = fields[6].strip()

    shell_users[shell].append(username)

# Classificar os nomes de usuário alfabeticamente para cada shell
for shell, users in shell_users.items():
    sorted_users = sorted(users)
    print("Shell:", shell,'\n')
    print("Usuários:\n ->",'\n -> '.join(sorted_users))
    print("-"*50)

