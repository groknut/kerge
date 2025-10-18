
from serial.tools import list_ports
import subprocess
import esptool
import json
from pathlib import Path

parent = Path(__file__).parent

settings_path = Path("settings.json")

def load_data():
    if settings_path.exists():
        with open(settings_path, mode='r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    else:
        print("Не удалось загрузить пакет настроек")

def save(data):
    with open(settings_path, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# -l
def ports_list():
    ports = list_ports.comports()

    if not ports:
        print("портов нет")
        return
    print("COM-порты доступные")
    for port in ports:
        print(f"{port.device} - {port.description}")


# информация о портах -p
def port_info(p):
    print(p)

# стираем память
def erase_flash(port):
    try:
        esptool.main(['--port', port, 'erase_flash'])
        print('очищено')
    except Exception as e:
        print(e)

def write_bin(bin_file):
    port = input("введите порт: ")
    try:
        esptool.main(
            ['--chip', data['chip'], 
            '--port', port,
            '--baud', data['baud'],
            'write_flash', '0x0',
            bin_file
            ]
        )
        print("ready")
    except Exception as e:
        print(e)        
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Программа для записи bin файлов в устройства m5stack stickc plus 2"
    )

    parser.add_argument('-l', '--list', action='store_true' , help="количество портов COM")
    parser.add_argument('-p', '--port',  help="выбор порта")
    parser.add_argument('-w', '--write',  help="запись прошивки в микроконтроллерE")
    parser.add_argument('-b', '--baud',  help="установка скорости загрузки")
    parser.add_argument('-v', '--version', action='store_true',  help="версия программы")
    parser.add_argument('-e', '--erase',  help="стереть прошивку из микроконтроллера")
    args = parser.parse_args()

    if args.list:
        ports_list()
    elif args.port:
        port_info(args.p)
    elif args.write:
        write_bin(args.write)
    elif args.version:
        print(1.0)
    elif args.port and args.write:
        if args.write.endswith('.bin'):
            print(f"Запись BIN файла {args.write} в порт {args.port}")
            # Ваш код здесь
        else:
            print("Ошибка: файл должен иметь расширение .bin")        

if __name__ == "__main__":
    main()
