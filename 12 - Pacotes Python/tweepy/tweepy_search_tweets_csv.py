#SEARCH TWEEPY - SALVANDO EM UM CSV

import json
import tweepy
from datetime import datetime
import pandas as pd

with open('/home/franciscofoz/Documents/credentials_twitter.json') as arquivo:
    credenciais = json.load(arquivo)

bearer_token = credenciais['bearer_token']
client = tweepy.Client(bearer_token)

user_id = 914378883763441664

termo_de_busca = 'biblioteconomia'

tweets = client.search_recent_tweets(termo_de_busca, expansions=['author_id'],tweet_fields=['created_at'],max_results=100)

tweet_data = []

# Cada objeto Tweet tem os campos padrão ID e text
for tweet in tweets.data:
    # Obter o nome do usuário
    users = client.get_user(id=tweet.author_id).data

    username = users.name
    date = tweet.created_at.date()
    time = tweet.created_at.time()
    tweet_id = tweet.id
    tweet_text = tweet.text

    tweet_data.append([username, date, time, tweet_id, tweet_text])

# Criar um DataFrame do Pandas com os dados dos tweets
df = pd.DataFrame(tweet_data, columns=['Username', 'Date', 'Time', 'Tweet ID', 'Tweet'])

# Adicionar a data atual ao nome do arquivo CSV
data_atual = datetime.now().date().isoformat().replace('-','')

caminho = '/home/franciscofoz/Documents/GitHub/python-training/12 - Pacotes Python/tweepy/tweets_csv'
nome_do_arquivo = f'/tweets_{termo_de_busca}_{data_atual}.csv'
output_file = caminho + nome_do_arquivo


# Salvar o DataFrame em um arquivo CSV
df.to_csv(output_file, index=False)

print(f'Tweets salvos em: {output_file}')
