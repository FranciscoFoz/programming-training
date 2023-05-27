#SEARCH TWEEPY

import json
import tweepy
from datetime import datetime, timedelta

with open('/home/franciscofoz/Documents/credentials_twitter.json') as arquivo:
    credenciais = json.load(arquivo)

bearer_token = credenciais['bearer_token']
client = tweepy.Client(bearer_token)


string_de_busca = 'biblioteconomia -is:retweet'

resultados_por_requisicao = 30  
total_tweets = 0

datas_ultimos_tweets = []

while total_tweets < 30:
    tweets = client.search_recent_tweets(
        string_de_busca,
        expansions=['author_id'],
        tweet_fields=['created_at'],
        max_results=resultados_por_requisicao
    )

    for tweet in tweets.data:
        # Obter o nome do usuário
        users = client.get_user(id=tweet.author_id).data

        print(f'USERNAME: {users}')
        print(f'Data/Hora: {tweet.created_at.date()} {tweet.created_at.time()}')
        print(f'TWEET ID: {tweet.id}')
        print(f'TWEET: {tweet.text}')
        print(f'Nº TWEET: {total_tweets + 1}')

        print(f'DATA: {tweet.created_at}')
        print('-' * 30)

        datas_ultimos_tweets.append(tweet.created_at)  

        total_tweets += 1

        if total_tweets >= 30:
            break

    # Obtém a data do último tweet da lista para usar como ponto de partida para a próxima requisição
    data_ultimos_tweet = min(datas_ultimos_tweets)

    data_minima = data_ultimos_tweet + timedelta(seconds=1)

    # Define os parâmetros para buscar os próximos tweets com base na última data
    params = {
        "query": "Biblioteconomia",
        "expansions": ["author_id"],
        "tweet_fields": ["created_at"],
        "max_results": resultados_por_requisicao,
        "end_time": data_minima.isoformat()
    }

    # Realiza a próxima requisição de tweets
    tweets = client.search_recent_tweets(**params)
