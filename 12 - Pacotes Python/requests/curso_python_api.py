# Curso: Python e APIs: conhecendo a biblioteca Requests

import requests
import pandas as pd

## 1. CONHECENDO A REQUESTS

#r = requests.get('https://api.github.com/events')

#print(r)
#print(r.text)


### EXERCICIO
'''
Com o objeto response retornado pela requisição, imprima na tela as seguintes informações sobre a requisição:

* status code da requisição, para analisar se foi bem sucedida ou não;
* conteúdo da requisição, para conferir se os dados de usuário vieram corretamente;
* URL da requisição feita, para garantir que a url utilizada na requisição foi a correta.

Após conferir isso, analise novamente o conteúdo retornado pela requisição e imprima na tela apenas as seguintes informações sobre a pessoa usuária em questão:

Nome
Nome de usuário
Número de repositórios públicos
Data de criação da conta no GitHub

'''

# github_franciscofoz = 'https://api.github.com/users/FranciscoFoz'

# r = requests.get(github_franciscofoz)

# print(f'Status: {r.status_code}\n')
# print(f'URL: {r.url}\n')
# print(f'Conteúdo:\n {r.json()}')


# print(f'Nome: {r.json()["login"]}\n')
# print(f'Nome de usuário: {r.json()["name"]}\n')
# print(f'Número de repositórios públicos:{r.json()["public_repos"]}\n')
# print(f'Data da criação da conta: {r.json()["created_at"]}')



## 2. EXTRAINDO DADOS

api_base_url = 'https://api.github.com'
owner = 'amzn'
url = f'{api_base_url}/users/{owner}/repos'


access_token = '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'
headers = {'Authorization': 'Bearer ' + access_token,
           'X-GitHub-Api-Version': '2022-11-28'}


# r = requests.get(url,headers=headers)


# repos_list = []
# for page_num in range(1, 6):
#     try:
#         url_page = f'{url}?page={page_num}'
#         response = requests.get(url_page, headers=headers)
#         repos_list.append(response.json())
#     except:
#         repos_list.append(None)

# page = 1
# followers_list = []

# ## 3. TRANSFORMANDO DADOS

# repos_name = []
# for page in repos_list:
#     for repo in page:
#         repos_name.append(repo['name'])

# repos_language = []
# for page in repos_list:
#     for repo in page:
#         repos_language.append(repo['language'])
    
# dados_amz = pd.DataFrame()
# dados_amz['repository_name'] = repos_name
# dados_amz['language'] = repos_language

# dados_amz['language'].fillna('NULL')


## 4. ARMAZENANDO OS DADOS

# api_base_url = 'https://api.github.com'
# url = f'{api_base_url}/user/repos'

# data = {
#     'name': 'linguagens-utilizadas',
#     'description': 'Repositorio com as linguagens de prog da Amazon',
#     'private': False
# }

# response = requests.post(url, json=data, headers=headers)
# print(response.status_code)



## 5. ESTRUTURANDO OS DADOS

# class DadosRepositorios:

#     def __init__(self, owner):
#         self.owner = owner
#         self.api_base_url = 'https://api.github.com'
#         self.access_token= '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'
#         self.headers = {'Authorization':'Bearer ' + self.access_token,
#                         'X-GitHub-Api-Version': '2022-11-28'}

#     def lista_repositorios(self):
#         repos_list = []

#         for page_num in range(1, 20):
#             try:
#                 url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
#                 response = requests.get(url, headers=self.headers)
#                 repos_list.append(response.json())
#             except:
#                 repos_list.append(None)
        
#         return repos_list
    
#     def nomes_repos(self, repos_list):
#         repo_names=[]
#         for page in repos_list:
#             for repo in page:
#                 try:
#                     repo_names.append(repo['name'])
#                 except:
#                     pass

#         return repo_names
    
#     def nomes_linguagens(self, repos_list):
#         repo_languages=[]
#         for page in repos_list:
#             for repo in page:
#                 try:
#                     repo_languages.append(repo['language'])
#                 except:
#                     pass

#         return repo_languages
    
#     def cria_df_linguagens(self):

#         repositorios = self.lista_repositorios()
#         nomes = self.nomes_repos(repositorios)
#         linguagens = self.nomes_linguagens(repositorios)

#         dados = pd.DataFrame()
#         dados['repository_name'] = nomes
#         dados['language'] = linguagens

#         return dados  
    
# amazon_rep = DadosRepositorios('amzn')
# ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()


# netflix_rep = DadosRepositorios('netflix')
# ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

# spotify_rep = DadosRepositorios('spotify')
# ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()


# ling_mais_usadas_amzn.to_csv('dados/linguagens_amzn.csv')
# ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv')
# ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv')

owner = 'FranciscoFoz'
repo = 'linguagens-utilizadas'
url = f'https://api.github.com/{owner}/{repo}'

response = requests.delete(url,headers=headers)
print(response)
