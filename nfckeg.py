from db import Database

class nfckeg():

    def __init__(self):
        self.lecture_near=None
        self.lecture_out=None
        self.newdb=Database()
        self.isTag=False

    def calculate_dif():
        dif=self.lecture_near-self.lecture_out
        return dif

    def add_dif(self,dif):
        if self.lecture_near is not None and self.lecture_out is not None:
            (tagids,ID)=newdb.get_tagids
            for tagid in tagids:
                if tagid == current_tagid
                    self.isTag=True
                    newdb.set_liters(dif,ID)
                    msg="lecture added"
                    break
            if isTag == False:
                msg="No tagid matches"
                return msg

    def mainloop(self)
        while True:
            if nfc.nfc_near()==True:
                self.lecture_near=flow.get_flow()
                if nfc.nfc_out()==True:
                    self.lecture_out=flow.get_flow()
                    dif=calculate_dif(self.lecture_near,self.lecture_out)
                    print add_dif(dif)
                    

                    

if __name__ == "__main__":

newkeg=nfckeg()
