import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
response_json = response.json()

heroes = ['Hulk', 'Captain America', 'Thanos']
intelligence = 0
smartest_hero = ''

for hero in response_json:
    if hero['name'] in heroes:
        hero_intelligence = int(hero['powerstats']['intelligence'])
        if hero_intelligence > intelligence:
            intelligence = hero_intelligence
            smartest_hero = hero['name']

print(f'Самый умный супергерой - {smartest_hero}. Его интеллект - {intelligence}.')
