import math
import time
class FakeMeasurements(object):
    def __init__(self, logger):
        self.logger = logger
        self.initial_temp = 25
        self.objective_temperature = 25
        self.time0 = time.monotonic()

    def connect_device(self, baudrate, device):
        return 200

    def list_devices(self):
        return [{"port": 'COM1(fake)', "description": 'Device_1'},
                {"port": 'COM2(fake)', "description": 'Device_2'},
                {"port": 'COM4(fake)', "description": 'Device_4'},]

    def disconnect_device(self, device):
        return { "status": "Closed Succesfully" }

    def set_objective_temperature(self, temperature):
        self.logger.info('Setting objective temperature: %s º', temperature)
        self.objective_temperature = float(temperature)
        self.time0 = time.monotonic()

    def request_temperature_measure(self):
        self.logger.info('Serial communication: Asking temperature')
        x = time.monotonic() - self.time0
        TAU = 7
        T = self.objective_temperature
        T0 = self.initial_temp
        value = T + ( T0 - T ) * math.exp( -x / TAU)
        self.initial_temp = value
        self.logger.info('Serial communication: Received temperature: %s º', value)
        return value