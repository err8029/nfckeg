from sensors import Sensor
from random import choice
import time

class Nfc(Sensor):

    def __init__(self):
        self.is_tagid = False
        self.n = 0.1

    def setup(self):
        time.sleep(self.n)

    def get_data(self):
        read_tagids=["00x1",None]
        self.setup()
        is_card = False
        read_tagid = choice(read_tagids)
        if read_tagid is not None:
            return (True,read_tagid)
        return (False,read_tagid)

    def get_cumulative(self):
        pass

    def reset_cumulative(self):
        pass

#if __name__ == "__main__":

#    newnfc=Nfc()
#    print newnfc.get_data()
