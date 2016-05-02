from channels import Channel
import telepot

class Tramboliko(telepot.Bot):
    """Tramboliko is my telegram bot"""
    def __init__(self, token, usuaris):
        super(Tramboliko, self).__init__(token)
        self.clist = None
        self.chat_id = None
        #self.users = usuaris

    def set_list(self, clist):
        self.clist = clist

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            command = msg['text']
            if self.clist is not None:
                self.clist.append(command)
                self.chat_id = chat_id
            else:
                self.sendMessage(chat_id, "NOOO!!!")

    def respond(self, message):
        if self.chat_id is not None:
            self.sendMessage(self.chat_id, message)


class TelegramChannel(Channel):
    """Class that will use Telegram to notify"""
    def __init__(self, cfg=None, name="TelegramChannel"):
        super(TelegramChannel, self).__init__(cfg, name)
        token = self.cfg["telegram"]["token"]
        self.bot = Tramboliko(token, self.cfg["telegram"]["token"])
        self.messagesnfc = []
        self.bot.set_list(self.messagesnfc)
        self.bot.notifyOnMessage()

    def get_msg(self):
        if self.msg_avail():
            return self.messagesnfc.pop(0)

    def msg_avail(self):
        return len(self.messagesnfc) > 0

    def respond(self, response):
        if response is None:
            response = "Command not understood"
        self.bot.respond(response)



    #def notify(self, user, message):
    #    """Send to "user", the message "message"."""
    #    pass
