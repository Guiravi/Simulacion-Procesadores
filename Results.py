import math
class Results:
    """
    Clase Resultados. Esta clase se utiliza para guardar y calcular las estadísticas finales de cada corrida.
    Como se guarda cada corrida, al finalizar todas las ejecuciones, también calcula las estadísticas finales tomando en cuenta todas las corridas.
    """

    # Constructor
    def __init__(self):
        self.processor_0_busy_time = []    # Tiempo en el que el procesador de la computadora 1 pasó ocupado en procesamiento
        self.processor_1_busy_time = []    # Tiempo en el que el procesador 1 de la computadora 2 pasó ocupado en procesamiento
        self.processor_2_busy_time = []    # Tiempo en el que el procesador 2 de la computadora 2 pasó ocupado en procesamiento
        self.processor_3_busy_time = []    # Tiempo en el que el procesador de la computadora 3 pasó ocupado en procesamiento

        self.computer_1_busy_time_for_rejected = []    # Tiempo en el que la computadora 1 pasó ocupado en procesamiento con mensajes que fueron rechazados
        self.computer_3_busy_time_for_rejected = []    # Tiempo en el que la computadora 3 pasó ocupado en procesamiento con mensajes que fueron rechazados

        self.number_of_rejected_messages = []    # Cantidad de mensajes que fueron rechazados
        self.number_of_sent_messages = []        # Cantidad de mensajes que fueron enviados
        self.rejected_message_mean_time_in_system = []
        self.sent_message_mean_time_in_system = []

        self.message_mean_time_in_system = []           # Tiempo promedio de mensajes en el sistema
        self.message_mean_amount_of_returned = []       # Cantidad de mensajes promedio rechazados
        self.message_mean_time_in_queue = []            # Tiempo promedio de mensajes en la cola
        self.message_mean_time_in_transmission = []     # Tiempo promedio de mensajes en transmisión
        self.message_mean_time_in_processing = []       # Tiempo promedio de mensajes en procesamiento

        self.last_clock = []    # Reloj final de la simulación

    def add_processor_busy_time(self, processor_list):
        """
        Método de clase 
        Agrega los tiempos que pasaron ocupados cada procesador en cada corrida
        """
        self.processor_0_busy_time.append(processor_list[0].processing_time)
        self.processor_1_busy_time.append(processor_list[1].processing_time)
        self.processor_2_busy_time.append(processor_list[2].processing_time)
        self.processor_3_busy_time.append(processor_list[3].processing_time)
    
    def add_messages_results(self, message_list):
        """
        Método de clase
        Se encarga de guardar los resultados de las estadísticas de los mensajes por corrida
        """

        # Resultados totales de la corrida para los mensajes
        total_messages = 0
        total_time_in_system = 0.0
        total_amount_returned = 0
        total_time_in_queue = 0.0
        total_time_in_transmission = 0.0
        total_time_in_processing = 0.0
        total_rejected_messages_time_in_system = 0.0
        total_sent_messages_time_in_system = 0.0
        
        number_of_rejected = 0
        number_of_sent = 0
        computer_1_time_rejected = 0.0
        computer_3_time_rejected = 0.0
        for message in message_list:
            # Solo se consideran los mensajes que fueron enviados o rechazados para las estadísticas
            if (message.status == "S" or message.status == "R"):
                total_messages += 1
                total_time_in_system += message.system_time
                total_amount_returned += message.amount_returned
                total_time_in_queue += message.queue_time
                total_time_in_transmission += message.transmission_time
                total_time_in_processing += message.processing_time_1 + message.processing_time_2 + message.processing_time_3
                
                if (message.status == "R"):
                    number_of_rejected += 1
                    computer_1_time_rejected += message.processing_time_1
                    computer_3_time_rejected += message.processing_time_3
                    total_rejected_messages_time_in_system += message.system_time
                else:
                    number_of_sent += 1
                    total_sent_messages_time_in_system += message.system_time
        
        # Se guarda el tiempo que pasa la computadora 1 procesando mensajes que terminaron rechazados
        self.computer_1_busy_time_for_rejected.append(computer_1_time_rejected)
        # Se guarda el tiempo que pasa la computadora 3 procesando mensajes que terminaron rechazados
        self.computer_3_busy_time_for_rejected.append(computer_3_time_rejected)
        # Se guarda el número de mensajes rechazados
        self.number_of_rejected_messages.append(number_of_rejected)
        # Se guarda el número de mensajes enviados
        self.number_of_sent_messages.append(number_of_sent)
        # Se calcula y se guarda el tiempo promedio de los mensajes rechazados en el sistema (para intervalos de confianza)
        self.rejected_message_mean_time_in_system.append(total_rejected_messages_time_in_system / number_of_rejected)
        # Se calcula y se guarda el tiempo promedio de los mensajes enviados en el sistema (para intervalos de confianza)
        self.sent_message_mean_time_in_system.append(total_sent_messages_time_in_system / number_of_sent)
        # Se calcula y se guarda el tiempo promedio de los mensajes en el sistema
        self.message_mean_time_in_system.append(total_time_in_system / total_messages)
        # Se calcula y se guarda el promedio de veces que los mensajes fueron devueltos
        self.message_mean_amount_of_returned.append(total_amount_returned / total_messages)
        # Se calcula y se guarda el tiempo promedio en cola de los mensajes
        self.message_mean_time_in_queue.append(total_time_in_queue / total_messages)
        # Se calcula y se guarda el tiempo promedio en transmisión de los mensajes
        self.message_mean_time_in_transmission.append(total_time_in_transmission / total_messages)
        # Se calcula y se guarda el tiempo promedio en procesamiento de los mensajes
        self.message_mean_time_in_processing.append(total_time_in_processing / total_messages)

    def add_last_clock_of_run(self, clock):
        """
        Método de clase
        Agrega el tiempo de reloj en el que finalizó la simulación
        """
        self.last_clock.append(clock)

    def percentage_processor_busy_time(self, run_number):
        """
        Método de clase
        Calcula el porcentaje de tiempo que cada procesador pasó ocupado
        """
        percentage_0 = (self.processor_0_busy_time[run_number] / self.last_clock[run_number]) * 100
        percentage_1 = (self.processor_1_busy_time[run_number] / self.last_clock[run_number]) * 100
        percentage_2 = (self.processor_2_busy_time[run_number] / self.last_clock[run_number]) * 100
        percentage_3 = (self.processor_3_busy_time[run_number] / self.last_clock[run_number]) * 100

        return (percentage_0, percentage_1, percentage_2, percentage_3)

    def percentage_processor_busy_rejected(self, run_number):
        """
        Método de clase
        Calcula el porcentaje del tiempo que pasaron ocupados la computadora 1 y 3 en procesamiento de mensajes que fueron rechazados
        """
        percentage_computer_1 = (self.computer_1_busy_time_for_rejected[run_number] / self.processor_0_busy_time[run_number]) * 100
        percentage_computer_3 = (self.computer_3_busy_time_for_rejected[run_number] / self.processor_3_busy_time[run_number]) * 100

        return (percentage_computer_1, percentage_computer_3)

    def percentage_rejected_messages(self, run_number):
        """
        Método de clase
        Calcula el porcentaje de mensajes que fueron rechazados
        """
        return (self.number_of_rejected_messages[run_number] / (self.number_of_sent_messages[run_number] + self.number_of_rejected_messages[run_number])) * 100
    
    def message_mean_system(self, run_number):
        """
        Método de clase
        Retorna el tiempo promedio en el sistema de los mensajes para un número de corrida específico
        """
        return self.message_mean_time_in_system[run_number]

    def message_mean_returned(self, run_number):
        """
        Método de clase 
        Retorna la cantidad promedio que los mensajes fueron devueltos para un número de corrida específico
        """
        return self.message_mean_amount_of_returned[run_number]

    def message_mean_queue(self, run_number):
        """
        Método de clase 
        Retorna el tiempo promedio en cola de los mensajes para un número de corrida específico
        """
        return self.message_mean_time_in_queue[run_number]
    
    def message_mean_transmission(self, run_number):
        """
        Método de clase
        Retorna el tiempo promedio en transmisión de los mensajes para un número de corrida específico
        """
        return self.message_mean_time_in_transmission[run_number]
    
    def percentage_message_processing(self, run_number):
        """
        Método de clase
        Calcula y retorna el porcentaje de tiempo que pasaron los mensajes en procesamiento
        """
        return (self.message_mean_time_in_processing[run_number] / self.message_mean_time_in_system[run_number]) * 100
    

    def finished_percentage_processor_busy_time(self):
        """
        Método de clase
        Calcula el porcentaje promedio que pasaron los procesadores ocupados para cuando se finalizan todas las corridas
        Se obtienen los porcentajes de cada corrida, y se calcula el promedio de todos los porcentajes
        """
        percentage_0 = 0.0
        percentage_1 = 0.0
        percentage_2 = 0.0
        percentage_3 = 0.0

        # Se obtienen y suman los porcentajes de cada corrida
        for i in range(len(self.processor_0_busy_time)):
            percentage_of_run = self.percentage_processor_busy_time(i)
            percentage_0 += percentage_of_run[0]
            percentage_1 += percentage_of_run[1]
            percentage_2 += percentage_of_run[2]
            percentage_3 += percentage_of_run[3]
        
        # Se calcula el promedio de cada porcentaje de cada procesador
        percentage_0 = percentage_0 / len(self.processor_0_busy_time)
        percentage_1 = percentage_1 / len(self.processor_0_busy_time)
        percentage_2 = percentage_2 / len(self.processor_0_busy_time)
        percentage_3 = percentage_3 / len(self.processor_0_busy_time)
        
        return (percentage_0, percentage_1, percentage_2, percentage_3)

    def finished_percentage_processor_busy_rejected(self):
        """
        Método de clase
        Calcula el porcentaje promedio que pasaron los procesadores ocupados en mensajes que fueron rechazados 
        para cuando se finalizan todas las corridas
        Se obtienen los porcentajes de cada corrida, y se calcula el promedio de todos los porcentajes
        """
        percentage_computer_1 = 0.0
        percentage_computer_3 = 0.0

        # Se obtienen y suman los porcentajes de cada corrida
        for i in range(len(self.computer_1_busy_time_for_rejected)):
            percentage_of_run = self.percentage_processor_busy_rejected(i)
            percentage_computer_1 += percentage_of_run[0]
            percentage_computer_3 += percentage_of_run[1]
        
        # Se calcula el promedio de cada porcentaje de cada computadora
        percentage_computer_1 = percentage_computer_1 / len(self.computer_1_busy_time_for_rejected)
        percentage_computer_3 = percentage_computer_3 / len(self.computer_1_busy_time_for_rejected)

        return (percentage_computer_1, percentage_computer_3)

    def finished_percentage_rejected_messages(self):
        """
        Método de clase
        Calcula el porcentaje promedio de mensajes que fueron rechazados al finalizar todas las corridas
        Se obtienen los porcentajes de cada corrida, y se calcula el promedio de todos los porcentajes
        """
        percentage = 0.0
        
        # Se obtienen y suman todos los porcentajes de cada corrida
        for i in range(len(self.number_of_rejected_messages)):
            percentage += self.percentage_rejected_messages(i) 
        
        # Se calcula el porcentaje promedio de mensajes rechazados
        return percentage / len(self.number_of_rejected_messages)
    
    def finished_message_mean_system(self):
        """
        Método de clase
        Calcula el tiempo promedio en el sistema de los mensajes para cuando se finalizan todas las corridas
        Se obtienen todos los tiempos promedios de cada corrida y se calcula el promedio de esto
        """
        mean = 0.0
        
        # Se obtienen y suman todos los tiempos de cada corrida
        for i in range(len(self.message_mean_time_in_system)):
            mean += self.message_mean_system(i)
        
        # Se calcula el tiempo promedio en el sistema para todas las corridas
        return mean / len(self.message_mean_time_in_system)

    def finished_message_mean_returned(self):
        """
        Método de clase
        Calcula el promedio de las veces en las que un mensaje fue retornado para cuando se finalizan todas las corridas
        Se obtienen el promedio de veces que los mensajes fueron devueltos en cada corrida y se calcula el promedio de esto
        """
        mean = 0.0
        # Se acumulan la cantidad de veces que fue retornado cada mensaje
        for i in range(len(self.message_mean_amount_of_returned)):
            mean += self.message_mean_returned(i)
        # Se divide el acumulador entre la cantidad de mensajes totales
        return mean / len(self.message_mean_amount_of_returned)
        
    def finished_message_mean_queue(self):
        """
        Método de clase
        Calcula el tiempo promedio que los mensajes pasan en cola para cuando se finalizan todas las corridas
        Se obtienen el tiempo promedio que los mensajes pasan en cola en cada corrida y se calcula el promedio de esto
        """
        mean = 0.0
        # Se obtienen y suman todos los tiempos de cada corrida
        for i in range(len(self.message_mean_time_in_queue)):
            mean += self.message_mean_queue(i)

        # Se calcula el tiempo promedio en el sistema para todas las corridas
        return mean / len(self.message_mean_time_in_queue)

    def finished_message_mean_transmission(self):
        """
        Método de clase
        Calcula el tiempo promedio que los mensajes pasan en transmisión para cuando se finalizan todas las corridas
        Se obtienen el tiempo promedio que los mensajes pasan en cola en cada corrida y se calcula el promedio de esto
        """
        mean = 0.0
        # Se acumulan la cantidad de tiempo que pasó en transmisión cada mensaje
        for i in range(len(self.message_mean_time_in_transmission)):
            mean += self.message_mean_transmission(i)
        
        # Se calcula el tiempo promedio en el sistema para todas las corridas
        return mean / len(self.message_mean_time_in_transmission)

    
    def finished_percentage_message_processing(self):
        """
        Método de clase
        Calcula el procentaje promedio de tiempo que los mensajes pasan en procesamiento para cuando se finalizan todas las corridas
        Se obtienen el porcentaje promedio de tiempo que los mensajes pasan en procesamiento en cada corrida y se calcula el promedio de esto
        """
        percentage = 0.0
        
        # Se obtienen los porcentajes de cada corrida y se suman
        for i in range(len(self.message_mean_time_in_processing)):
            percentage += self.percentage_message_processing(i)
        
        # Se calcula el tiempo promedio en el sistema para todas las corridas
        return percentage / len(self.message_mean_time_in_processing)


    def rejected_confidence_interval(self):
        """
        Método de clase
        Calcula el intervalo de confianza del tiempo promedio del sistema de los mensajes rechazados
        """
        mean = 0.0
        # Se calcula la media muestral
        for y_i in self.rejected_message_mean_time_in_system:
            mean += y_i
        mean = mean / len(self.rejected_message_mean_time_in_system)
        # Se calcula la Varianza muestral
        variance = 0.0
        for y_i in self.rejected_message_mean_time_in_system:
            variance += (y_i - mean)**2
        variance = variance / (len(self.rejected_message_mean_time_in_system) - 1)
        # Se realiza el calculo de desviación para obtener el intervalo
        interval = 2.26*math.sqrt(variance/len(self.rejected_message_mean_time_in_system))
        return (mean - interval, mean + interval)

    def sent_confidence_interval(self):
        """
        Método de clase
        Calcula el intervalo de confianza del tiempo promedio del sistema de los mensajes enviados
        """
        # Se calcula la media muestral
        mean = 0.0
        for y_i in self.sent_message_mean_time_in_system:
            mean += y_i
        mean = mean / len(self.sent_message_mean_time_in_system)
        # Se calcula la Varianza muestral
        variance = 0.0
        for y_i in self.sent_message_mean_time_in_system:
            variance += (y_i - mean)**2
        variance = variance / (len(self.sent_message_mean_time_in_system) - 1)
        # Se realiza el calculo de desviación para obtener el intervalo
        interval = 2.26*math.sqrt(variance/len(self.sent_message_mean_time_in_system))
        return (mean - interval, mean + interval)

    def total_confidence_interval(self):
        """
        Método de clase
        Calcula el intervalo de confianza del tiempo promedio del sistema de todos los mensajes
        """
        # Se calcula la media muestral
        mean = 0.0
        for y_i in self.message_mean_time_in_system:
            mean += y_i
        mean = mean / len(self.message_mean_time_in_system)
        # Se calcula la Varianza muestral
        variance = 0.0
        for y_i in self.message_mean_time_in_system:
            variance += (y_i - mean)**2
        variance = variance / (len(self.message_mean_time_in_system) - 1)
        # Se realiza el calculo de desviación para obtener el intervalo
        interval = 2.26*math.sqrt(variance/len(self.message_mean_time_in_system))
        return (mean - interval, mean + interval)