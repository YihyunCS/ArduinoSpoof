import serial
import serial.tools.list_ports
from colorama import init, Fore

init(autoreset=True)

def change_serial(com_port, pid, hid):
    try:
        ser = serial.Serial(com_port, timeout=1)
        ser.write(b'AT\r\n')
        response = ser.readline().decode().strip()
        if response == 'OK':
            ser.write(b'AT+PID' + pid.encode() + b'\r\n')
            ser.write(b'AT+HID' + hid.encode() + b'\r\n')
            print(Fore.GREEN + "Done")
        else:
            print(Fore.RED + f"Error communicating with device on {com_port}")
        ser.close()
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def main():
    print("Available COM ports:")
    com_ports = [port.device for port in serial.tools.list_ports.comports()]
    for idx, port in enumerate(com_ports, start=1):
        print(f"{idx}. {port}")
    
    try:
        selected_port_index = int(input("Enter the number corresponding to the COM port: ")) - 1
        selected_com_port = com_ports[selected_port_index]
        pid = input("Enter the PID: ")
        hid = input("Enter the HID: ")

        change_serial(selected_com_port, pid, hid)
    except (IndexError, ValueError):
        print(Fore.RED + "Invalid input.")

if __name__ == "__main__":
    main()
