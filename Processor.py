from Message import Message


class Processor:
    busy = False
    busy_time = 0.0
    busy_time_rejected_message = 0.0
    queue = [Message]
    input_dist = 0
    output_dist = 0

    def __init__(self):
        return

    def insert_message(self, message):
        self.queue.append(message)
