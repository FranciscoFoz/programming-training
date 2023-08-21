# QUANTOS IP'S DIFERENTES
"""
Você recebeu a tarefa de analisar um arquivo de log de um servidor da web (por exemplo, Apache ou nginx) 
para identificar os diferentes endereços IP que tentaram acessar o servidor. 

O arquivo de log contém registros de cada solicitação ao servidor, 
incluindo o endereço IP do cliente que fez a solicitação.

Sua tarefa é criar um programa em Python que lê o arquivo de log, 
identifica os endereços IP únicos e exibe uma lista desses endereços.

Exemplo de log:

'''
2023-08-21 12:01:45 192.168.1.1 - GET /page1.html
2023-08-21 12:02:10 192.168.1.2 - GET /page2.html
2023-08-21 12:02:30 192.168.1.3 - GET /page1.html
2023-08-21 12:03:05 192.168.1.1 - GET /page3.html
2023-08-21 12:03:15 192.168.1.4 - GET /page4.html
2023-08-21 12:03:25 192.168.1.2 - GET /page2.html
'''

"""
import re

def extrair_ip_unico(log):
    ips_unico = set()

    for line in log.split('\n'):
        match = re.search(r'\d+\.\d+\.\d\.\d', line)
        if match:
            ips_unico.add(match.group())

    print(f"IP's únicos: {ips_unico}")

log = '''
2023-08-21 12:01:45 192.168.1.1 - GET /page1.html
2023-08-21 12:02:10 192.168.1.2 - GET /page2.html
2023-08-21 12:02:30 192.168.1.3 - GET /page1.html
2023-08-21 12:03:05 192.168.1.1 - GET /page3.html
2023-08-21 12:03:15 192.168.1.4 - GET /page4.html
2023-08-21 12:03:25 192.168.1.2 - GET /page2.html
'''


extrair_ip_unico(log)

