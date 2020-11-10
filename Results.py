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
        self.processor_0_busy_time.append(processor_list[0].processing_time)
        self.processor_1_busy_time.append(processor_list[1].processing_time)
        self.processor_2_busy_time.append(processor_list[2].processing_time)
        self.processor_3_busy_time.append(processor_list[3].processing_time)
    
    def add_messages_results(self, message_list):
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
        
        self.computer_1_busy_time_for_rejected.append(computer_1_time_rejected)
        self.computer_3_busy_time_for_rejected.append(computer_3_time_rejected)
        self.number_of_rejected_messages.append(number_of_rejected)
        self.number_of_sent_messages.append(number_of_sent)
        self.rejected_message_mean_time_in_system.append(total_rejected_messages_time_in_system / number_of_rejected)
        self.sent_message_mean_time_in_system.append(total_sent_messages_time_in_system / number_of_sent)
        self.message_mean_time_in_system.append(total_time_in_system / total_messages)
        self.message_mean_amount_of_returned.append(total_amount_returned / total_messages)
        self.message_mean_time_in_queue.append(total_time_in_queue / total_messages)
        self.message_mean_time_in_transmission.append(total_time_in_transmission / total_messages)
        self.message_mean_time_in_processing.append(total_time_in_processing / total_messages)

    def add_last_clock_of_run(self, clock):
        self.last_clock.append(clock)

    def percentage_processor_busy_time(self, run_number):
        percentage_0 = (self.processor_0_busy_time[run_number] / self.last_clock[run_number]) * 100
        percentage_1 = (self.processor_1_busy_time[run_number] / self.last_clock[run_number]) * 100
        percentage_2 = (self.processor_2_busy_time[run_number] / self.last_clock[run_number]) * 100
        percentage_3 = (self.processor_3_busy_time[run_number] / self.last_clock[run_number]) * 100

        return (percentage_0, percentage_1, percentage_2, percentage_3)

    def percentage_processor_busy_rejected(self, run_number):
        percentage_computer_1 = (self.computer_1_busy_time_for_rejected[run_number] / self.processor_0_busy_time[run_number]) * 100
        percentage_computer_3 = (self.computer_3_busy_time_for_rejected[run_number] / self.processor_3_busy_time[run_number]) * 100

        return (percentage_computer_1, percentage_computer_3)

    def percentage_rejected_messages(self, run_number):
        return (self.number_of_rejected_messages[run_number] / (self.number_of_sent_messages[run_number] + self.number_of_rejected_messages[run_number])) * 100
    
    def message_mean_system(self, run_number):
        return self.message_mean_time_in_system[run_number]

    def message_mean_returned(self, run_number):
        return self.message_mean_amount_of_returned[run_number]

    def message_mean_queue(self, run_number):
        return self.message_mean_time_in_queue[run_number]
    
    def message_mean_transmission(self, run_number):
        return self.message_mean_time_in_transmission[run_number]
    
    def percentage_message_processing(self, run_number):
        return (self.message_mean_time_in_processing[run_number] / self.message_mean_time_in_system[run_number]) * 100
    

    def finished_percentage_processor_busy_time(self):
        percentage_0 = 0.0
        percentage_1 = 0.0
        percentage_2 = 0.0
        percentage_3 = 0.0

        for i in range(len(self.processor_0_busy_time)):
            percentage_of_run = self.percentage_processor_busy_time(i)
            percentage_0 += percentage_of_run[0]
            percentage_1 += percentage_of_run[1]
            percentage_2 += percentage_of_run[2]
            percentage_3 += percentage_of_run[3]
        
        percentage_0 = percentage_0 / len(self.processor_0_busy_time)
        percentage_1 = percentage_1 / len(self.processor_0_busy_time)
        percentage_2 = percentage_2 / len(self.processor_0_busy_time)
        percentage_3 = percentage_3 / len(self.processor_0_busy_time)
        
        return (percentage_0, percentage_1, percentage_2, percentage_3)

    def finished_percentage_processor_busy_rejected(self):
        percentage_computer_1 = 0.0
        percentage_computer_3 = 0.0

        for i in range(len(self.computer_1_busy_time_for_rejected)):
            percentage_of_run = self.percentage_processor_busy_rejected(i)
            percentage_computer_1 += percentage_of_run[0]
            percentage_computer_3 += percentage_of_run[1]
        
        percentage_computer_1 = percentage_computer_1 / len(self.computer_1_busy_time_for_rejected)
        percentage_computer_3 = percentage_computer_3 / len(self.computer_1_busy_time_for_rejected)

        return (percentage_computer_1, percentage_computer_3)

    def finished_percentage_rejected_messages(self):
        percentage = 0.0
        for i in range(len(self.number_of_rejected_messages)):
            percentage += self.percentage_rejected_messages(i) 
        
        return percentage / len(self.number_of_rejected_messages)
    
    def finished_message_mean_system(self):
        mean = 0.0
        for i in range(len(self.message_mean_time_in_system)):
            mean += self.message_mean_system(i)
        
        return mean / len(self.message_mean_time_in_system)

    def finished_message_mean_returned(self):
        mean = 0.0
        for i in range(len(self.message_mean_amount_of_returned)):
            mean += self.message_mean_returned(i)
        
        return mean / len(self.message_mean_amount_of_returned)
        
    def finished_message_mean_queue(self):
        mean = 0.0
        for i in range(len(self.message_mean_time_in_queue)):
            mean += self.message_mean_queue(i)
        
        return mean / len(self.message_mean_time_in_queue)

    def finished_message_mean_transmission(self):
        mean = 0.0
        for i in range(len(self.message_mean_time_in_transmission)):
            mean += self.message_mean_transmission(i)
        
        return mean / len(self.message_mean_time_in_transmission)

    
    def finished_percentage_message_processing(self):
        percentage = 0.0

        for i in range(len(self.message_mean_time_in_processing)):
            percentage += self.percentage_message_processing(i)
        
        return percentage / len(self.message_mean_time_in_processing)


    def rejected_confidence_interval(self):
        mean = 0.0
        for y_i in self.rejected_message_mean_time_in_system:
            mean += y_i
        mean = mean / len(self.rejected_message_mean_time_in_system)
        variance = 0.0
        for y_i in self.rejected_message_mean_time_in_system:
            variance += (y_i - mean)**2
        variance = variance / (len(self.rejected_message_mean_time_in_system) - 1)
        interval = 2.26*math.sqrt(variance/len(self.rejected_message_mean_time_in_system))
        return (mean - interval, mean + interval)

    def sent_confidence_interval(self):
        mean = 0.0
        for y_i in self.sent_message_mean_time_in_system:
            mean += y_i
        mean = mean / len(self.sent_message_mean_time_in_system)
        variance = 0.0
        for y_i in self.sent_message_mean_time_in_system:
            variance += (y_i - mean)**2
        variance = variance / (len(self.sent_message_mean_time_in_system) - 1)
        interval = 2.26*math.sqrt(variance/len(self.sent_message_mean_time_in_system))
        return (mean - interval, mean + interval)

    def total_confidence_interval(self):
        mean = 0.0
        for y_i in self.message_mean_time_in_system:
            mean += y_i
        mean = mean / len(self.message_mean_time_in_system)
        variance = 0.0
        for y_i in self.message_mean_time_in_system:
            variance += (y_i - mean)**2
        variance = variance / (len(self.message_mean_time_in_system) - 1)
        interval = 2.26*math.sqrt(variance/len(self.message_mean_time_in_system))
        return (mean - interval, mean + interval)