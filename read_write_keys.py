PUB_PATH = 'pub.txt'
PRIVATE_PATH = 'private.txt'


def write_pub(key):
    with open(PUB_PATH, 'wb') as file:
        file.write(key)


def write_private(key):
    with open(PRIVATE_PATH, 'w') as file:
        file.write(key)


def rad_pub():
    with open(PUB_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def rad_private():
    with open(PRIVATE_PATH, 'r', encoding='utf-8') as file:
        content = file.read()
    return content