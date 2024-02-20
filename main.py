import requests


ARTICLE_IDS = ['Лондон', 'Шереметьево', 'Череповец']


if __name__ == "__main__":
    for article_id in ARTICLE_IDS:
        url = f'https://wttr.in/{article_id}?nTqmM&lang=ru'
        response = requests.get(url)
        print(response.text)