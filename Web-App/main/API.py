import requests

url = 'https://olimp.miet.ru/ppo_it/api'

response = requests.get(url)

print(requests.content)