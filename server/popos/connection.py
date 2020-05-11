import serial
import serial.tools.list_ports as ports_list
import struct

class Connection(object):
    def __init__(self):
        self.connection_available = False

    def create_connection(self, baud_rate, default_port = None):
        ports = list(ports_list.comports())
        for p in ports:
            if p.device == '/dev/ttyACM0' or p.device == '/dev/ttyUSB0':  # arduino found
                print("Arduino found at " + p.device)
                return serial.Serial(p.device, baud_rate)
        raise IOError("Could not find an arduino - is it plugged in?")

    def list_devices(self):
        devices = list(ports_list.comports())
        self.devices = devices
        devices_info = []
        for p in devices:
            devices_info.append({"port": p.device, "description": p.description})
        return devices_info

    def connect_device(self, baud_rate, device):
        self.connection = serial.Serial(device, baud_rate)
        self.connection_available = True

    def disconnect_device(self, device):
        if not self.connection_available:
            return { "error": "Can't close connection. None is open." }
        if (self.connection.port == device) and self.connection.is_open: # .port .name .portsrt ._port tienen todos el valor 'COM4'
            self.connection.close()
            self.connection_available = False
            return { "status": "Closed Succesfully" }
        return { "error": "Can't close connection on port " + device }

    def ping(self, message = 'a' ):
        # raw_data = struct.pack('<cb', message)
        # print("Seding: '" + raw_data + "' to " + self.connection.port )
        self.connection.write(message.encode())
        received = self.connection.read()
        print("Received: " )
        print(received)
        return received
