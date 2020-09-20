import serial
import struct
import time
import serial.tools.list_ports as ports_list
import sys
import json
from pdb import set_trace as st
from server.popos.status_parser import StatusParser

class Commander():
    connection = None
    connection_available = False
    logger = None
    baud_rate = 9600
    device_status_codes = { "status": None, "error": None }
    device_status_descriptions = { "status": None, "error": None }
    target_temperature = None
    last_measurement = None
    last_measurement_timestamp = None
    mode = None

    def __init__(self):
        self.commands = {}
        self.load_commands()

    def load_commands(self):
        with open('json/commands.json') as json_file:
            commands = json.load(json_file)
        for index, item in enumerate(commands):
            self.commands[item["name"]] = Command(item, index)
    
    def connect_device(self, device_name, default_port = None):
        ports = list(ports_list.comports())
        for p in ports:
            if p.device == device_name:
                try:
                    Commander.logger.info('Device found at %s', p.device)
                    Commander.connection = serial.Serial(p.device, Commander.baud_rate, parity=serial.PARITY_EVEN, timeout=3)
                    Commander.connection.reset_input_buffer()
                    Commander.connection.reset_output_buffer()
                    time.sleep(3)
                except Exception as e:
                    Commander.logger.info('Unable to connect to %s', p.device)
                    Commander.logger.info(e)
                    Commander.connection = None
                    return 404
                try:
                    self.status()
                except Exception as e:
                    Commander.logger.info('Selected device is invalid: %s', p.device)
                    Commander.logger.info(e)
                    Commander.connection = None
                    return 404
                Commander.connection_available = True
                return 200

    def list_devices(self):
        devices = list(ports_list.comports())
        devices_info = []
        for p in devices:
            devices_info.append({"port": p.device, "description": p.description})
        return devices_info

    def disconnect_device(self, device):
        if not Commander.connection_available:
            return { "error": "Can't close connection. None is open." }
        if (Commander.connection.port == device) and Commander.connection.is_open: # .port .name .portsrt ._port tienen todos el valor 'COM4'
            Commander.connection.close()
            Commander.connection_available = False
            Commander.logger.info('Succesfully disconected device %s', device)
            return { "status": "Closed Succesfully" }
        Commander.logger.info("Can't close connection on port " + device)
        return { "error": "Can't close connection on port " + device }
    
    def hot(self, temp):
        Commander.target_temperature = temp
        Commander.mode = "hot"
        status = self.commands["hot"].perform(Commander.connection, [temp])
        Commander.update_status(status)
    
    def cold(self, temp):
        Commander.target_temperature = temp
        Commander.mode = "cold"
        status = self.commands["cold"].perform(Commander.connection, [temp])
        Commander.update_status(status)
    
    def stop(self):
        Commander.target_temperature = None
        Commander.mode = None
        status = self.commands["stop"].perform(Commander.connection, [])
        Commander.update_status(status)

    def status(self):
        status = self.commands["status"].perform(Commander.connection, [])
        Commander.update_status(status)
        return status
    
    def read_temperature(self):
        temp = self.commands["read_temperature"].perform(Commander.connection, [])
        Commander.last_measurement = temp[-1]
        Commander.last_measurement_timestamp = time.monotonic()
        Commander.update_status(temp[0:2])
        return temp[-1]
    
    def error_set(self, error):
        self.commands["error_set"].perform(Commander.connection, [error])
    
    def error_clear(self):
        self.commands["error_clear_all"].perform(Commander.connection, [])

    @classmethod
    def update_status(cls, status):
        Commander.device_status_codes["status"] = status[0]
        Commander.device_status_codes["error"] = status[1]
        [Commander.device_status_descriptions["status"], Commander.device_status_descriptions["error"]] = StatusParser.parse(status)
    
class Command():
    endianness = '<'
    parse_data_type = { "uint8_t": "b",
                        "float": "f" }
    data_size = { "uint8_t": 1,
                  "float": 4 }
    data_formatter = { "uint8_t": int,
                       "float": float }

    def __init__(self, parameters, index):
        self.parameters = parameters
        self.name = parameters["name"]
        self.serial_identifier = index
        self.send_data_format = self.endianness + 'b' # Char for the command identified by the array position.
        self.send_data_format += ''.join([ self.parse_data_type[a["type"]] for a in parameters["input"] ])
        self.receive_data_format = self.endianness + 'bb' + ''.join([ self.parse_data_type[a["type"]] for a in parameters["output"] ])
        self.receive_data_buffer_size = sum([ self.data_size[a["type"]] for a in parameters["output"] ]) + 2

    def send_chunk(self, serial_connection, data):
        raw_data = struct.pack(self.send_data_format, self.serial_identifier, *data)
        Commander.logger.info(raw_data)
        serial_connection.write(raw_data)
        return True

    def read_chunk(self, serial_connection):
        raw_data = serial_connection.read(self.receive_data_buffer_size)
        Commander.logger.info(raw_data)
        return list(struct.unpack(self.receive_data_format, raw_data))

    def perform(self, serial_connection, data):
        try:
            serial_connection.reset_input_buffer()
            serial_connection.reset_output_buffer()
            formated_data = self.format_input(data)
            self.send_chunk(serial_connection, formated_data)
            return self.read_chunk(serial_connection)
        except Exception as e:
            Commander.logger.info(e)
            Commander.connection = None
            Commander.connection_available = False
            return self.error_occured()

    def format_input(self, data):
        formated = []
        for index, variable in enumerate(self.parameters["input"]):
            formated.append(self.data_formatter[variable["type"]](data[index]))
        return tuple(formated)
    
    def error_occured(self):
        error_status = [int(-1)]
        error_code = [int(-1)]
        expected_response = []
        for variable in self.parameters["output"]:
            expected_response.append(self.data_formatter[variable["type"]](0))
        return error_status + error_code + expected_response
