from Processor import Processor
from Message import Message
from Event import Event

# VARIABLES GLOBALES


event_queue = [Event]  # Cola de eventos en la que se ingresa cada uno de los eventos del sistema
clock = 0.0  # Reloj del sistema
processor_1 = Processor()
processor_2_1 = Processor()
processor_2_2 = Processor()
processor_3 = Processor()


# GENERADORES DE DISTRIBUCIONES


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

    clock = event.get_arrival_time()

    # Se verifica si el procesador está ocupado
    if processor_1.busy:
        event.message.insert_arrival_time(clock)
        processor_1.insert_message(event.message)
    else:
        time = generate_d6()  # Se genera el tiempo aleatorio según la distribución D6
        event.message.insert_departure_time(clock + time)  # Se ingresa el tiempo en que termina de procesarse el mensage
        event_new = Event(event.get_message(), clock + time, 1)  # Se crea el evento SMC1
        insert_event(event_new)  # Se inserta el evento en la cola de eventos
    return


def SMC1(event):
    return


def initialize():
    processor_1 = Processor()


def test():
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
