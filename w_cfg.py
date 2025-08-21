import os

import api_get


def get_path():
    with open("cfg_path.txt", 'r', encoding='utf-8') as file:
        content = file.read()
        if content[-1] == '\n':
            content = content[:-1]
    return os.path.expanduser(content)


def write_cfg(content):
    with open(get_path(), 'w') as file:
        file.write(content)


def reload_printer_cfg():
    content = api_get.api_get()
    write_cfg(content)
