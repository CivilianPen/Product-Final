import requests

url = 'https://olimp.miet.ru/ppo_it/api'


MAP = []
s= []
for i in range(64):
    response = requests.get(url)
    data = response.json()['message']['data']
    if not data in MAP:
        MAP.append(data)

