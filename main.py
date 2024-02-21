import requests
import logging


logging.basicConfig(level=logging.INFO)


def main():
    article_ids = ['Лондон', 'Шереметьево', 'Череповец']
    for article_id in article_ids:
        params = {'nTqmM': '', 'lang': 'ru'}
        url = f'https://wttr.in/{article_id}'
        response = requests.get(url, params=params)

        if response.ok:
            print(response.text)
        else:
            logging.error(f'Ошибка при получении данных для {article_id}. HTTP статус: {response.status_code}')


if __name__ == "__main__":
    main()