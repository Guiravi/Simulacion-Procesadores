from Computer import Computer
from Distribution import Distribution
from Event import Event
from Interface import Interface
from Message import Message
from Processor import Processor


class Simulation:
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
        self.all_runs_results = []      # Lista con las estadisticas finales de cada corrida. Se usa para calcular el promedio de todas las corridas

        self.interface = Interface()    # Instancia para utilizar la interfaz de consola
        self.computer_1 = None
        self.computer_2 = None
        self.computer_3 = None

    def run(self):
        self.get_user_input()
        self.createEvents()
        self.createComputers()

        for i in range(self.number_of_runs):
            print("Ejecutando corrida " + str(i) + "\n")
            self.message_list.append(Message(0))
            self.message_list.append(Message(1))
            self.event_list["LMC2"].id_message = 0
            self.event_list["LMC3"].id_message = 1

            self.do_events()

            # Calcular estadisticas
            # Reset
        # Calcular estadisticas de todas las corridas

    def get_user_input(self):
        self.number_of_runs = self.interface.ask_number_of_runs()
        self.simulation_time = self.interface.ask_simulation_time()
        self.max = 4 * self.simulation_time  # Actualiza el valor de max

        self.set_simulation_distributions()

        self.x1_probability = self.interface.ask_x_probability(1)
        self.x2_probability = self.interface.ask_x_probability(2)
        self.x3_probability = self.interface.ask_x_probability(3)

    def set_simulation_distributions(self):
        distribution_dictionary = {1: "Direct",
                                   2: "TLC",
                                   3: "Uniform",
                                   4: "Exponential",
                                   5: "Density"}
        for i in range(6):
            dist = Distribution()
            option = self.interface.ask_distribution("D" + str(i+1))
            dist.id = distribution_dictionary[option]
            self.set_dist_parameters(dist)
            self.distribution_list["D"+str(i+1)] = dist

    def set_dist_parameters(self, dist):
        if (dist.id == "Direct"):
            parameters = self.interface.ask_normal()
            dist.miu = parameters[0]
            dist.sigma2 = parameters[1]
        elif (dist.id == "TLC"):
            parameters = self.interface.ask_normal()
            dist.miu = parameters[0]
            dist.sigma2 = parameters[1]
        elif (dist.id == "Uniform"):
            parameters = self.interface.ask_uniform()
            dist.a = parameters[0]
            dist.b = parameters[1]
        elif (dist.id == "Exponential"):
            parameters = self.interface.ask_exponential()
            dist.lambd = parameters
        else:
            parameters = self.interface.ask_density()
            dist.k = parameters[0]
            dist.a = parameters[1]
            dist.b = parameters[2]

    def createEvents(self):
        self.event_list["LMC1"] = (Event("LMC1", self.max))
        self.event_list["LMC2"] = (Event("LMC2", 0))
        self.event_list["LMC3"] = (Event("LMC3", 0))
        self.event_list["SMC1"] = (Event("SMC1", self.max))
        self.event_list["SMC2P1"] = (Event("SMC2P1", self.max))
        self.event_list["SMC2P2"] = (Event("SMC2P2", self.max))
        self.event_list["SMC3"] = (Event("SMC3", self.max))

    def createComputers(self):
        self.computer_1 = Computer(1, None)
        self.computer_1.add_processor(0, self.distribution_list["D6"])
        self.processor_list.append(self.computer_1.processors_list[0])

        self.computer_2 = Computer(2, self.distribution_list["D1"])
        self.computer_2.add_processor(1, self.distribution_list["D2"])
        self.computer_2.add_processor(2, self.distribution_list["D3"])
        self.processor_list.append(self.computer_2.processors_list[0])
        self.processor_list.append(self.computer_2.processors_list[1])

        self.computer_3 = Computer(3, self.distribution_list["D4"])
        self.computer_3.add_processor(3, self.distribution_list["D5"])
        self.processor_list.append(self.computer_3.processors_list[0])

    def do_events(self):
        run_finished = False
        while(run_finished == False):
            min_ocurrence_event = min(self.event_list, key=lambda x: self.event_list[x].event_time)

            if (min_ocurrence_event == "LMC1"):
                self.do_LMC1_event()
            elif(min_ocurrence_event == "LMC2"):
                self.do_LMC2_event()
            elif(min_ocurrence_event == "LMC3"):
                self.do_LMC3_event()
            elif(min_ocurrence_event == "SMC1"):
                self.do_SMC1_event()
            elif(min_ocurrence_event == "SMC2P1"):
                self.do_SMC2P1_event()
            elif(min_ocurrence_event == "SMC2P2"):
                self.do_SMC2P2_event()
            elif(min_ocurrence_event == "SMC3"):
                self.do_SMC3_event()

            if (self.clock >= self.simulation_time):
                run_finished = True
        
        # Aumentar tiempos de procesamiento de procesadores faltantes ocupados

    def do_LMC1_event(self):
        self.clock = self.event_list["LMC1"].event_time
        print("Haciendo evento LMC1")

    def do_LMC2_event(self):
        print("Haciendo evento LMC2")
        self.clock = self.event_list["LMC2"].event_time
        self.event_list["LMC2"].event_time = self.max

    def do_LMC3_event(self):
        print("Haciendo evento LMC3")
        self.clock = self.event_list["LMC3"].event_time
        self.event_list["LMC3"].event_time = self.max

    def do_SMC1_event(self):
        print("Haciendo evento SMC1")

    def do_SMC2P1_event(self):
        print("Haciendo evento SMC2P12")

    def do_SMC2P2_event(self):
        print("Haciendo evento SMC2P12")

    def do_SMC3_event(self):
        print("Haciendo evento SMC3")
