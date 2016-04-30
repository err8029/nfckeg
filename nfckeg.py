from db import Database
from sensors import Sensor 
from sensors import Flow 
from sensors import Nfc 

class nfckeg():

    """Class for Ambrosio Personal Digital Butler
    Will run our house"""
    def __init__(self):
        super(nfckeg, self).__init__()
        self.cl = CommandList()
        self.actions = []
        self.actions.append(ac.MusicPlayer())
        self.actions.append(ac.SensorAction())


    def next_command(self):
        try:
            return self.cl.next()
        except:
            return (None, None)


    def execute_command(self, command):
        print "Will execute", command
        # Foreach Action in actions.
        #   if is_for_you()
        #       action.do
        words = command.split()
        first_word = words[0]
        rest_words = words[1:]
        response = None
        for a in self.actions:
            if a.is_for_you(first_word):
                response = a.do(rest_words)
                break
        else:
            print "No t'entenc"
        return response

    def mainloop(self):
        # While True:
        #   command = get_command
        #   do_command(command)
        #   update
        while True:
            chan, command = self.next_command()
            if command:
                response = self.execute_command(command)
                chan.respond(response)

            time.sleep(1)
            self.update_channels()


if __name__ == "__main__":

    newkeg=nfckeg()
    newkeg.mainloop()
