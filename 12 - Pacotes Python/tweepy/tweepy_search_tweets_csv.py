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


results_per_request = 10 
total_tweets = 40

data_ultimos_tweets = []

while total_tweets < 40:
    tweets = client.search_recent_tweets(
        termo_de_busca,
        expansions=['author_id'],
        tweet_fields=['created_at'],
        max_results=results_per_request
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
        print('-' * 20)

        data_ultimos_tweets.append(tweet.created_at) 

        total_tweets += 1

        if total_tweets >= 40:
            break

    # Obtém a data do último tweet da lista para usar como ponto de partida para a próxima requisição
    data_ultimos_tweets = min(data_ultimos_tweets)

    # Define a data mínima para buscar tweets posteriores à última data
    data_min = data_ultimos_tweets + timedelta(seconds=1)

    # Define os parâmetros para buscar os próximos tweets com base na última data
    query_params = {
        "query": "Biblioteconomia",
        "expansions": ["author_id"],
        "tweet_fields": ["created_at"],
        "max_results": results_per_request,
        "end_time": data_min.isoformat()
    }

    # Realiza a próxima requisição de tweets
    tweets = client.search_recent_tweets(**query_params)
    
# CONTINUAR REFATORANDO


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

