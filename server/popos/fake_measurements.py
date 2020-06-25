import math
import time
class FakeMeasurements(object):
    def __init__(self):
        self.initial_temp = 25
        self.objective_temperature = None
        self.time0 = None

    def set_objective(self, temperature):
        self.objective_temperature = float(temperature)
        self.time0 = time.monotonic()
    
    def read_temperature(self):
        x = time.monotonic() - self.time0
        TAU = 7
        T = self.objective_temperature
        T0 = self.initial_temp
        value = T + ( T0 - T ) * math.exp( -x / TAU)
        return value