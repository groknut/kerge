
from serial.tools import list_ports
import subprocess
import esptool
import json
from pathlib import Path

__version__ = '0.0.1'
__author__ = "groknut"
__url__ = "https://github.com/groknut/kerge"

parent = Path(__file__).parent

settings_path = Path("settings.json")

def load_data():
    if settings_path.exists():
        with open(settings_path, mode='r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    return None
    

def save(data):
    with open(settings_path, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def ports_list():
    ports = list_ports.comports()

    if not ports:
        print("Ports not found")
        return
    print("Ports:")
    for port in ports:
        print(f"{port.device} - {port.description}")

def erase_flash(port):
    try:
        esptool.main(['--port', port, 'erase_flash'])
        print('Flash erase')
    except Exception as e:
        print(e)

def port_info(port_name):
    try:
        port = None
        for p in list_ports.comports():
            if p.device == port_name:
                port = p
                break

        if not port:
            print(f"{port_name} not found ")
            return

        print(f"""Device: {port.device}
Description: {port.description}
Manufacturer: {port.manufacturer}""")

    except Exception as e:
        print("Error:", e)
        
        

def write_bin(data, bin_file, port_name):

    try:
        esptool.main(
            ['--chip', data['chip'], 
            '--port', port_name,
            '--baud', str(data['baud']),
            'write_flash', '0x0',
            bin_file
            ]
        )
        print(f"Writting a BIN file {bin_file} to the {port_name}")
    except Exception as e:
        print(e)
             
import argparse

def main():
    data = load_data()

    if data is None:
        print("Couldn't download the settings package")
    
    parser = argparse.ArgumentParser(
        description="A program for writing bin files to devices (m5stack stickC plus 2)"
    )

    parser.add_argument('-l', '--list', action='store_true' , help="list of ports")
    parser.add_argument('-p', '--port',  help="select of port")
    parser.add_argument('-w', '--write', type=str,  help="writing firmware to the microcontroller")
    parser.add_argument('-b', '--baud', nargs='?', const=True, type=int, help="setting the download speed")
    parser.add_argument('-v', '--version', action='store_true',  help="program version")
    parser.add_argument('-e', '--erase',  help="erase flash from the microcontroller")
    args = parser.parse_args()

    if args.list:
        ports_list()

    elif args.port and args.write:
        print(args.write, type(args.write))
        if args.write.endswith('.bin'):
            print(args.port)
            write_bin(data, args.write, args.port)
        else:
            print("Error: the file must have an extension .bin")

    elif args.port:
        port_info(args.port)

    elif args.write:
        write_bin(args.write)

    elif args.version:
        print("Version:", __version__)

    elif args.erase:
        erase_flash(args.erase)

    elif args.baud is True:
        print(f"current baud rate: {data['baud']}")

    elif isinstance(args.baud, int):
        data['baud'] = args.baud
        print(f"set baud rate: {data['baud']}") 
    else:
        print(f"""
creator: {__author__}
homepage: {__url__}
""")

    save(data)        

if __name__ == "__main__":
    main()
