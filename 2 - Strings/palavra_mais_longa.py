#PALAVRA MAIS LONGA
'''
Essa função irá receber um texto (string) e retornará a palavra mais longa.
'''

def palavra_mais_longa(texto):

    return sorted(texto.split(),key=len)[-1]


texto = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

palavra_mais_longa(texto)


texto_2 = '''
No meu computador,
o Python habita
e com ele eu desvendo
a lógica infinita

Nas linhas de código
encontro o meu ser
e através da sintaxe
posso me conhecer

As funções e métodos
são como os versos
que em harmonia se unem
formando universos

E como Pessoa disse
somos todos um pouco
no Python me encontro
e me torno outro louco

Louco pela programação
e por tudo que ela traz
em um mundo digital
onde a criatividade jaz

Então que o Python
seja minha poesia
e em cada linha de código
eu encontre a sabedoria.

'''
palavra_mais_longa(texto_2)