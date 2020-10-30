from Message import Message
from Processor import Processor


class Computer:

    def __init__(self, input_distribution):
        self.input_distribution = input_distribution    # Distribución de llega de mensajes externos
        self.queue_messages = [Message]                 # Cola de mensajes
        self.processors_list = [Processor]              # Lista de procesadores de la computadora
        return

    def add_processor(self, output_dist):
        processor = Processor(output_dist)
        self.processors_list.append(processor)

    def get_input_distribution(self):
        return self.input_distribution

    def get_output_distribution(self, i):
        return self.processors_list[i].get_output_distribution()

    def insert_message(self, message):
        self.queue_messages.append(message)

    def pop_message(self):
        message = -1
        if len(self.queue_messages) > 0:
            message = self.queue_messages.pop(0)
        return message
