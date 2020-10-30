class Processor:

    def __init__(self, output_distribution):
        self.empty = True                               # Estado del procesador (libre u ocupado)
        self.processing_time = 0.0                      # Tiempo de procesamiento
        self.processing_time_rejected_message = 0.0     # Tiempo procesando mensajes rechazados
        self.output_distribution = output_distribution  # Distribución de salida de mensajes
        return

    def change_state(self):
        self.empty = not self.empty

    def empty(self):
        return self.empty

    def add_processing_time(self, time):
        self.processing_time = self.processing_time + time
        return self.processing_time

    def get_processing_time(self):
        return self.processing_time

    def add_processing_time_rejected_message(self, time):
        self.processing_time_rejected_message = self.processing_time_rejected_message + time
        return self.processing_time_rejected_message

    def get_processing_time_rejected_message(self):
        return self.processing_time_rejected_message

    def get_output_distribution(self):
        return self.output_distribution
