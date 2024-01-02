#SEARCH TWEEPY - SALVANDO EM UM CSV

import json
import tweepy
from datetime import datetime, timedelta
import pandas as pd

with open('/home/franciscofoz/Documents/credentials_twitter.json') as arquivo:
    credenciais = json.load(arquivo)

bearer_token = credenciais['bearer_token']
client = tweepy.Client(bearer_token)

string_de_busca = '#Biblioteconomia'

tweets = client.search_recent_tweets(
    string_de_busca,
    expansions=['author_id'],
    tweet_fields=['created_at'],
    max_results=100
)

tweet_data = []

for tweet in tweets.data:
    tweet_datetime = datetime.strptime(str(tweet.created_at), "%Y-%m-%d %H:%M:%S%z")
    brasilia_offset = timedelta(hours=-3)
    
    tweet_datetime_brasilia = tweet_datetime + brasilia_offset
    
    # Obter o nome do usuário do tweet
    users = client.get_user(id=tweet.author_id).data
    username = f'@{users}'
    username_name  = users.name
    
    date_brasilia = tweet_datetime_brasilia.date()
    hora_brasilia = tweet_datetime_brasilia.time()
    tweet_id = tweet.id
    tweet_text = tweet.text
    date_GMT = tweet_datetime.date()
    hora_GMT = tweet_datetime.time()


    tweet_data.append([username,username_name, date_brasilia, hora_brasilia, tweet_id, tweet_text,date_GMT,hora_GMT])
    
   
df = pd.DataFrame(tweet_data, 
                  columns=['username',
                           'username_name',
                           'date_brasilia', 
                           'hora_brasilia', 
                           'tweet_id', 
                           'tweet_text',
                           'date_GMT',
                           'hora_GMT'])

# Adicionar a data atual ao nome do arquivo CSV
data_atual = datetime.now().date().isoformat().replace('-','')

caminho = '/home/franciscofoz/Documents/GitHub/python-training/12 - Pacotes Python/tweepy/tweets_csv'
string_de_busca_formatado = string_de_busca.replace(' ','')
nome_do_arquivo = f'/tweets_{string_de_busca_formatado}_{data_atual}.csv'
output_file = caminho + nome_do_arquivo

# Salvar o DataFrame em um arquivo CSV
df.to_csv(output_file, index=False)

print(f'Tweets salvos em: {output_file}')



