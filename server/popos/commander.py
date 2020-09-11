import serial
import struct
import time
import serial.tools.list_ports as ports_list
import threading
import csv
import sys
import cmd
import numpy
import json
from pdb import set_trace as st

class Commander():
    connection = None
    connection_available = False
    logger = None
    baud_rate = 9600

    def __init__(self):
        self.commands = {}
        self.load_commands()

    def load_commands(self):
        with open('server/popos/commands.json') as json_file:
            commands = json.load(json_file)
        for index, item in enumerate(commands):
            self.commands[item["name"]] = Command(item, index)
    
    def connect_device(self, device_name, default_port = None):
        ports = list(ports_list.comports())
        for p in ports:
            Commander.logger.info(p.device)
            if p.device == device_name:
                try:
                    Commander.logger.info('Device found at %s', p.device)
                    Commander.connection = serial.Serial(p.device, Commander.baud_rate, parity=serial.PARITY_EVEN)
                    Commander.connection_available = True
                    Commander.connection.reset_input_buffer()
                    Commander.connection.reset_output_buffer()
                    time.sleep(3)
                    return 200
                except Exception as e:
                    Commander.logger.info('Unable to connect to %s', p.device)
                    Commander.logger.info(e)
                    return 404

    def list_devices(self):
        devices = list(ports_list.comports())
        devices_info = []
        for p in devices:
            devices_info.append({"port": p.device, "description": p.description})
        return devices_info

    def disconnect_device(self, device):
        if not Commander.connection_available:
            return { "error": "Can't close connection. None is open." }
        if (Commander.connection.port == device) and self.connection.is_open: # .port .name .portsrt ._port tienen todos el valor 'COM4'
            Commander.connection.close()
            Commander.connection_available = False
            Commander.logger.info('Succesfully disconected device %s', device)
            return { "status": "Closed Succesfully" }
        Commander.logger.info("Can't close connection on port " + device)
        return { "error": "Can't close connection on port " + device }
    
    def hot(self, temp):
        self.commands["hot"].perform(Commander.connection, [temp])
    
    def cold(self, temp):
        self.commands["cold"].perform(Commander.connection, [temp])

    def status(self):
        return self.commands["status"].perform(Commander.connection, [])
    
    def read_temperature(self):
        temp = self.commands["read_temperature"].perform(Commander.connection, [])
        return temp[-1]

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
        serial_connection.reset_input_buffer()
        serial_connection.reset_output_buffer()
        formated_data = self.format_input(data)
        self.send_chunk(serial_connection, formated_data)
        return self.read_chunk(serial_connection)

    def format_input(self, data):
        formated = []
        for index, variable in enumerate(self.parameters["input"]):
            formated.append(self.data_formatter[variable["type"]](data[index]))
        return tuple(formated)
