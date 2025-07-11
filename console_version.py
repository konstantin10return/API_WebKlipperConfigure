#!./venv/Script/python.exe


import sys

import read_write_keys
import gen_keys
from w_cfg import reload_printer_cfg


def key_gen():
    gen_keys.regen_keys()
    print('key (ключ)')
    print(read_write_keys.rad_pub())


def help_message():
    print('''-h или --help выдает эту краткую справку
    
    -g или --keygen создает новый ключ устройства
    
    -k или --key выводит ключ устройства
    
    -r или --reloadcfg обновить конфигурационный файл''')


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("command sintacs error")
        print("неправильный синтаксис команды")
        sys.exit()
    arg = args[0].strip()
    if arg == '--keygen' or arg == '-g':
        key_gen()
    elif arg == '-k' or arg == '--key':
        print(read_write_keys.rad_pub())
    elif arg == '-r' or arg == '--reloadcfg':
        reload_printer_cfg()
    elif arg == '-h' or arg == '--help':
        help_message()
    else:
        print("command sintacs error")
        print("неправильный синтаксис команды")