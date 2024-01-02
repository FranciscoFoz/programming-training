#ORDENACAO DE STRING
'''
Essa função irá receber uma string e retornará ela ordenada pela sua ordenação Unicode.
'''

def strsort(a_string):

    return ''.join(sorted(a_string))

print(strsort('dcba'))
