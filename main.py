# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Message:
    system_time = 0.0
    processing_time = 0.0
    queue_time = 0.0
    amount_returned = 0.0

    def __init__(self):
        return


class Processor:
    busy_time = 0.0
    busy_time_rejected_message = 0.0
    queue = []
    input_dist = 0
    output_dist = 0

    def __init__(self):
        return


def initialize(name):
    msg = Message()
    pc2 = Processor()
    print(msg.queue_time)
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def simulation(amount_simulations, time):
    # for para correr la cantidad de simulaciones
    for i in range(amount_simulations):
        initialize('PyCharm')
        clock = 0.0
        while clock < time:
            # se busca el mínimo
            print("simulacion " + str(i) + " clock " + str(clock))
            clock = clock + 1.1
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    simulation(2, 10.0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
