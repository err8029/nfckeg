from sensors import Sensor
from random import choice
import time

class Flow(Sensor):

    def __init__(self):
        self.flow_readings =list()
        self.time = range(0,10)
        self.cumulative_flow = 0
        self.n = 0.1

    def setup(self):
        time.sleep(self.n)

    def get_data(self):
        for second in self.time:
            list_readings = ['20','40','10','55','0',None]
            self.setup()
            reading_chosen = choice(list_readings)
            if reading_chosen is not None:
                self.flow_readings.append(int(reading_chosen))
        return self.flow_readings

    def get_cumulative(self,readings):
        for flow in self.flow_readings:
            self.cumulative_flow = self.cumulative_flow+flow
        return self.cumulative_flow

    def reset_cumulative(self):
        self.cumulative_flow = 0
        return self.cumulative_flow
