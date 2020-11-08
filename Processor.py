class Processor:

    def __init__(self, _id, _output_distribution):
        self._id = _id                                  # Identificador del procesador
        self._busy_status = False                        # Estado del procesador (libre u ocupado)
        self._processing_time = 0.0                      # Tiempo que el procesador pasa ocupado
        self._output_distribution = _output_distribution  # Distribución de salida de mensajes

    @property
    def id(self):
        return self._id

    @property
    def busy_status(self):
        return self._busy_status

    @busy_status.setter
    def busy_status(self, value):
        self.busy_status = value

    @property
    def processing_time(self):
        return self._processing_time

    @processing_time.setter
    def processing_time(self, value):
        self._processing_time = value

    @property
    def output_distribution(self):
        return self._output_distribution

    @output_distribution.setter
    def output_distribution(self, value):
        self._output_distribution = value
