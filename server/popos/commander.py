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

    def __init__(self, ser):
        self.ser = ser
        self.commands = {}
        self.load_commands()

    def load_commands(self):
        with open('commands.json') as json_file:
            commands = json.load(json_file)
        for index, item in enumerate(commands):
            self.commands[item["name"]] = Command(item, index)
    
    def hot(self, temp):
        self.commands["hot"].perform([temp])
    
    def cold(self, temp):
        self.commands["cold"].perform([temp])

    def status(self):
        return self.commands["status"].perform()
    
    def read_temperature(self):
        return self.commands["read_temperature"].perform()

class Command():
    endianness = '<'
    parse_data_type = { "uint8_t": "b",
                        "float": "f" }
    parse_unpac = { "uint8_t": "b",
                    "float": "bbbb" }
    data_formatter = { "uint8_t": int,
                       "float": float }

    def __init__(self, parameters, index):
        self.parameters = parameters
        self.name = parameters["name"]
        self.sends_input = len(parameters["input"]) > 0
        self.sends_output = len(parameters["output"]) > 0
        self.serial_identifier = bytes(str(index), encoding="ascii")
        self.send_data_format = self.endianness + 'c' # Char for the command identified by the array position.
        self.send_data_format += ''.join([ self.parse_data_type[a["type"]] for a in parameters["input"] ])
        self.receive_data_format= ''.join([ self.parse_data_type[a["type"]] for a in parameters["output"] ])


    @classmethod
    def send_chunk(cls, data_format, data):
        st()
        raw_data = struct.pack(data_format, *data)
        Commander.ser.write(raw_data)
        return True

    @classmethod
    def read_chunk(cls, size, data_format):
        raw_data = Commander.ser.read(size)
        return struct.unpack(data_format, raw_data)

    def perform(self, data): # No tengo idea porque, pero no me deja definirlo como classmethod
        formated_data = self.format_input(data)
        if self.sends_input: self.send_chunk(self.send_data_format, (self.serial_identifier, *formated_data))
        if self.sends_output: return self.read_chunk(2, '<bb')

    def format_input(self, data): # No tengo idea porque, pero no me deja definirlo como classmethod
        formated = []
        for index, variable in enumerate(self.parameters["input"]):
            formated.append(self.data_formatter[variable["type"]](data[index]))
        return tuple(formated)

if __name__ == "__main__":
    fa = Commander(1)
    fa.cold(19)
    st()
