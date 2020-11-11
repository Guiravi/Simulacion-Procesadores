from Computer import Computer
from Distribution import Distribution
from Distribution import calculate_uniform
from Event import Event
from Interface import Interface
from Message import Message
from Processor import Processor
from Results import Results

class Simulation:
    """
    Clase Simulación. En esta clase se controla la simulación basada en eventos.
    En esta clase se implementan los métodos que se debe realizar para cada evento en específico (LMC1, LMC2, LMC3, SMC1, SMC2P1, SMC2P2, SCM3)
    """
    # Constructor
    def __init__(self):
        self.clock = 0.0                # Reloj de la simulacion
        self.number_of_runs = 0         # Cantidad de veces a ejecutar la simulacion
        self.simulation_time = 0.0      # Tiempo de simulacion por corrida
        self.max = 0.0                  # Valor utilizado como infinito (se cambia a 4 * Tiempo de simulacion)
        self.x1_probability = 0.0       # Probabilidad de X1
        self.x2_probability = 0.0       # Probabilidad de X2
        self.x3_probability = 0.0       # Probabilidad de X3

        self.distribution_list = {}     # Contiene D1, D2, D3, D4, D5 y D6
        self.event_list = {}            # Contiene la lista de eventos para programar
        self.message_list = []          # Contiene todos los mensajes que se crean en una corrida
        self.processor_list = []        # Contiene todos los procesadores utilizados en la simulacion
        self.LMC1_list = []             # Lista ordenada de mensajes que deben llegar a la computadora 1
        self.LMC2_list = []             # Lista ordenada de mensajes que deben llegar a la computadora 2
        self.LMC3_list = []             # Lista ordenada de mensajes que deben llegar a la computadora 3
        
        self.results = Results()        # Objeto que contiene los resultados de cada corrida

        self.interface = Interface()    # Instancia para utilizar la interfaz de consola
        self.computer_1 = None          # Instancia de la Computadora 1 de la Simulación
        self.computer_2 = None          # Instancia de la Computadora 2 de la Simulación
        self.computer_3 = None          # Instancia de la Computadora 3 de la Simulación

    def run(self):
        """
        Método de clase
        En este método se hace el procesamiento general de la simulación
        """
        # Se solicitan y obtienen los datos de inicio al usuario
        self.get_user_input()
        # Se crean los eventos iniciales
        self.createEvents()
        # Se crean las computadoras y sus procesadores
        self.createComputers()
        # Comienza las iteraciones por las n simulaciones indicadas por el usuario
        for i in range(self.number_of_runs):
            # Se imprime el número de simulación
            self.interface.print_number_of_run(i)
            # Se ingresan los primeros mensajes de llegada en la computadora 2 y 3 y se programan los eventos
            self.message_list.append(Message(0))
            self.message_list.append(Message(1))
            self.event_list["LMC2"].id_message = 0
            self.event_list["LMC3"].id_message = 1
            self.LMC2_list.append((0, 0))
            self.LMC3_list.append((1, 0))
            # Se relizan de manera cíclica todos los eventos de la simulación
            self.do_events()

            # Guardar datos para calcular estadisticas
            self.results.add_processor_busy_time(self.processor_list)
            self.results.add_messages_results(self.message_list)
            self.results.add_last_clock_of_run(self.clock)
            
            # Imprimir estadisticas de la corrida
            self.print_statistics(i)
            # Se reinican los datos para una nueva corrida
            self.reset_run()
        # Imprimir estadisticas finales
        self.print_final_statistics()
        
    def get_user_input(self):
        """
        Método de clase
        Se obtienen cada uno de los datos del usuario necesarios para la simulación
        """
        # Se le solicita al usuario la cantidad de simulaciones
        self.number_of_runs = self.interface.ask_number_of_runs()
        # Se le solicita al usuario el tiempo que debe durar cada simulación
        self.simulation_time = self.interface.ask_simulation_time()
        # Se fija el valor de max o infinito en la simulación
        self.max = 4 * self.simulation_time  # Actualiza el valor de max
        # Se piden los datos de cada una de las distribuciones
        self.set_simulation_distributions()

        # Se asignan las probabilidades de retorno o rechazo de un mensaje por parte de los procesadores
        self.x1_probability = self.interface.ask_x_probability(1)
        self.x2_probability = self.interface.ask_x_probability(2)
        self.x3_probability = self.interface.ask_x_probability(3)

    def set_simulation_distributions(self):
        """
        Método de clase
        Se inicializan cada una de las simulaciones y sus respectivos parámetros
        """
        # Se crea un diccionario para manejar los identificadores de cada distribución
        distribution_dictionary = {1: "Direct",
                                   2: "TLC",
                                   3: "Uniform",
                                   4: "Exponential",
                                   5: "Density"}
        # Se realiza la solicitud de los datos de cada una de las 6 distribuciones
        for i in range(6):
            dist = Distribution()
            # Se pregunta cual distribución desa asignar a la distribución de la simulación: D_i 
            option = self.interface.ask_distribution("D" + str(i+1))
            # Según la distribución señalada entonces se asígna el identificador
            dist.id = distribution_dictionary[option]
            # Se piden los parámetros que necesita la distribución elegida
            self.set_dist_parameters(dist)
            # Agrega la distribución al diccionario de distribuciones en su ubicación asociada
            self.distribution_list["D"+str(i+1)] = dist

    def set_dist_parameters(self, dist):
        """
        Método de clase
        Se inicializan los respectivos parámetros de la distribución: dist
        """
        if (dist.id == "Direct"): # ¿Es una distribución normal directa?
            # Se inicializan los parámetros miu y sigma^2
            parameters = self.interface.ask_normal()
            dist.miu = parameters[0]
            dist.sigma2 = parameters[1]
        elif (dist.id == "TLC"): # ¿Es una distribución normal por el método de convolución?
            # Se inicializan los parámetros miu y sigma^2
            parameters = self.interface.ask_normal()
            dist.miu = parameters[0]
            dist.sigma2 = parameters[1]
        elif (dist.id == "Uniform"): # ¿Es una distribución uniforme?
            # Se inicializan los parámetros a y b
            parameters = self.interface.ask_uniform()
            dist.a = parameters[0]
            dist.b = parameters[1]
        elif (dist.id == "Exponential"): # ¿Es una distribución exponencial?
            # Se inicializa el parámetro lambda
            parameters = self.interface.ask_exponential()
            dist.lambd = parameters
        else: # ¿Es una distribución de función de densidad?
            # Se inicializan los parámetros k, a y b
            parameters = self.interface.ask_density()
            dist.k = parameters[0]
            dist.a = parameters[1]
            dist.b = parameters[2]

    def createEvents(self):
        """
        Método de clase
        Se inicializan cada unos de los eventos que son necesarios para la simulación, los que tienen max están desprogramados
        y los que tienen el valor de 0 están programados al momento 0 del reloj
        """
        self.event_list["LMC1"] = (Event("LMC1", self.max))
        self.event_list["LMC2"] = (Event("LMC2", 0))
        self.event_list["LMC3"] = (Event("LMC3", 0))
        self.event_list["SMC1"] = (Event("SMC1", self.max))
        self.event_list["SMC2P1"] = (Event("SMC2P1", self.max))
        self.event_list["SMC2P2"] = (Event("SMC2P2", self.max))
        self.event_list["SMC3"] = (Event("SMC3", self.max))

    def createComputers(self):
        """
        Método de clase
        Se crean las computadoras y sus respectivos procesadores
        """
        # Se crea la computadora 1 y se inicializa su distribución de arribos en None y su identificador en 1
        self.computer_1 = Computer(1, None)
        # Se crea el procesador con identificador 0 y distribución de salida D6
        self.computer_1.add_processor(0, self.distribution_list["D6"])
        # Se agrega el procesador a la lista de procesadores
        self.processor_list.append(self.computer_1.processors_list[0])

        # Se crea la computadora 2 y se inicializa su distribución de arribos en D1 y su identificador en 2
        self.computer_2 = Computer(2, self.distribution_list["D1"])
        # Se crea el procesador con identificador 1 y distribución de salida D2
        self.computer_2.add_processor(1, self.distribution_list["D2"])
        # Se crea el procesador con identificador 2 y distribución de salida D3
        self.computer_2.add_processor(2, self.distribution_list["D3"])
        # Se agrega el procesador a la lista de procesadores
        self.processor_list.append(self.computer_2.processors_list[0])
        # Se agrega el procesador a la lista de procesadores
        self.processor_list.append(self.computer_2.processors_list[1])

        # Se crea la computadora 3 y se inicializa su distribución de arribos en D4 y su identificador en 3
        self.computer_3 = Computer(3, self.distribution_list["D4"])
        # Se crea el procesador con identificador 3 y distribución de salida D5
        self.computer_3.add_processor(3, self.distribution_list["D5"])
        # Se agrega el procesador a la lista de procesadores
        self.processor_list.append(self.computer_3.processors_list[0])

    def print_statistics(self, run_number):
        """
        Método de clase
        Se realiza la impresión de las estádisticas correspondientes al número de corrida señalado
        """
        # Se imprime el porcentaje de tiempo que pasó el procesador ocupado en general y con mensajes rechazados
        self.interface.print_percentage_processor_busy(self.results.percentage_processor_busy_time(run_number))
        self.interface.print_percentage_processor_busy_rejected(self.results.percentage_processor_busy_rejected(run_number))
        # Se imprime el porcentaje de mensajes rechazados
        self.interface.print_percentage_rejected_messages(self.results.percentage_rejected_messages(run_number))

        # Se imprime el promedio de tiempo en el sistema de un mensaje
        self.interface.print_mean_system_time(self.results.message_mean_system(run_number))
        # Se imprime el promedio de la cantidad de veces que fue devuelto un mensaje
        self.interface.print_mean_amount_returned(self.results.message_mean_returned(run_number))
        # Se imprime el promedio de tiempo en cola en el sistema de un mensaje
        self.interface.print_mean_queue_time(self.results.message_mean_queue(run_number))
        # Se imprime el promedio de tiempo en transmisión en el sistema de un mensaje
        self.interface.print_mean_transmission_time(self.results.message_mean_transmission(run_number))
        # Se imprime el promedio de tiempo en procesamiento en el sistema de un mensaje
        self.interface.print_percentage_in_processing_time(self.results.percentage_message_processing(run_number))

    def print_final_statistics(self):
        """
        Método de clase
        Realiza la impresión de todas las estadísticas finales
        """
        print("---------------------ESTADÍSTICAS FINALES---------------------\n")
        # Se imprime el porcentaje de tiempo que pasó el procesador ocupado en general y con mensajes rechazados
        self.interface.print_percentage_processor_busy(self.results.finished_percentage_processor_busy_time())
        self.interface.print_percentage_processor_busy_rejected(self.results.finished_percentage_processor_busy_rejected())
        # Se imprime el porcentaje de mensajes rechazados
        self.interface.print_percentage_rejected_messages(self.results.finished_percentage_rejected_messages())

        # Se imprime el promedio de tiempo en el sistema de un mensaje
        self.interface.print_mean_system_time(self.results.finished_message_mean_system())
        # Se imprime el promedio de la cantidad de veces que fue devuelto un mensaje
        self.interface.print_mean_amount_returned(self.results.finished_message_mean_returned())
        # Se imprime el promedio de tiempo en cola en el sistema de un mensaje
        self.interface.print_mean_queue_time(self.results.finished_message_mean_queue())
        # Se imprime el promedio de tiempo en transmisión en el sistema de un mensaje
        self.interface.print_mean_transmission_time(self.results.finished_message_mean_transmission())
        # Se imprime el promedio de tiempo en procesamiento en el sistema de un mensaje
        self.interface.print_percentage_in_processing_time(self.results.finished_percentage_message_processing())
        
        # Se imprime el intervalo de confianza para el tiempo promedio en el sistema de los mensajes rechazados
        self.interface.print_confidence_interval_rejected(self.results.rejected_confidence_interval())
        # Se imprime el intervalo de confianza para el tiempo promedio en el sistema de los mensajes enviados
        self.interface.print_confidence_interval_sent(self.results.sent_confidence_interval())
        # Se imprime el intervalo de confianza para el tiempo promedio en el sistema de todos los mensajes
        self.interface.print_confidence_interval_total(self.results.total_confidence_interval())

    def reset_run(self):
        """
        Método de clase
        Reinicia todos los valores para poder iniciar la siguiente simulación
        """
        # Limpia la lista de mensajes
        del self.message_list[:]

        # Limpia las listas ordenadas de mensajes por llegar a la computadora 1, 2 y 3
        self.LMC1_list.clear()
        self.LMC2_list.clear()
        self.LMC3_list.clear()

        # Reinicia el valor inicial de todos los eventos
        self.event_list["LMC1"].event_time = self.max
        self.event_list["LMC2"].event_time = 0
        self.event_list["LMC3"].event_time = 0
        self.event_list["SMC1"].event_time = self.max
        self.event_list["SMC2P1"].event_time = self.max
        self.event_list["SMC2P2"].event_time = self.max
        self.event_list["SMC3"].event_time = self.max

        # Reinicia los valores de cada procesador
        for processor in self.processor_list:
            processor.busy_status = False
            processor.processing_time = 0.0
            processor.last_registered_clock = 0.0
        
        # Limpia las colas de mensajes
        self.computer_1.queued_messages.clear()
        self.computer_2.queued_messages.clear()
        self.computer_3.queued_messages.clear()

    def do_events(self):
        """
        Método de clase
        Se realiza la ejecución correspondiente a una simulación
        """
        # Se indica que no ha terminado la corrida de la simulación
        run_finished = False
        while(run_finished == False): # ¿No ha acabado la corrida de la simulación?
            # Obtenga el mínimo de los eventos
            min_ocurrence_event = min(self.event_list, key=lambda x: self.event_list[x].event_time)

            if (min_ocurrence_event == "LMC1"): # ¿Es el evento LMC1?
                # Realice el evento
                self.do_LMC1_event()
            elif(min_ocurrence_event == "LMC2"): # ¿Es el evento LMC2?
                # Realice el evento
                self.do_LMC2_event()
            elif(min_ocurrence_event == "LMC3"): # ¿Es el evento LMC3?
                # Realice el evento
                self.do_LMC3_event()
            elif(min_ocurrence_event == "SMC1"): # ¿Es el evento SMC1?
                # Realice el evento
                self.do_SMC1_event()
            elif(min_ocurrence_event == "SMC2P1"): # ¿Es el evento SMC2P1?
                # Realice el evento
                self.do_SMC2P1_event()
            elif(min_ocurrence_event == "SMC2P2"): # ¿Es el evento SMC2P2?
                # Realice el evento
                self.do_SMC2P2_event()
            elif(min_ocurrence_event == "SMC3"): # ¿Es el evento SMC3?
                # Realice el evento
                self.do_SMC3_event()

            if (self.clock >= self.simulation_time): # ¿Acabo el tiempo de simulación?
                # indique que la simulación ya acabó
                run_finished = True
        
        # Actualice el tiempo de procesamiento de los procesadores que no terminaron de procesar
        self.update_remaining_processing_times()
        
    def update_remaining_processing_times(self):
        """
        Método de clase
        Se actualizan los tiempos de procesamiento de cada uno de los procesadores que no terminaron de trabajar al final
        de la simulación
        """
        # Recorra cada uno de los procesadores
        for processor in self.processor_list:
            if processor.busy_status == True: # ¿El procesador estaba trabajando cuando terminó la simulación?
                # Actualice su tiempo de procesamiento
                processor.update_processing_time(self.clock)

    def do_LMC1_event(self):
        """
        Este es el método que ejecuta el evento llega mensaje a la computadora 1
        """
        # Se actualiza el reloj al tiempo del evento
        self.clock = self.event_list["LMC1"].event_time
        # Se obtiene el mensaje que está llegando a la computadora 1
        event_message = self.message_list[self.event_list["LMC1"].id_message]
        # Se suma el tiempo de transmisión al tiempo del mensaje en el sistema y en transmisión
        event_message.system_time += 20.0
        event_message.transmission_time += 20.0
        
        if (self.computer_1.processors_list[0].busy_status == False):  # ¿Está el procesador libre?
            # Se asigna el procesador
            assigned_processor = self.computer_1.processors_list[0]
            # Se programa el evento para que el procesador seleccionado procese el mensaje
            self.event_list["SMC1"].event_time = self.clock + assigned_processor.output_distribution.calculate()
            self.event_list["SMC1"].id_message = event_message.id
            # Se cambia el estado del procesador a ocupado
            assigned_processor.busy_status = True
            # Se guarda el momento en el que el mensaje empezó a ser procesado
            event_message.last_registered_clock = self.clock
            # Se guarda el momento en el que el procesador empezó a procesar el mensaje
            assigned_processor.last_registered_clock = self.clock
        else:
            # Se ingresa el mensaje a la cola de la computadora
            self.computer_1.add_queued_message(event_message.id)
            # Se guarda el momento en el que el mensaje empezó a esperar en cola
            event_message.last_registered_clock = self.clock
        
        # Se saca de la lista ordenada de mensajes que deben llegar a la computadora 1 el mensaje que ya se procesó o puso en cola
        self.LMC1_list.remove((event_message.id, self.clock))
        
        if (len(self.LMC1_list) != 0):
            # Se busca el próximo mensaje que tiene que llegar a la computadora 1
            next_event_parameters = min(self.LMC1_list, key= lambda x: x[1]) # Devuelve (id_mensaje, tiempo_ocurrencia)
            # Se programa el siguiente Evento LMC1
            self.event_list["LMC1"].id_message = next_event_parameters[0]
            self.event_list["LMC1"].event_time = next_event_parameters[1]
        else:
            # Se desprograma el evento LMC1
            self.event_list["LMC1"].event_time = self.max

    def do_LMC2_event(self):
        """
        Este es el método que ejecuta el evento llega mensaje a la computadora 2
        """
        # Se actualiza el reloj al tiempo del evento
        self.clock = self.event_list["LMC2"].event_time
        # Se obtiene el mensaje que está llegando a la computadora 2
        event_message = self.message_list[self.event_list["LMC2"].id_message]
        
        if (event_message.last_computer == 0):  # ¿Es un mensaje nuevo?
            # Se asigna a la computadora 2 como la primera computadora del mensaje
            event_message.first_computer = 2
            # Se programa el próximo mensaje nuevo que debe llegar a la computadora 2
            new_message = Message(len(self.message_list))
            new_message_time = self.clock + self.computer_2.input_distribution.calculate()
            self.LMC2_list.append((new_message.id, new_message_time))
            self.message_list.append(new_message)
        else:  # ¿Es un mensaje devuelto desde la computadora 1?
            # Se suma el tiempo de transmisión al tiempo del mensaje en el sistema y en transmisión
            event_message.system_time += 3.0
            event_message.transmission_time += 3.0
            # Se incrementa en 1 la cantidad de veces que fue retornado el mensaje
            event_message.amount_returned += 1
        
        assigned_processor = None
        if (self.computer_2.processors_list[0].busy_status == False and self.computer_2.processors_list[1].busy_status == False):  # ¿Están los dos procesadores libres?
            # Se calcula con probalidad 50/50 a cual procesador se le asigna el mensaje para que lo procese
            random_number = calculate_uniform(0, 99) # Utiliza método propio de generación de aleatorios con distribución uniforme
            if(random_number < 50):
                assigned_processor = self.computer_2.processors_list[0]
            else:
                assigned_processor = self.computer_2.processors_list[1]
        elif (self.computer_2.processors_list[0].busy_status == False):  # ¿Está el procesador 1 libre?
            # Se asigna el procesador 1
            assigned_processor = self.computer_2.processors_list[0]
        elif (self.computer_2.processors_list[1].busy_status == False):  # ¿Está el procesador 2 libre?
            # Se asigna el procesador 2
            assigned_processor = self.computer_2.processors_list[1]
        # ¿Ninguno está libre?
        # Se mantiene: assigned_processor = None
        
        if(assigned_processor != None):  # ¿Existía un procesador libre?
            # Se programa el evento para que el procesador seleccionado procese el mensaje
            event_str = "SMC2P" + str(assigned_processor.id)
            self.event_list[event_str].event_time = self.clock + assigned_processor.output_distribution.calculate()
            self.event_list[event_str].id_message = event_message.id
            # Se cambia el estado del procesador a ocupado
            assigned_processor.busy_status = True
            # Se guarda el momento en el que el mensaje empezó a ser procesado
            event_message.last_registered_clock = self.clock
            # Se guarda el momento en el que el procesador empezó a procesar el mensaje
            assigned_processor.last_registered_clock = self.clock
        else:
            # Se ingresa el mensaje a la cola de la computadora
            self.computer_2.add_queued_message(event_message.id)
            # Se guarda el momento en el que el mensaje empezó a esperar en cola
            event_message.last_registered_clock = self.clock
        
        # Se saca de la lista ordenada de mensajes que deben llegar a la computadora 2 el mensaje que ya se procesó o puso en cola
        self.LMC2_list.remove((event_message.id, self.clock))
        
        # Se busca el próximo mensaje que tiene que llegar a la computadora 2
        next_event_parameters = min(self.LMC2_list, key= lambda x: x[1]) # Devuelve (id_mensaje, tiempo_ocurrencia)
        # Se programa el siguiente Evento LMC2
        self.event_list["LMC2"].id_message = next_event_parameters[0]
        self.event_list["LMC2"].event_time = next_event_parameters[1]

    def do_LMC3_event(self):
        """
        Este es el método que ejecuta el evento llega mensaje a la computadora 3
        """
        # Se actualiza el reloj al tiempo del evento
        self.clock = self.event_list["LMC3"].event_time
        # Se obtiene el mensaje que está llegando a la computadora 3
        event_message = self.message_list[self.event_list["LMC3"].id_message]

        if (event_message.last_computer == 0):  # ¿Es un mensaje nuevo?
            # Se asigna a la computadora 3 como la primera computadora del mensaje
            event_message.first_computer = 3
            # Se programa el próximo mensaje nuevo que debe llegar a la computadora 3
            new_message = Message(len(self.message_list))
            new_message_time = self.clock + self.computer_3.input_distribution.calculate()
            self.LMC3_list.append((new_message.id, new_message_time))
            self.message_list.append(new_message)
        else:  # ¿Es un mensaje devuelto desde la computadora 1?
            # Se suma el tiempo de transmisión al tiempo del mensaje en el sistema y en transmisión
            event_message.system_time += 3.0
            event_message.transmission_time += 3.0
            # Se incrementa en 1 la cantidad de veces que fue retornado el mensaje
            event_message.amount_returned += 1
        
        if (self.computer_3.processors_list[0].busy_status == False):  # ¿Está el procesador libre?
            # Se asigna el procesador
            assigned_processor = self.computer_3.processors_list[0]
            # Se programa el evento para que el procesador seleccionado procese el mensaje
            self.event_list["SMC3"].event_time = self.clock + assigned_processor.output_distribution.calculate()
            self.event_list["SMC3"].id_message = event_message.id
            # Se cambia el estado del procesador a ocupado
            assigned_processor.busy_status = True
            # Se guarda el momento en el que el mensaje empezó a ser procesado
            event_message.last_registered_clock = self.clock
            # Se guarda el momento en el que el procesador empezó a procesar el mensaje
            assigned_processor.last_registered_clock = self.clock
        else:
            # Se ingresa el mensaje a la cola de la computadora
            self.computer_3.add_queued_message(event_message.id)
            # Se guarda el momento en el que el mensaje empezó a esperar en cola
            event_message.last_registered_clock = self.clock
        
        # Se saca de la lista ordenada de mensajes que deben llegar a la computadora 3 el mensaje que ya se procesó o puso en cola
        self.LMC3_list.remove((event_message.id, self.clock))
        
        # Se busca el próximo mensaje que tiene que llegar a la computadora 3
        next_event_parameters = min(self.LMC3_list, key= lambda x: x[1]) # Devuelve (id_mensaje, tiempo_ocurrencia)
        # Se programa el siguiente Evento LMC2
        self.event_list["LMC3"].id_message = next_event_parameters[0]
        self.event_list["LMC3"].event_time = next_event_parameters[1]

        

    def do_SMC1_event(self):
        """
        Este es el método que ejecuta el evento sale mensaje de la computadora 1
        """
        # Se actualiza el reloj al tiempo del evento
        self.clock = self.event_list["SMC1"].event_time
        # Se obtiene el mensaje que debe salir de la computadora 1
        event_message = self.message_list[self.event_list["SMC1"].id_message]
        # Se actualiza el tiempo en el sistema del mensaje
        event_message.update_system_time(self.clock)
        # Se actualiza el tiempo que duró el mensaje procesándose en la computadora 1
        event_message.update_processing_time_1(self.clock)
        # Se actualiza el tiempo que duró procesando el mensaje la computadora 1
        self.computer_1.processors_list[0].update_processing_time(self.clock)
        
        # Se toma un aleatorio de 0 a 99 para calcular la probabilidad X1 y X3 de que se devuelva el mensaje a su respectiva computadora
        random_number = calculate_uniform(0,99)
        if (event_message.last_computer == 2):  # ¿El mensaje viene de la computadora 2? 
            if(random_number < self.x1_probability):  # ¿Se tiene que devolver el mensaje a la computadora 2?
                # Agrega en la Lista Ordenada de mensajes que deben de llegar a la computadora 2 el mensaje a devolver
                next_message_time = self.clock + 3.0
                self.LMC2_list.append((event_message.id, next_message_time))
                # Se busca el próximo mensaje que tiene que llegar a la computadora 2
                next_event_parameters = min(self.LMC2_list, key= lambda x: x[1]) # Devuelve (id_mensaje, tiempo_ocurrencia)
                # Se programa el evento LMC2
                self.event_list["LMC2"].id_message = next_event_parameters[0]
                self.event_list["LMC2"].event_time = next_event_parameters[1]
            else:  # ¿El mensaje debe de enviarse?
                # Se realiza el envío del mensaje
                event_message.send()
        elif (event_message.last_computer == 3):  # ¿El mensaje viene de la computadora 3?
            if (random_number < self.x3_probability):  # ¿Se tiene que devolver el mensaje a la computadora 3?
                # Agrega en la Lista Ordenada de mensajes que deben de llegar a la computadora 3 el mensaje a devolver
                next_message_time = self.clock + 3.0
                self.LMC3_list.append((event_message.id, next_message_time))
                # Se busca el próximo mensaje que tiene que llegar a la computadora 3
                next_event_parameters = min(self.LMC3_list, key= lambda x: x[1]) # Devuelve (id_mensaje, tiempo_ocurrencia)
                # Se programa el evento LMC3
                self.event_list["LMC3"].id_message = next_event_parameters[0]
                self.event_list["LMC3"].event_time = next_event_parameters[1]
            else:  # ¿El mensaje debe de enviarse?
                # Se realiza el envío del mensaje
                event_message.send()
        
        # Se asigna la computadora 1 como la última en la que ha estado el mensaje
        event_message.last_computer = 1
        
        if (len(self.computer_1.queued_messages) == 0):  # ¿La cola de la computadora 1 está vacía?
            # Se Se cambia el estado del procesador a libre y se desprograma el evento SMC1
            self.computer_1.processors_list[0].busy_status = False
            self.event_list["SMC1"].event_time = self.max
        else:  # ¿La cola de la computadora 1 tiene algún mensaje?
            #  Se toma el mensaje a ser procesado
            next_message_to_process_id = self.computer_1.pop_queued_message()
            next_message_to_process = self.message_list[next_message_to_process_id]
            # Se le actualizan los tiempo en cola y en el sistema al mensaje por procesar
            next_message_to_process.update_queue_time(self.clock)
            next_message_to_process.update_system_time(self.clock)
            # Se programa el evento SMC1
            self.event_list["SMC1"].event_time = self.clock + self.computer_1.processors_list[0].output_distribution.calculate()
            self.event_list["SMC1"].id_message = next_message_to_process_id
            # Se guarda el momento en el que el mensaje empezó a ser procesado
            next_message_to_process.last_registered_clock = self.clock
            # Se guarda el momento en el que el procesador empezó a procesar el mensaje
            self.computer_1.processors_list[0].last_registered_clock = self.clock

    def do_SMC2P1_event(self):
        """
        Este es el método que ejecuta el evento sale mensaje del procesador 1 computadora 2
        """    
        # Se actualiza el reloj al tiempo del evento
        self.clock = self.event_list["SMC2P1"].event_time
        # Se obtiene el mensaje que debe salir del procesador 1 de la computadora 2
        event_message = self.message_list[self.event_list["SMC2P1"].id_message]
        # Se actualiza el tiempo en el sistema del mensaje
        event_message.update_system_time(self.clock)
        # Se actualiza el tiempo que duró el mensaje procesándose en el procesador 1 de la computadora 2
        event_message.update_processing_time_2(self.clock)
        # Se actualiza el tiempo que duró procesando el mensaje el procesador 1 de la computadora 2
        self.computer_2.processors_list[0].update_processing_time(self.clock)
        # Se asigna la computadora 2 como la última en la que ha estado el mensaje
        event_message.last_computer = 2
        # Agrega en la Lista Ordenada de mensajes que deben de llegar a la computadora 1 el mensaje a enviar
        next_message_time = self.clock + 20.0
        self.LMC1_list.append((event_message.id, next_message_time))
        # Se busca el próximo mensaje que tiene que llegar a la computadora 1
        next_event_parameters = min(self.LMC1_list, key= lambda x: x[1]) # Devuelve (id_mensaje, tiempo_ocurrencia)
        # Se programa el evento LMC1
        self.event_list["LMC1"].id_message = next_event_parameters[0]
        self.event_list["LMC1"].event_time = next_event_parameters[1]
        
        if (len(self.computer_2.queued_messages) == 0):  # ¿La cola de la computadora 2 está vacía?
            # Se cambia el estado del procesador a libre y se desprograma el evento SMC2P1
            self.computer_2.processors_list[0].busy_status = False
            self.event_list["SMC2P1"].event_time = self.max
        else:  # ¿La cola de la computadora 2 tiene algún mensaje?
            # Se toma el mensaje a ser procesado
            next_message_to_process_id = self.computer_2.pop_queued_message()
            next_message_to_process = self.message_list[next_message_to_process_id]
            # Se le actualizan los tiempo en cola y en el sistema al mensaje por procesar
            next_message_to_process.update_queue_time(self.clock)
            next_message_to_process.update_system_time(self.clock)
            # Se programa el evento SMC2P1
            self.event_list["SMC2P1"].event_time = self.clock + self.computer_2.processors_list[0].output_distribution.calculate()
            self.event_list["SMC2P1"].id_message = next_message_to_process_id
            # Se guarda el momento en el que el mensaje empezó a ser procesado
            next_message_to_process.last_registered_clock = self.clock
            # Se guarda el momento en el que el procesador empezó a procesar el mensaje
            self.computer_2.processors_list[0].last_registered_clock = self.clock

    def do_SMC2P2_event(self):
        """
        Este es el método que ejecuta el evento sale mensaje del procesador 2 computadora 2
        """ 
        # Se actualiza el reloj al tiempo del evento
        self.clock = self.event_list["SMC2P2"].event_time
        # Se obtiene el mensaje que debe salir del procesador 2 de la computadora 2
        event_message = self.message_list[self.event_list["SMC2P2"].id_message]
        # Se actualiza el tiempo en el sistema del mensaje
        event_message.update_system_time(self.clock)
        # Se actualiza el tiempo que duró el mensaje procesándose en el procesador 2 de la computadora 2
        event_message.update_processing_time_2(self.clock)
        # Se actualiza el tiempo que duró procesando el mensaje el procesador 2 de la computadora 2
        self.computer_2.processors_list[1].update_processing_time(self.clock)
        # Se asigna la computadora 2 como la última en la que ha estado el mensaje
        event_message.last_computer = 2
        # Agrega en la Lista Ordenada de mensajes que deben de llegar a la computadora 1 el mensaje a enviar
        next_message_time = self.clock + 20.0
        self.LMC1_list.append((event_message.id, next_message_time))
        # Se busca el próximo mensaje que tiene que llegar a la computadora 1
        next_event_parameters = min(self.LMC1_list, key= lambda x: x[1]) # Devuelve (id_mensaje, tiempo_ocurrencia)
        # Se programa el evento LMC1
        self.event_list["LMC1"].id_message = next_event_parameters[0]
        self.event_list["LMC1"].event_time = next_event_parameters[1]
        
        if (len(self.computer_2.queued_messages) == 0):  # ¿La cola de la computadora 2 está vacía?
            # Se cambia el estado del procesador a libre y se desprograma el evento SMC2P2
            self.computer_2.processors_list[1].busy_status = False
            self.event_list["SMC2P2"].event_time = self.max
        else:  # ¿La cola de la computadora 2 tiene algún mensaje?
            # Se toma el mensaje a ser procesado
            next_message_to_process_id = self.computer_2.pop_queued_message()
            next_message_to_process = self.message_list[next_message_to_process_id]
            # Se le actualizan los tiempo en cola y en el sistema al mensaje por procesar
            next_message_to_process.update_queue_time(self.clock)
            next_message_to_process.update_system_time(self.clock)
            # Se programa el evento SMC2P2
            self.event_list["SMC2P2"].event_time = self.clock + self.computer_2.processors_list[1].output_distribution.calculate()
            self.event_list["SMC2P2"].id_message = next_message_to_process_id
            # Se guarda el momento en el que el mensaje empezó a ser procesado
            next_message_to_process.last_registered_clock = self.clock
            # Se guarda el momento en el que el procesador empezó a procesar el mensaje
            self.computer_2.processors_list[1].last_registered_clock = self.clock
    
    def do_SMC3_event(self):
        """
        Este es el método que ejecuta el evento sale mensaje de la computadora 3
        """
        # Se actualiza el reloj al tiempo del evento
        self.clock = self.event_list["SMC3"].event_time
        # Se obtiene el mensaje que debe salir de la computadora 3
        event_message = self.message_list[self.event_list["SMC3"].id_message]
        # Se actualiza el tiempo en el sistema del mensaje
        event_message.update_system_time(self.clock)
        # Se actualiza el tiempo que duró el mensaje procesándose en la computadora 3
        event_message.update_processing_time_3(self.clock)
        # Se actualiza el tiempo que duró procesando el mensaje el procesador de la computadora 3
        self.computer_3.processors_list[0].update_processing_time(self.clock)
        # Se asigna la computadora 3 como la última en la que ha estado el mensaje
        event_message.last_computer = 3

        # Se toma un aleatorio de 0 a 99 para calcular la probabilidad X2 de que se rechace un mensaje
        random_number = calculate_uniform(0,99)

        if(random_number < self.x2_probability): # ¿Se debe rechazar el mensaje?
            # Se rechaza el mensaje
            event_message.reject()
        else: # Se envía el mensaje a la computadora 1
            # Agrega en la Lista Ordenada de mensajes que deben de llegar a la computadora 1
            next_message_time = self.clock + 20.0
            self.LMC1_list.append((event_message.id, next_message_time))
            # Se busca el próximo mensaje que tiene que llegar a la computadora 1
            next_event_parameters = min(self.LMC1_list, key= lambda x: x[1]) # Devuelve (id_mensaje, tiempo_ocurrencia)
            # Se programa el evento LMC1
            self.event_list["LMC1"].id_message = next_event_parameters[0]
            self.event_list["LMC1"].event_time = next_event_parameters[1]
        
        if (len(self.computer_3.queued_messages) == 0):  # ¿La cola de la computadora 3 está vacía?
            # Se cambia el estado del procesador a libre y se desprograma el evento SMC3
            self.computer_3.processors_list[0].busy_status = False
            self.event_list["SMC3"].event_time = self.max
        else:  # ¿La cola de la computadora 3 tiene algún mensaje?
            # Se toma el mensaje a ser procesado
            next_message_to_process_id = self.computer_3.pop_queued_message()
            next_message_to_process = self.message_list[next_message_to_process_id]
            # Se le actualizan los tiempo en cola y en el sistema al mensaje por procesar
            next_message_to_process.update_queue_time(self.clock)
            next_message_to_process.update_system_time(self.clock)
            # Se programa el evento SMC3
            self.event_list["SMC3"].event_time = self.clock + self.computer_3.processors_list[0].output_distribution.calculate()
            self.event_list["SMC3"].id_message = next_message_to_process_id
            # Se guarda el momento en el que el mensaje empezó a ser procesado
            next_message_to_process.last_registered_clock = self.clock
            # Se guarda el momento en el que el procesador empezó a procesar el mensaje
            self.computer_3.processors_list[0].last_registered_clock = self.clock
            
            