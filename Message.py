class Message:

    def __init__(self):
        self.queue_time = 0.0       # Tiempo en cola
        self.processing_time = 0.0  # Tiempo de procesamiento
        self.system_time = 0.0      # Tiempo total en el sistema
        self.amount_returned = 0    # Cantidad de veces retornado a computadora 2 o 3 respectivamente
        self.arrival_time = 0.0     # Tiempo en el que empezó a ser procesado
        self.departure_time = 0.0   # Tiempo en el que termina el procesamiento

    def get_system_time(self):
        return self.system_time

    def get_processing_time(self):
        return self.processing_time

    def get_queue_time(self):
        return self.queue_time

    def get_system_time(self):
        return self.system_time

    def get_amount_returned(self):
        return self.amount_returned

    def get_departure_time(self):
        return self.departure_time

    def add_system_time(self, time):
        self.system_time = self.system_time + time
        return self.system_time

    def add_processing_time(self, time):
        self.processing_time = self.processing_time + time
        return self.processing_time

    def add_queue_time(self, time):
        self.queue_time = self.queue_time + time
        return self.queue_time

    def add_amount_returned(self):
        self.amount_returned = self.amount_returned + 1
        return self.amount_returned

    def set_arrival_time(self, time):
        self.arrival_time = time

    def set_departure_time(self, time):
        self.departure_time = time
