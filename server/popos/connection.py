import serial
import serial.tools.list_ports as ports_list
import struct
from commander import Commander

SEPARATOR_SIZE = 1
DATA_SIZE = 4

class Connection(object):
    def __init__(self, logger):
        self.connection_available = False
        self.logger = logger
        self.commander = Commander()

    def connect_device(self, baud_rate, device_name, default_port = None):
        ports = list(ports_list.comports())
        for p in ports:
            if p.device == device_name:  # arduino found
                # print("Device found at " + p.device)
                try:
                    self.connection = serial.Serial(p.device, baud_rate, parity=serial.PARITY_EVEN)
                    self.initialize_commander()
                    self.connection_available = True
                    self.logger.info('Device found at %s', p.device)
                    return 200
                except:
                    self.logger.info('Unable to connect to %s', p.device)
                    return 404
    
    def initialize_commander(self):
        self.commander.ser = self.connection

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
            self.logger.info('Succesfully disconected device %s', device)
            return { "status": "Closed Succesfully" }
        self.logger.info("Can't close connection on port " + device)
        return { "error": "Can't close connection on port " + device }

    # def request_temperature_measure(self):
    #     if not self.connection_available:
    #         return { "error": "Device disconnected." }
    #     self.logger.info("Serial communication: Asking temperature")
    #     self.connection.write(b'x')
    #     while self.connection.in_waiting <(SEPARATOR_SIZE + DATA_SIZE):
    #         pass
    #     raw_separator = self.connection.read(SEPARATOR_SIZE)
    #     if raw_separator == b'x':
    #         serial_data = self.connection.read(DATA_SIZE)
    #         temperature, = struct.unpack('<f', serial_data)
    #         self.logger.info("Serial communication: Received temperature %s", str('%.1f'%(temperature)))
    #         return {"temperature": str('%.1f'%(temperature))}
    #     self.logger.info("Serial communication: Invalid temperature measurement.")
    #     return { "error": "Invalid temperature measurement." }        

    def ping(self, message = 'a' ):
        # raw_data = struct.pack('<cb', message)
        # print("Seding: '" + raw_data + "' to " + self.connection.port )
        self.logger.info("Serial communication: Ping " + message)
        self.connection.write(message.encode())
        received = self.connection.read()
        self.logger.info("Serial communication: Pong " + received)
        return received

    def request_temperature_measure(self):
        self.commander.read_temperature()
