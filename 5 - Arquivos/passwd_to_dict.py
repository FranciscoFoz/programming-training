# PASSWD TO DICT

user_id = dict()
with open('text_etc-passwd_sample.txt',encoding='utf-8') as text:
    for line in text.readlines():
        if not line.startswith('#'):
            linha_separada = line.strip().split(':')
            user_id[linha_separada[0]] = linha_separada[2]
            
print(user_id)