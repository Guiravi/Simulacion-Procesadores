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

        self.distribution_list[]        # Contiene D1, D2, D3, D4, D5 y D6
        self.event_list = []            # Contiene la lista de eventos para programar
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

    def get_user_input(self):
        self.number_of_runs = self.interface.ask_number_of_runs()
        self.simulation_time = self.interface.ask_simulation_time()
        self.max = 4 * self.simulation_time

        self.set_simulation_distributions()

    def set_simulation_distributions(self):
        distribution_dictionary = {1: "Direct",
                                   2: "TLC",
                                   3: "Uniform",
                                   4: "Exponential",
                                   5: "Density"}
        for i in range(6):
            dist = Distribution()
            option = self.interface.ask_distribution("D" + (i+1))
            dist.id = distribution_dictionary[option]
            self.set_dist_parameters(dist)

    
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
        else:
            parameters = self.interface.ask_density()