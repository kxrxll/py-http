import requests
from pprint import pprint
from ya_uploader import YaUploader


def get_heroes_list():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    return response.json()


def find_and_print_max_intelligent_hero_name(arr):
    max_intelligent_hero = max(arr, key=lambda x: x["powerstats"]["intelligence"])
    max_intelligent_hero_name = max_intelligent_hero["name"]
    max_intelligent_hero_intelligence = max_intelligent_hero["powerstats"]["intelligence"]
    pprint(f"The most intelligent hero is {max_intelligent_hero_name}, \
his intelligence is {max_intelligent_hero_intelligence}")


if __name__ == '__main__':
    heroes_list = get_heroes_list()
    find_and_print_max_intelligent_hero_name(heroes_list)
    token = "AQAAAAA4K3AyAADLW79VZaDx1kQyjL2smqCwFQE"
    ya_uploader = YaUploader(token)
    ya_uploader.upload('/Загрузки/test.txt', "./ya_disk/test.txt")
