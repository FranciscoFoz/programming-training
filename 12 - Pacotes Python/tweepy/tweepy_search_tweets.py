#SEARCH TWEEPY

import json
import tweepy
from datetime import datetime

with open('/home/franciscofoz/Documents/credentials_twitter.json') as arquivo:
    credenciais = json.load(arquivo)

bearer_token = credenciais['bearer_token']
client = tweepy.Client(bearer_token)

user_id = 914378883763441664

tweets = client.search_recent_tweets("Biblioteconomia", expansions=['author_id'],tweet_fields=['created_at'])
# Cada objeto Tweet tem os campos padrão ID e text
for tweet in tweets.data:
    # Obter o nome do usuário
    users = client.get_user(id=tweet.author_id).data
    
    print(f'USERNAME: {users}')
    print(f'Data/Hora: {tweet.created_at.date()} {tweet.created_at.time()}')
    print(f'TWEET ID: {tweet.id}')
    print(f'TWEET: {tweet.text}')
    
    # Verificar se o tweet possui localização
    if 'place' in tweet:
        place = tweet.place
        print(f'PLACE: {place}')
    else:
        print(f'PLACE: NOT')
    print('-'*20)
    