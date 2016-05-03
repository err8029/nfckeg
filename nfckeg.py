from db import Database
from sensors import Sensor
from sensors import Flow
from sensors import Nfc

class nfckeg():

    """Class for Ambrosio Personal Digital Butler
    Will run our house"""
    def __init__(self):
        self.new_database = Database()
        self.new_nfc = Nfc()
        self.new_flow = Flow()
        pass
    def read_flow(self):
        is_card = False
        while is_card != True:
            (is_card, tag_id_in) = self.new_nfc.get_data()
        flow_readings = self.new_flow.get_data()
        data_in = self.new_flow.get_cumulative(flow_readings)
        tag_id_out = None
        print tag_id_in
        while is_card != False:
            (is_card, tag_id_out) = self.new_nfc.get_data()
        data_out = self.new_flow.get_cumulative(flow_readings)
        flow_readings = self.new_flow.get_data()
        dif_data = abs(data_out-data_in)
        return dif_data, tag_id_in

    def mainloop(self):
        # While True:
        #   command = get_command
        #   do_command(command)
        #   update
        while True:
            (dif, tag_id) = self.read_flow()
            print dif
            print tag_id
            id_user = self.new_database.get_tagids(str(tag_id))
            print id_user
            self.new_database.set_liters(str(dif),id_user)



if __name__ == "__main__":

    newkeg=nfckeg()
    newkeg.mainloop()
