#FOLLOWERS TWEEPY

import tweepy
import json

with open('/home/franciscofoz/Documents/credentials_twitter.json') as arquivo:
    credenciais = json.load(arquivo)


bearer_token = credenciais['bearer_token']
client = tweepy.Client(bearer_token)

user_id = 914378883763441664


followers = client.get_users_followers(
    user_id, max_results=250
)
followers_total = len(followers.data)
print('Total de seguidores:', followers_total)
print('Usernames:\n',10*'-','\n')
for user in followers.data:
    print(f'Username: {user.username}')
