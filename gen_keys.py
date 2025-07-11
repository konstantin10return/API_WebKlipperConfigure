import time
import random

import bcrypt

import read_write_keys

EXTRA_CHARS_COUNT = 40
CHARS = 'qwertyuiop[]asdfghjkl;)zxcvbnm<>@!*-+\\0123456789(.{}'


def gen_private_key():
    rez = str(time.time()) + '_'
    for _ in range(EXTRA_CHARS_COUNT):
        possible_chars = random.sample(list(CHARS), len(CHARS))
        while len(possible_chars) >= 2:
            random.shuffle(possible_chars)
            if random.choice([True, False]):
                possible_chars = possible_chars[random.randint(0, len(possible_chars) - 1):]
            else:
                possible_chars = possible_chars[:random.randint(1, len(possible_chars))]
            if random.choice([True, False]):
                random.shuffle(possible_chars)

        rez += possible_chars[0]
    return rez


def gen_pub_key(private_key):
    return bcrypt.hashpw(private_key.encode(), bcrypt.gensalt())


def regen_keys():
    private = gen_private_key()
    public = gen_pub_key(private)
    read_write_keys.write_private(private)
    read_write_keys.write_pub(public)


if __name__ == "__main__":
    regen_keys()