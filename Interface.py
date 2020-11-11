from os import system, name 

def clear():
    """
    Método
    Limpia todo lo que está escrito en la consola
    """
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
        

class Interface:
    """
    Clase Interfaz. Se utiliza para controlar la interfaz de consola y la interacción con el usuario.
    """

    def ask_number_of_runs(self):
        """
        Método para preguntar el número de corridas
        """

        number = 0
        while(number <= 0):
            number = input("Digite el número de veces que se va a correr la simuación: ")
            clear()
            try:
                number = int(number)
                if(number <= 0):
                    clear()
                    print("Por favor digite un número entero positivo mayor que 0\n")
            except ValueError:
                clear()
                print("Por favor digite un número entero válido\n")
                number = 0
        
        return number

    def ask_simulation_time(self):
        """
        Método para preguntar el tiempo de simulación
        """
        number = 0
        while(number <= 0):
            number = input("Digite el tiempo por el que se debe ejecutar la simulación en segundos: ")
            clear()
            try:
                number = int(number)
                if(number <= 0):
                    print("Por favor digite un número entero positivo mayor que 0\n")
            except ValueError:
                print("Por favor digite un número entero válido\n")
                number = 0
        
        return number

    def ask_distribution(self, dist_number):
        """
        Método para preguntar la distribución a utilizar en D1, D2, D3, D4 y D5
        """
        number = 0
        while(number <= 0 or number >= 6):
            print("Seleccione la distribución que desea utilizar para " + dist_number + ": \n" +
                  "1. Distribución normal por método directo\n" +
                  "2. Distribución normal por método de la convolución\n" +
                  "3. Distribución uniforme\n" +
                  "4. Distribución exponencial\n" +
                  "5. Distribución con función de densidad f(x) = kx\n")
            number = input("Digite su opción del 1 al 5: ")
            clear()
            try:
                number = int(number)
                if(number <= 0 or number >= 6):
                    print("Por favor digite una opción válida (1, 2, 3, 4 ó 5)\n")
            except ValueError:
                print("Por favor digite un número entero válido\n")
                number = 0
        
        return number

    def ask_normal(self):
        """
        Método para consultar los parámetros miu y sigma^2 de la distribución normal
        """

        miu = None
        sigma2 = None

        while (miu == None):
            miu = input("Digite el valor del parámetro Miu: ")
            clear()
            try:
                miu = float(miu)
            except ValueError:
                print("Por favor digite un número válido\n")
                miu = None
        while (sigma2 == None):
            sigma2 = input("Digite el valor del parámetro Sigma^2: ")
            clear()
            try:
                sigma2 = float(sigma2)
            except ValueError:
                print("Por favor digite un número válido\n")
                sigma2 = None
        return (miu, sigma2)

    def ask_uniform(self):
        """
        Método para consultar los parámetros a y b de la distribución uniforme
        """

        a = None
        b = None

        while (a == None):
            a = input("Digite el valor del parámetro a: ")
            clear()
            try:
                a = float(a)
            except ValueError:
                print("Por favor digite un número válido\n")
                a = None

        while (b == None):
            b = input("Digite el valor del parámetro b que sea mayor que a (%.4f): " % a)
            clear()
            try:
                b = float(b)
                if(b <= a):
                    print("Por favor digite un número mayor que a (%.4f)" % a)
                    b = None
            except ValueError:
                print("Por favor digite un número válido\n")
                b = None
        return (a, b)

    def ask_exponential(self):
        """
        Método para preguntar el parámetro lambda de la distribución uniforme
        """

        lambd = None

        while (lambd == None):
            lambd = input("Digite el valor del parámetro lambda: ")
            clear()
            try:
                lambd = float(lambd)
            except ValueError:
                print("Por favor digite un número válido\n")
                lambd = None

        return lambd

    def ask_density(self):
        """
        Método para consultar los parámetros k, a y b de la función de densidad f(x) = kx
        """

        k = None
        a = None
        b = None

        while (k == None):
            k = input("Digite el valor del parámetro k: ")
            clear()
            try:
                k = float(k)
            except ValueError:
                print("Por favor digite un número válido\n")
                k = None

        while (a == None):
            a = input("Digite el valor del parámetro a: ")
            clear()
            try:
                a = float(a)
            except ValueError:
                print("Por favor digite un número válido\n")
                a = None

        while (b == None):
            b = input("Digite el valor del parámetro b que sea mayor que a (%.4f): " % a)
            clear()
            try:
                b = float(b)
                if(b <= a):
                    print("Por favor digite un número mayor que a (%.4f)" % a)
                    b = None
            except ValueError:
                print("Por favor digite un número válido\n")
                b = None

        return (k, a, b)

    def ask_x_probability(self, x_number):
        """
        Método para preguntar las probabilidades x1, x2 y x3
        """

        probability = 0.0

        while (probability <= 0.0 or probability >= 100.0):
            probability = input("Digite la probabilidad de X" + str(x_number) + " (valor entre ]0,100[): ")
            clear()
            try:
                probability = float(probability)
                if(probability <= 0.0 or probability >= 100.0):
                    print("Por favor digite un valor en el rango adecuado ]0, 100[\n")
            except ValueError:
                print("Por favor digite un número válido\n")
                probability = 0.0
        return probability

    def print_number_of_run(self, run_number):
        """
        Método para imprimir el número de corrida actual
        """
        print("---------------------Corrida #%i---------------------\n" % (run_number+1))
    
    def print_percentage_processor_busy(self, percentages):
        """
        Método que imprime los porcentajes de tiempo que pasa ocupado cada procesador del sistema
        """
        print("Porcentaje del tiempo que pasa ocupado el procesador de la Computadora 1: %.4f %%\n" % percentages[0])
        print("Porcentaje del tiempo que pasa ocupado el procesador 1 de la Computadora 2: %.4f %%\n" % percentages[1])
        print("Porcentaje del tiempo que pasa ocupado el procesador 2 de la Computadora 2: %.4f %%\n" % percentages[2])
        print("Porcentaje del tiempo que pasa ocupado el procesador de la Computadora 3: %.4f %%\n" % percentages[3])
    
    def print_percentage_processor_busy_rejected(self, percentages):
        """
        Método que imprime los porcentajes de tiempo que pasan ocupados las computadoras en mensajes que se rechazan
        """
        print("Porcentaje del tiempo que pasa ocupado el procesador de la Computadora 1 en mensajes rechazados: %.4f %%\n" % percentages[0])
        print("Porcentaje del tiempo que pasa ocupado el procesador de la Computadora 3 en mensajes rechazados: %.4f %%\n" % percentages[1])
    
    def print_percentage_rejected_messages(self, percentage):
        """
        Método que imprime el porcentaje de mensajes que fue rechazado
        """
        print("Porcentaje de mensajes que fueron rechazados: %.4f %%\n" % percentage)

    def print_mean_system_time(self, mean):
        """
        Método que imprime el tiempo promedio en el sistema de los mensajes
        """
        print("Tiempo promedio en el sistema de los mensajes: %.4f s\n" % mean)

    def print_mean_amount_returned(self, amount):
        """
        Método que imprime la cantidad de veces promedio que fue devuelto un mensaje
        """
        print("Promedio de veces que fue devuelto un mensaje: %.4f \n" % amount)
    
    def print_mean_queue_time(self, mean):
        """
        Método que imprime el tiempo promedio en cola para los mensajes
        """
        print("Tiempo promedio en cola de los mensajes: %.4f s\n" % mean)
    
    def print_mean_transmission_time(self, mean):
        """
        Método que imprime el tiempo promedio en transmisión de los mensajes
        """
        print("Tiempo promedio en transmisión de los mensajes: %.4f s\n" % mean)

    def print_percentage_in_processing_time(self, percentage):
        """
        Método que imprime el porcentaje de tiempo que los mensajes pasan en procesamiento
        """
        print("Porcentaje del tiempo en que los mensajes pasaron en procesamiento: %.4f %%\n" % percentage)
    
    def print_confidence_interval_rejected(self, confidence_interval):
        """
        Método que imprime el intervalo de confianza del tiempo promedio que pasan los mensajes rechazados en el sistema
        """
        print("El intervalo de confianza de tiempo promedio en el sistema para mensajes rechazados es de: [%.4f , %.4f]" % (confidence_interval[0], confidence_interval[1]))

    def print_confidence_interval_sent(self, confidence_interval):
        """
        Método que imprime el intervalo de confianza del tiempo promedio que pasan los mensajes enviados en el sistema
        """
        print("El intervalo de confianza de tiempo promedio en el sistema para mensajes enviados es de: [%.4f , %.4f]" % (confidence_interval[0], confidence_interval[1]))

    def print_confidence_interval_total(self, confidence_interval):
        """
        Método que imprime el intervalo de confianza del tiempo promedio que pasan todos los mensajes en el sistema 
        """
        print("El intervalo de confianza de tiempo promedio en el sistema para todos los mensajes es de: [%.4f , %.4f]" % (confidence_interval[0], confidence_interval[1]))