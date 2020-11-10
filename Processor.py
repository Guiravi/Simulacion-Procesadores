class Processor:

    """
    Clase Procesador. Se utiliza para guardar las estadísticas de cada procesador. También contiene la distribución que utiliza para el tiempo de procesamiento
    """
    # Constructor
    def __init__(self, _id, _output_distribution):
        self._id = _id                                    # Identificador del procesador
        self._busy_status = False                         # Estado del procesador (libre u ocupado)
        self._processing_time = 0.0                       # Tiempo que el procesador pasa ocupado
        self._last_registered_clock = 0.0                 # Ultimo tiempo de reloj registrado (para calcular tiempo de procesamiento del mensaje)
        self._output_distribution = _output_distribution  # Distribución de salida de mensajes


    # --------------- Definición de Métodos Get y Set para atributos de clase Processor --------------- #

    @property
    def id(self):
        return self._id

    @property
    def busy_status(self):
        return self._busy_status

    @busy_status.setter
    def busy_status(self, value):
        self._busy_status = value

    @property
    def processing_time(self):
        return self._processing_time

    @processing_time.setter
    def processing_time(self, value):
        self._processing_time = value

    @property
    def last_registered_clock(self):
        return self._last_registered_clock

    @last_registered_clock.setter
    def last_registered_clock(self, value):
        self._last_registered_clock = value

    @property
    def output_distribution(self):
        return self._output_distribution

    @output_distribution.setter
    def output_distribution(self, value):
        self._output_distribution = value

    # --------------- FIN Definición de Métodos Get y Set para atributos de clase Processor --------------- #
    def update_processing_time(self, current_clock):
        """
        Método de clase
        Se añade el tiempo que se gastó en procesamiento, restándole al 
        reloj actual el tiempo en que empezó a procesar el mensaje
        """
        self.processing_time += (current_clock - self.last_registered_clock)