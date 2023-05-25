#INTRODUÇÃO TWEEPY

import tweepy
import json

with open('/home/franciscofoz/Documents/credentials_twitter.json') as arquivo:
    credenciais = json.load(arquivo)


bearer_token = credenciais['bearer_token']
client = tweepy.Client(bearer_token)

user_ids = [914378883763441664]


users = client.get_users(ids=user_ids, user_fields=["profile_image_url"])
print('-'*20)
for user in users.data:
    print(f'Usuário: {user.username}\nFoto: {user.profile_image_url}')
print('-'*20,2*'\n')
   
tweets = client.get_users_tweets(user_ids[0])

for tweet in tweets.data:
    print(f'ID: {tweet.id}')
    print(f'TWEET: {tweet.text}')
    print('-'*20)
