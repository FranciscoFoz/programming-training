# FINAL LINE
'''
Escreva uma função (get_final_line) que receba um nome de arquivo como argumento. 
A função deve retornar a linha final desse arquivo na tela.
'''

from io import StringIO

fakefile = StringIO('''
nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
''')

def get_final_line(filename):
    final_line = ''
    for current_line in filename:
        final_line = current_line
    return final_line

#print(get_final_line('/etc/passwd'))

with open('/home/franciscofoz/Documents/GitHub/python-training/5 - Arquivos/text_sample.txt') as t:
    print(get_final_line(t))
