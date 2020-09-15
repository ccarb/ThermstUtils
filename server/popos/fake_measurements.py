import math
import time

class DummyClass(object):
    pass

class FakeMeasurements(object):
    def __init__(self, logger):
        self.logger = logger
        self.initial_temp = 25
        self.objective_temperature = 25
        self.time0 = time.monotonic()
        self.device_list = [ {"port": 'COM1(fake)', "description": 'Device_1'},
                            {"port": 'COM2(fake)', "description": 'Device_2'},
                            {"port": 'COM4(fake)', "description": 'Device_4'},]
        self.connection=DummyClass()
        self.connection.port = None
        self.connection_available = None
        self.mode = None
        self.target_temperature = None
        self.last_measurement = None
        self.device_status_codes={"status":"0","error":"0"}
        self.device_status_descriptions={"status":"Using testing mode","error":"No errors"}


    def connect_device(self, device_name, default_port=None):
        for device in device_list:
            if device["port"] == device_name:
                self.connection.port = device_name
                self.connection_available = True
        return 200

    def list_devices(self):
        return self.device_list

    def disconnect_device(self, device):
        return { "status": "Closed Succesfully" }

    def hot(self, temperature):
        self.logger.info('Setting objective temperature: %s º', temperature)
        self.objective_temperature = float(temperature)
        self.mode="hot"
        self.target_temperature = temperature
        self.time0 = time.monotonic()

    def cold(self, temperature):
        self.logger.info('Setting objective temperature: %s º', temperature)
        self.objective_temperature = float(temperature)
        self.mode="cold"
        self.target_temperature = temperature
        self.time0 = time.monotonic()

    def stop(self):
        self.mode=None
        self.logger.info('Stopped device')

    def read_temperature(self):
        self.logger.info('Serial communication: Asking temperature')
        x = time.monotonic() - self.time0
        TAU = 7
        T = self.objective_temperature
        T0 = self.initial_temp
        value = T + ( T0 - T ) * math.exp( -x / TAU)
        self.initial_temp = value
        self.logger.info('Serial communication: Received temperature: %s º', value)
        self.last_measurement=value
        self.last_measurement_timestamp = time.monotonic()
        return value