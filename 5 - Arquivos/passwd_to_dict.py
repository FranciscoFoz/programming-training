# PASSWD TO DICT

with open('text_etc-passwd_sample.txt',encoding='utf-8') as text:
    for line in text.readlines():
        print(line.strip())