#! /usr/bin/python
import serial
import struct
import time
import serial.tools.list_ports as ports_list
from live_plot import Plotter
import threading
import csv
import sys
import cmd
import numpy


BAUD_RATE = 9600
SEPARATOR_SIZE = 1
SEPARATOR = b't'
DATA_SIZE = 4
DATA_FORMAT = '<f'
T_LABELS = ('t1', 't2')
TIMEOUT = 0.5

DEBUG = False


class Commander(cmd.Cmd):
    ser = None
    communication_available = threading.Event();
    start = 0
    time = 0
    t1 = None
    t2 = None

    @classmethod
    def wait_communication_available(cls):
        while not Commander.communication_available.isSet():
            pass

    @classmethod
    def send_chunk(cls, data_format, data):
        raw_data = struct.pack(data_format, *data)
        Commander.ser.write(raw_data)
        return True

    @classmethod
    def read_chunk(cls, size, data_format):
        raw_data = Commander.ser.read(size)
        data = struct.unpack(data_format, raw_data)
        return data
    
    @classmethod
    def set_data(cls, t1, t2):
        Commander.t1 = t1
        Commander.t2 = t2
        Commander.time = time.time() - Commander.start

    def do_data(self, data):
        print(f'time = {Commander.time}')
        print(f't1 = {Commander.t1}')
        print(f't2 = {Commander.t2}')
        print(f'dif = {Commander.t2 - Commander.t1}')

    def do_pwm_cold(self, dato):
        self.wait_communication_available()
        Commander.communication_available.clear()
        self.send_chunk('<cB', (b'a', numpy.uint8(dato)))
        Commander.communication_available.set()

    def do_pwm_hot(self, dato):
        self.wait_communication_available()
        Commander.communication_available.clear()
        self.send_chunk('<cB', (b'b', numpy.uint8(dato)))
        Commander.communication_available.set()

    def do_cold(self, dato):
        self.wait_communication_available()
        Commander.communication_available.clear()
        self.send_chunk('<cB', (b'd', int(dato)))
        frame = self.read_chunk(2, '<bb')
        Commander.communication_available.set()
        print(f'frame = {frame}')
        Commander.start = time.time()

    def do_hot(self, dato):
        self.wait_communication_available()
        Commander.communication_available.clear()
        self.send_chunk('<cB', (b'e', int(dato)))
        frame = self.read_chunk(2, '<bb')
        Commander.communication_available.set()
        print(f'frame = {frame}')
        Commander.start = time.time()
        
    def do_stop(self, data):
        self.wait_communication_available()
        Commander.communication_available.clear()
        self.send_chunk('<c', (b's',))
        Commander.communication_available.set()
        Commander.start = time.time()


    def do_error(self, data):
        self.wait_communication_available()
        Commander.communication_available.clear()
        self.send_chunk('<cB', (b'x',numpy.uint8(data)))
        Commander.communication_available.set()


    def do_no_error(self, data):
        self.wait_communication_available()
        Commander.communication_available.clear()
        self.send_chunk('<c', (b'z',))
        Commander.communication_available.set()

    def do_pwm_get(self, data):
        self.wait_communication_available()
        Commander.communication_available.clear()
        if not self.send_chunk('<c', (b'f',)):
            return
        pwm = self.read_chunk(1, '<b')[0]
        Commander.communication_available.set()
        print(f'pwm = {pwm}')

    def do_status(self, data):
        self.wait_communication_available()
        Commander.communication_available.clear()
        if not self.send_chunk('<c', (b'i',)):
            return
        status = self.read_chunk(2, '<bb')
        Commander.communication_available.set()
        print(f'status = {status}')

    def do_temp_referencia(self, data):
        self.wait_communication_available()
        Commander.communication_available.clear()
        if not self.send_chunk('<c', (b'g',)):
            return
        referencia = self.read_chunk(4, '<f')[0]
        Commander.communication_available.set()
        print(f'temperatura referencia = {referencia}')


    def do_exit(self, data):
        return True

    def do_EOF(self, data):
        return True


def find_arduino(baud_rate):
    ports = list(ports_list.comports())
    for p in ports:
        if p.device == '/dev/ttyACM0' or p.device == '/dev/ttyUSB0':  # arduino found
            print("Device found at " + p.device)
            ser = serial.Serial(p.device, baud_rate, parity=serial.PARITY_EVEN)
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            time.sleep(3)
            return ser

    raise IOError("Could not find the device - is it plugged in?")


def start_cmd(stop_event):
    Commander().cmdloop()
    stop_event.set()
    print("Closing plot")

def main():

    try:
        ser = find_arduino(BAUD_RATE)
    except IOError as e:
        print(e)
        return
    Commander.ser = ser

    stop_event = threading.Event()
    t = threading.Thread(name='commander', target=start_cmd, args=(stop_event,))
    t.start()

    p = Plotter([0, 30], [0, 40])
    p.set_ticks('y', [y for y in range(0, 40, 1)])
    start_time = time.time()
    data = {}
    for l in T_LABELS:
        p.add_line(l)
        data[l] = []
    times = [[],[]]

    Commander.communication_available.set()

    while not stop_event.isSet():
        
        Commander.wait_communication_available()

        i = 0
        Commander.communication_available.clear()
        for l in T_LABELS:
            Commander.send_chunk('<cb', (b't',i))
            current_data = Commander.read_chunk(DATA_SIZE, DATA_FORMAT)[0]
            current_time = time.time()-start_time
            p.add_data([current_time], [current_data], l)
            data[l].append(current_data)
            times[i].append(current_time)
            i += 1
        Commander.communication_available.set()
        Commander.set_data(data['t1'][-1], data['t2'][-1])
        time.sleep(0.1)

    ser.close()
    p.close()
    t.join()
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'w') as dataFile:
            wr = csv.writer(dataFile)
            wr.writerows([times, data])


if __name__ == "__main__":
    main()