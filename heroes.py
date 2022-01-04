from pprint import pprint

import requests

dict_comparison = dict()


def get_a_seperhero():
    max = 0
    url = "https://www.superheroapi.com/api.php/2619421814940190/search/Hulk"
    response = requests.get(url)
    dict = (response.json())
    for el in dict['results']:
        if el['name'] == 'Hulk':
            intelligence_Hulk = el['powerstats']['intelligence']
            dict_comparison[el['name']] = intelligence_Hulk
            if max < int(intelligence_Hulk):
                max = int(intelligence_Hulk)
    url = "https://www.superheroapi.com/api.php/2619421814940190/search/Captain America"
    response = requests.get(url)
    dict = (response.json())
    for el in dict['results']:
        intelligence_Captain_America = el['powerstats']['intelligence']
        dict_comparison[el['name']] = intelligence_Captain_America
        if max < int(intelligence_Captain_America):
            max = int(intelligence_Captain_America)
    url = "https://www.superheroapi.com/api.php/2619421814940190/search/Thanos"
    response = requests.get(url)
    dict = (response.json())
    for el in dict['results']:
        intelligence_Thanos = el['powerstats']['intelligence']
        dict_comparison[el['name']] = intelligence_Thanos
        if max < int(intelligence_Thanos):
            max = int(intelligence_Thanos)
    for keys,values in dict_comparison.items():
        if values == str(max):
            pprint (keys)

get_a_seperhero()