from Computer import Computer
from Event import Event

# VARIABLES GLOBALES
distribution_list = []
event_queue = [Event]  # Cola de eventos en la que se ingresa cada uno de los eventos del sistema
clock = 0.0  # Reloj del sistema
computer_1 = Computer
computer_2 = Computer
computer_3 = Computer

distri = { 1 : "Normal método directo",
           2 : "Normal método de la convolución",
           3 : "Uniforme",
           4 : "Exponencial",
           5 : "Función de Densidad f(x) = kx"}

# GENERADORES DE DISTRIBUCIONES
def generate_time(distribution):
    i = distribution - 1
    result = 0.0
    if distribution_list[i] == 0:
        print("Normal directo")
        result = normal_direct()
    elif distribution_list[i] == 1:
        print("Normal convolución")
        result = generate_d2()
    elif distribution_list[i] == 2:
        print("uniforme")
        result = generate_d3()
    elif distribution_list[i] == 3:
        print("exponencial")
        result = generate_d4()
    elif distribution_list[i] == 4:
        print("densidad")
        result = generate_d5()
    return result


def normal_direct():
    return 0


def generate_d2():
    return 0


def generate_d3():
    return 0


def generate_d4():
    return 0


def generate_d5():
    return 0


def generate_d6():
    return 0


# GESTIÓN DE LA COLA DE EVENTOS
def insert_event(event):
    event_queue.append(event)


def get_min():
    global event_queue
    event = event_queue[0]
    result = -1
    for i in range(len(event_queue)):
        if event.get_arrival_time() > event_queue[i].get_arrival_time():
            event = event_queue[i]
            result = i
    return result


# IMPLEMENTACIÓN DE LOS EVENTOS
def LMC1(event):
    global clock
    global event_queue

    # Se realiza el salto del reloj al inicio del evento
    clock = event.get_arrival_time()

    # Se verifica si el procesador está vacío
    if computer_1.get_processor(0).empty():
        # Se genera el tiempo aleatorio según la distribución D6
        time = generate_time(computer_1.get_processor(0).get_output_distribution())
        event.message.insert_departure_time(clock + time)  # Se ingresa cuando se terminara de procesar el mensage
        event_new = Event(event.get_message(), clock + time, 1)  # Se crea el evento SMC1
        insert_event(event_new)  # Se inserta el evento en la cola de eventos
    else:
        event.message.insert_arrival_time(clock)
        computer_1.insert_message(event.message)
    return


def SMC1(event):
    return


#MÉTODOS DE SIMULACIÓN
def initialize(d1, d2, d3, d4, d5, d6):
    global computer_1
    global computer_2
    global computer_3

    # Se añaden las computadoras con cada una de sus respectivas distribuciones
    computer_1 = Computer(0)
    computer_2 = Computer(1)
    computer_3 = Computer(4)

    # Se añaden los procesadores con cada una de sus respectivas distribuciones
    computer_1.add_processor(6)
    computer_2.add_processor(2)
    computer_2.add_processor(3)
    computer_3.add_processor(5)


def check_simulation():
    print("hola")


def final_statistics():
    return


def simulation(amount_simulations, time, d1, d2, d3, d4, d5, d6):
    global clock
    global event_queue

    # Ciclo para correr la cantidad de simulaciones indicada
    for i in range(amount_simulations):
        initialize(d1, d2, d3, d4, d5, d6)
        clock = 0.0
        while clock < time:
            # se busca el mínimo
            index = get_min()

            # Se extrae el evento de la cola de eventos
            event = event_queue.pop(index)

            # Se busca la ejecución que corresponde al evento y se ejecuta
            if event.type == 0:
                LMC1(event)     # Se ejecuta el evento LMC1
            elif event.type == 1:
                SMC1(event)     # Se ejecuta el evento SMC1
            elif event.type == 2:
                print("option 3")
            elif event.type == 3:
                print("option 4")
    return


def create_distributions(i):
    d1 = int(input("Ingrese la distribución D%s: " % (i)))
    while not (0 < d1 < 6):
        d1 = int(input("\t Ingrese un número de distribución válida por favor: "))
    print("\t Usted eligió: %s para la distribución d%s" % (distri[d1], i))


if __name__ == '__main__':
    # Se guarda el valor de cada una de las distribuciones
    for i in range(1,7):
        create_distributions(i)
    check_simulation()
