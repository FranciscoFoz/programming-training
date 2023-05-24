
import tweepy


bearer_token = "AAAAAAAAAAAAAAAAAAAAAGyzlQEAAAAAnqeH9Wvqr7phCkm%2FJ3fZ4%2FVlciQ%3DQSAqwplfZ0kXj9JE8EYr5i4WmjDKn0IQYXM0QPLOzK0XIl4TQp"
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
