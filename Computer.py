from Message import Message
from Processor import Processor


class Computer:

    def __init__(self, _id, _input_distribution):
        self._id = _id                                  # Identificador de la computadora (1, 2 o 3)
        self._input_distribution = _input_distribution  # Distribución de llega de mensajes externos
        self._queued_messages = []                      # Cola de mensajes
        self._processors_list = []                      # Lista de procesadores de la computadora
        return

    # --------------- Definición de Métodos Get y Set para atributos de clase Processor --------------- #

    @property
    def id(self):
        return self._id

    @property
    def input_distribution(self):
        return self._input_distribution
    
    @input_distribution.setter
    def input_distribution(self, value):
        self._input_distribution = value

    @property
    def queued_messages(self):
        return self._queued_messages
    
    @property
    def processors_list(self):
        return self._processors_list

    # --------------- FIN Definición de Métodos Get y Set para atributos de clase Processor --------------- #
    
    """
    Se agrega un procesador con un identificador y distribución de salidad, señalada por parámetros
    """
    def add_processor(self, id, output_dist):
        processor = Processor(id, output_dist)
        self._processors_list.append(processor)

    """
    Se agrega el id de un mensaje a la cola de mensajes
    """
    def add_queued_message(self, message_id):
        self._queued_messages.append(message_id)

    """
    Se remueve el id de un mensaje de la cola de mensajes
    """
    def pop_queued_message(self):
        message = -1
        if len(self._queued_messages) > 0:
            message = self._queued_messages.pop(0)
        return message
