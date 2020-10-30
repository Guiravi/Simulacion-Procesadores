from Message import Message


class Event:
    message = Message
    arrival_time = 0.0
    type = 0

    def __init__(self, msg, arrival_time, type):
        self.msg = msg
        self.arrival_time = arrival_time
        self.type = type

    def get_arrival_time(self):
        return self.arrival_time

    def get_message(self):
        return self.message

    def set_type(self, type):
        self.type = type

    def set_arrival_time(self, time):
        self.arrival_time = time
