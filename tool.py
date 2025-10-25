
from serial.tools import list_ports
import esptool

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
        print("Error:", e)

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

        print(rf"""
Device: {port.device}
Description: {port.description}
Manufacturer: {port.manufacturer}
""")

    except Exception as e:
        print("Error:", e)
        
        

def write_bin(data, bin_file, port_name):

    try:
       	if data['chip']:
            esptool.main(
                [
    	            '--chip', data['chip'], 
    	            '--port', port_name,
    	            '--baud', str(data['baud']),
    	            'write_flash', '0x0',
    	            bin_file
                ]
            )
        else:
            esptool.main(
                [
                    '--port', port_name,
                    '--baud', str(data['baud']),
                    'write_flash', '0x0',
                    bin_file
                ]
            )

       	print(f"Writting a BIN file {bin_file} to the {port_name}")
   	
    except Exception as e:
        print(e)
