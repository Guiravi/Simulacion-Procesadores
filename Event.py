class Event:

    def __init__(self, _id_event, _event_time):
        self._id_event = _id_event            # Identificador de evento (LMC1 SMC1 LMC2 SMC2P1 SMC2P2 LMC3 SMC3)
        self._id_message = None           # Identificador del mensaje con el que se realiza el evento
        self._event_time = _event_time    # Tiempo en el que ocurre el evento

    # --------------- Definición de Métodos Get y Set para atributos de clase Processor --------------- #

    @property
    def id_event(self):
        return self._id_event

    @property
    def id_message(self):
        return self._id_message

    @id_message.setter
    def id_message(self, value):
        self._id_message = value

    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value

    # --------------- FIN Definición de Métodos Get y Set para atributos de clase Processor --------------- #
 