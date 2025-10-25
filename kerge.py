
from data import get_project_info, save, load_data
from tool import ports_list, erase_flash, port_info, write_bin
import argparse

project_info = get_project_info()

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
        if args.write.endswith('.bin'):
            write_bin(data, args.write, args.port)
        else:
            print("Error: the file must have an extension .bin")

    elif args.port:
        port_info(args.port)

    elif args.write:
        write_bin(args.write)

    elif args.version:
        print("Version:", project_info['version'])

    elif args.erase:
        erase_flash(args.erase)

    elif args.baud is True:
        print(f"current baud rate: {data['baud']}")

    elif isinstance(args.baud, int):
        data['baud'] = args.baud
        print(f"set baud rate: {data['baud']}")
         
    else:
        print(f"""
creator: {project_info['creator']}
homepage: {project_info['url']}
""")

    save(data)        

if __name__ == "__main__":
    main()
