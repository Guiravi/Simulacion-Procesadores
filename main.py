from Computer import Computer
from Message import Message
from Event import Event

# VARIABLES GLOBALES
event_queue = [Event]  # Cola de eventos en la que se ingresa cada uno de los eventos del sistema
clock = 0.0  # Reloj del sistema
computer_1 = Computer
computer_2 = Computer
computer_3 = Computer


# GENERADORES DE DISTRIBUCIONES
def generate_d1():
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

    # Se verifica si el procesador está ocupado
    if computer_1.empty():
        time = generate_d6()  # Se genera el tiempo aleatorio según la distribución D6
        event.message.insert_departure_time(clock + time)  # Se ingresa cuando se terminara de procesar el mensage
        event_new = Event(event.get_message(), clock + time, 1)  # Se crea el evento SMC1
        insert_event(event_new)  # Se inserta el evento en la cola de eventos
    else:
        event.message.insert_arrival_time(clock)
        computer_1.insert_message(event.message)
    return


def SMC1(event):
    return


def initialize():
    global computer_1
    global computer_2
    global computer_3

    computer_1 = Computer(-1)
    computer_2 = Computer(1)
    computer_3 = Computer(4)

    computer_1.add_processor(6)
    computer_2.add_processor(2)
    computer_2.add_processor(3)
    computer_3.add_processor(5)


def test():
    initialize()
    print("Test")


def final_statistics():
    return


def simulation(amount_simulations, time):
    global clock
    global event_queue

    # Ciclo para correr la cantidad de simulaciones indicada
    for i in range(amount_simulations):
        initialize()
        clock = 0.0
        while clock < time:
            # se busca el mínimo
            i = get_min()

            # Se extrae el evento de la cola de eventos
            event = event_queue.pop(i)

            # Se busca la ejecución que corresponde al evento y se ejecuta
            if event.type == 0:
                LMC1(event)
            elif event.type == 1:
                SMC1(event)
            elif event.type == 2:
                print("option 3")
            elif event.type == 3:
                print("option 4")
    return


if __name__ == '__main__':
    test()
