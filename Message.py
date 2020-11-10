class Message:

    # Constructor
    def __init__(self, _id):
        self._id = _id                           # Identificador del mensaje
        self._status = "TBD"                     # Estado del mensaje: S=Sent, R=Rejected o TBD=To Be Defined
        self._first_computer = 0                 # La computadora original que recibio el mensaje (2 o 3)
        self._last_computer = 0                  # La ultima computadora en la que estuvo el mensaje
        self._processing_time_1 = 0.0            # Tiempo de procesamiento que ha tenido el mensaje en la computadora 1
        self._processing_time_2 = 0.0            # Tiempo de procesamiento que ha tenido el mensaje en la computadora 2
        self._processing_time_3 = 0.0            # Tiempo de procesamiento que ha tenido el mensaje en la computadora 3
        self._queue_time = 0.0                   # Tiempo en cola
        self._transmission_time = 0.0             # Tiempo en transmision
        self._system_time = 0.0                  # Tiempo total en el sistema
        self._amount_returned = 0                # Cantidad de veces retornado a computadora 2 o 3 respectivamente
        self._last_registered_clock = 0.0        # Ultimo tiempo de reloj registrado (para calcular tiempo en cola o tiempo de procesamiento del mensaje)


    # --------------- Definición de Métodos Get y Set para atributos de clase Message --------------- #

    @property
    def id(self):
        return self._id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def first_computer(self):
        return self._first_computer

    @first_computer.setter
    def first_computer(self, value):
        self._first_computer = value

    @property
    def last_computer(self):
        return self._last_computer

    @last_computer.setter
    def last_computer(self, value):
        self._last_computer = value

    @property
    def processing_time_1(self):
        return self._processing_time_1

    @processing_time_1.setter
    def processing_time_1(self, value):
        self._processing_time_1 = value

    @property
    def processing_time_2(self):
        return self._processing_time_2

    @processing_time_2.setter
    def processing_time_2(self, value):
        self._processing_time_2 = value

    @property
    def processing_time_3(self):
        return self._processing_time_3

    @processing_time_3.setter
    def processing_time_3(self, value):
        self._processing_time_3 = value

    @property
    def queue_time(self):
        return self._queue_time

    @queue_time.setter
    def queue_time(self, value):
        self._queue_time = value

    @property
    def transmission_time(self):
        return self._transmission_time

    @transmission_time.setter
    def transmission_time(self, value):
        self._transmission_time = value

    @property
    def system_time(self):
        return self._system_time

    @system_time.setter
    def system_time(self, value):
        self._system_time = value

    @property
    def amount_returned(self):
        return self._amount_returned

    @amount_returned.setter
    def amount_returned(self, value):
        self._amount_returned = value

    @property
    def last_registered_clock(self):
        return self._last_registered_clock

    @last_registered_clock.setter
    def last_registered_clock(self, value):
        self._last_registered_clock = value

    # --------------- FIN Definición de Métodos Get y Set para atributos de clase Message --------------- #

    """
    Se añade el tiempo que duró el procesamiento del mensaje en la computadora 1, restándole al 
    reloj actual el tiempo en que empezó a procesar
    """
    def update_processing_time_1(self, current_clock):
        self._processing_time_1 += (current_clock - self._last_registered_clock)

    """
    Se añade el tiempo que duró el procesamiento del mensaje en la computadora 2, restándole al 
    reloj actual el tiempo en que empezó a procesar
    """
    def update_processing_time_2(self, current_clock):
        self._processing_time_2 += (current_clock - self._last_registered_clock)

    """
    Se añade el tiempo que duró el procesamiento del mensaje en la computadora 3, restándole al 
    reloj actual el tiempo en que empezó a procesar
    """
    def update_processing_time_3(self, current_clock):
        self._processing_time_3 += (current_clock - self._last_registered_clock)

    """
    Se añade el tiempo que duró en cola el mensaje, restándole al reloj actual el tiempo 
    en que empezó a esperar en cola
    """
    def update_queue_time(self, current_clock):
        self._queue_time += (current_clock - self._last_registered_clock)

    """
    Se añade el tiempo que duró el procesamiento del mensaje o el tiempo en cola, al tiempo total en el sistema. 
    """
    def update_system_time(self, current_clock):
        self._system_time += (current_clock - self._last_registered_clock)

    """
    Se coloca el estado del mensaje en enviado
    """
    def send(self):
        self._status = "S"
    
    """
    Se coloca el estado del mensaje en rechazado
    """
    def reject(self):
        self._status = "R"
    