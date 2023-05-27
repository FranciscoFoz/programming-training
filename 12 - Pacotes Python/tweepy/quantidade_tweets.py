# QUANTIDADE TWEETS TWITTER

import json
import tweepy
from datetime import datetime, timedelta
import pandas as pd

with open('/home/franciscofoz/Documents/credentials_twitter.json') as arquivo:
    credenciais = json.load(arquivo)

bearer_token = credenciais['bearer_token']
client = tweepy.Client(bearer_token)


string_de_busca = "biblioteconomia"

response = client.get_recent_tweets_count(string_de_busca, granularity="day")

dicionario_tweets_data = {'data':[],'quantidade':[]}

for count in response.data:
    tweet_start = (datetime.strptime(str(count['start']), "%Y-%m-%dT%H:%M:%S.%fZ") - timedelta(hours=-3)).date().isoformat()
    quantidade = count['tweet_count']
    
    dicionario_tweets_data['data'].append(tweet_start)
    dicionario_tweets_data['quantidade'].append(quantidade)
    

df_tweets_data = pd.DataFrame(dicionario_tweets_data)
total = df_tweets_data['quantidade'].sum()
df_tweets_data['percentual'] = round(df_tweets_data['quantidade'].div(total) * 100,1)

print(df_tweets_data)
print(f'TOTAL={total}')

    