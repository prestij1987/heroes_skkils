

pip install requests

import requests
import json




heroes_data = {}

def get_intelligence(name):
    url = f"https://superheroapi.com/api/{TOKEN}/search/{name}"
    params = {"name": name}
    headers = {"Authorization": TOKEN}
    hero_id = requests.get(url, params=params, headers=headers, timeout=5)
    return hero_id.json()['results'][0]['powerstats']['intelligence']


def the_smartest_hero(heroes_data):
    final_list = []
    max_int = max(heroes_data.values())
    final_dict = {k:v for k, v in heroes_data.items() if v == max_int}
    final_list = list(final_dict.items())    
    return f'The smartest hero is {final_list[0][0]}: {final_list[0][1]} points'


heroes_data['Hulk'] = int(get_intelligence('Hulk'))
heroes_data['Captain America'] = int(get_intelligence('Captain America'))
heroes_data['Thanos'] = int(get_intelligence('Thanos'))



print(the_smartest_hero(heroes_data))

    
Hulk_stats = get_powerstats(Hulk_id)
Capt_stats = get_powerstats(Capt_id)
Thanos_stats = get_powerstats(Thanos_id)

print(Hulk_stats)
print(Capt_stats)
print(Thanos_stats)



# Отдает словарь. Нужно получить всю информацию по ключу
# results, а потом из него получить значения по ключу powerstats.
