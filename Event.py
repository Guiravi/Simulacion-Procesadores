class Event:

    def __init__(self, message, arrival_time, id_event):
        self.message = message              # Mensaje
        self.arrival_time = arrival_time    # Tiempo en el que ocurre el evento
        self.id_event = id_event                    # Identificado de evento

    def get_arrival_time(self):
        return self.arrival_time

    def get_message(self):
        return self.message

    def set_type(self, id_event):
        self.id_event = id_event

    def set_arrival_time(self, time):
        self.arrival_time = time
