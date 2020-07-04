import math
import time
class FakeMeasurements(object):
    def __init__(self, logger):
        self.logger = logger
        self.initial_temp = 25
        self.objective_temperature = 25
        self.time0 = time.monotonic()

    def set_objective(self, temperature):
        self.logger.info('Setting objective temperature: %s º', temperature)
        self.objective_temperature = float(temperature)
        self.time0 = time.monotonic()
    
    def read_temperature(self):
        self.logger.info('Serial communication: Asking temperature')
        x = time.monotonic() - self.time0
        TAU = 7
        T = self.objective_temperature
        T0 = self.initial_temp
        value = T + ( T0 - T ) * math.exp( -x / TAU)
        self.logger.info('Serial communication: Received temperature: %s º', value)
        return value