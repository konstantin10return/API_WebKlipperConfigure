import requests

from read_write_keys import rad_private


def get_cfg_id():
    with open("cfg_id.txt", 'r', encoding='utf-8') as file:
        content = file.read()
    try:
        return int(content)
    except ValueError:
        print("Не удалось считать id конфигурации из файла cfg_id.txt")
        raise ValueError(f'{content}')


def api_get():
    print(rad_private())
    url = f'https://webklipperconfigure.ru/public_api/config/{get_cfg_id()}/{rad_private()}'
    url = f'http://127.0.0.1:5001/public_api/config/{get_cfg_id()}/{rad_private()}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data["text"]
    else:
        raise BaseException(f'Ошибка api: {response.status_code}')

