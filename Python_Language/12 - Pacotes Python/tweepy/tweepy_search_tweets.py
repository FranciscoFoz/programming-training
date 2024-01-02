#SEARCH TWEEPY

import json
import tweepy
from datetime import datetime, timedelta

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

total_tweets = 0

for tweet in tweets.data:
    tweet_datetime = datetime.strptime(str(tweet.created_at), "%Y-%m-%d %H:%M:%S%z")
    brasilia_offset = timedelta(hours=-3)
    
    tweet_datetime_brasilia = tweet_datetime + brasilia_offset
    
    # Obter o nome do usuário do tweet
    users = client.get_user(id=tweet.author_id).data
    print(f'USERNAME: @{users}')
    print(f'NOME: {users.name}')
    print(f'Data/Hora - Brasília: {tweet_datetime_brasilia.date()} {tweet_datetime_brasilia.time()}')
    print(f'TWEET ID: {tweet.id}')
    print(f'TWEET: {tweet.text}')
    print(f'Nº TWEET: {total_tweets + 1}')
    print(f'Data/Hora - GMT: {tweet_datetime.date()} {tweet_datetime.time()}')
    print('-' * 30)
    
    total_tweets += 1

