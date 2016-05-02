from channels import Channel

class TextChannel(Channel):
    """Class that prints on console the sent message"""
    def __init__(self, cfg=None, name="TextChannel"):
        super(MockObject, self).__init__(cfg, name)
        self.messagesnfc = []
        with open ("messagesnfc.txt", "r") as f:
            for line in f:
                self.messages.append(line)


    def get_msg(self):
        if self.msg_avail():
            return self.messagesnfc.pop(0)

    def msg_avail(self):
        return len(self.messagesnfc) > 0


    #def notify(self, user, message):
    #    """Send to "user", the message "message"."""
    #    pass

    #def broadcast(self, message):
    #    """Send to the "broadcast" channel the message "message"."""
    #    pass
