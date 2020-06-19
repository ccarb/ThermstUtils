import serial
import serial.tools.list_ports as ports_list
import struct

SEPARATOR_SIZE = 1
DATA_SIZE = 4

class Connection(object):
    def __init__(self):
        self.connection_available = False

    def connect_device(self, baud_rate, device_name, default_port = None):
        ports = list(ports_list.comports())
        for p in ports:
            if p.device == device_name:  # arduino found
                print("Device found at " + p.device)
                try:
                    self.connection = serial.Serial(p.device, baud_rate)
                    self.connection_available = True
                    return 200
                except:
                    return 404

    def list_devices(self):
        devices = list(ports_list.comports())
        self.devices = devices
        devices_info = []
        for p in devices:
            devices_info.append({"port": p.device, "description": p.description})
        return devices_info

    def disconnect_device(self, device):
        if not self.connection_available:
            return { "error": "Can't close connection. None is open." }
        if (self.connection.port == device) and self.connection.is_open: # .port .name .portsrt ._port tienen todos el valor 'COM4'
            self.connection.close()
            self.connection_available = False
            return { "status": "Closed Succesfully" }
        return { "error": "Can't close connection on port " + device }

    def request_temperature_measure(self):
        if not self.connection_available:
            return { "error": "Device disconnected." }
        self.connection.write(b'x')
        while self.connection.in_waiting <(SEPARATOR_SIZE + DATA_SIZE):
            pass
        raw_separator = self.connection.read(SEPARATOR_SIZE)
        if raw_separator == b'x':
            serial_data = self.connection.read(DATA_SIZE)
            temperature, = struct.unpack('<f', serial_data)
            return {"temperature": str('%.1f'%(temperature))}
        return { "error": "Invalid temperature measure." }        

    def ping(self, message = 'a' ):
        # raw_data = struct.pack('<cb', message)
        # print("Seding: '" + raw_data + "' to " + self.connection.port )
        self.connection.write(message.encode())
        received = self.connection.read()
        print("Received: " )
        print(received)
        return received
