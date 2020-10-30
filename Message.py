class Message:
    system_time = 0.0
    processing_time = 0.0
    arrival_time = 0.0
    departure_time = 0.0
    queue_time = 0.0
    amount_returned = 0.0

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

    def insert_arrival_time(self, time):
        self.arrival_time = time

    def insert_departure_time(self, time):
        self.departure_time = time
