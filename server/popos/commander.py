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
    ser = None

    def __init__(self):
        self.commands = {}
        self.load_commands()

    def load_commands(self):
        with open('commands.json') as json_file:
            commands = json.load(json_file)
        for index, item in enumerate(commands):
            self.commands[item["name"]] = Command(item, index)
    
    def hot(self, temp):
        self.commands["hot"].perform(Commander.ser, [temp])
    
    def cold(self, temp):
        self.commands["cold"].perform(Commander.ser, [temp])

    def status(self):
        return self.commands["status"].perform(Commander.ser, [])
    
    def read_temperature(self):
        return self.commands["read_temperature"].perform(Commander.ser, [])

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
        self.serial_identifier = bytes(str(index), encoding="ascii")
        self.send_data_format = self.endianness + 'c' # Char for the command identified by the array position.
        self.send_data_format += ''.join([ self.parse_data_type[a["type"]] for a in parameters["input"] ])
        self.receive_data_format = self.endianness + ''.join([ self.parse_data_type[a["type"]] for a in parameters["output"] ])
        self.receive_data_buffer_size = sum([ self.data_size[a["type"]] for a in parameters["output"] ])

    def send_chunk(self, serial_connection, data):
        raw_data = struct.pack(self.send_data_format, self.serial_identifier, *data)
        self.dato_enviado = raw_data
        serial_connection.write(raw_data)
        return True

    def read_chunk(self, serial_connection):
        raw_data = serial_connection.read(self.receive_data_buffer_size)
        return list(struct.unpack(self.receive_data_format, raw_data))

    def perform(self, serial_connection, data):
        formated_data = self.format_input(data)
        if len(self.parameters["input"]) > 0:
            self.send_chunk(serial_connection, formated_data)
        if len(self.parameters["output"]) > 0::
            return self.read_chunk(serial_connection)

    def format_input(self, data):
        formated = []
        for index, variable in enumerate(self.parameters["input"]):
            formated.append(self.data_formatter[variable["type"]](data[index]))
        return tuple(formated)
