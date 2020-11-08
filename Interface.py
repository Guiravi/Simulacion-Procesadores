class Interface:
    def __init__(self):
        pass

    def ask_number_of_runs(self):
        number = 0
        while(number < 0):
            number = input("Digite el número de veces que se va a correr la simuación: ")

            try:
                number = int(number)
                if(number < 0):
                    print("Por favor digite un número entero positivo\n")
            except ValueError:
                print("Por favor digite un número entero válido\n")
                number = 0

        return number

    def ask_simulation_time(self):
        number = 0
        while(number < 0):
            number = input("Digite el tiempo por el que se debe ejecutar la simulación en segundos: ")

            try:
                number = int(number)
                if(number < 0):
                    print("Por favor digite un número entero positivo\n")
            except ValueError:
                print("Por favor digite un número entero válido\n")
                number = 0

        return number

    def ask_distribution(self, dist_number):
        number = 0
        while(number < 0 or number > 6):
            print("Seleccione la distribución que desea utilizar para " + dist_number + ": \n" +
                  "1. Distribución normal por método directo\n" +
                  "2. Distribución normal por método de la convolución\n" +
                  "3. Distribución uniforme\n" +
                  "4. Distribución exponencial\n" +
                  "5. Distribución con función de densidad f(x) = kx\n")
            number = input("Digite su opción del 1 al 5: ")

            try:
                number = int(number)
                if(number < 0 or number > 6):
                    print("Por favor digite una opción válida (1, 2, 3, 4 ó 5)\n")
            except ValueError:
                print("Por favor digite un número entero válido\n")
                number = 0

        return number

    def ask_direct_method(self):
        return
    
    def ask_tlc_method(self):
        return
    
    def ask_uniform(self):
        return
    
    def ask_exponential(self):
        return
    
    def ask_density(self):
        return

    def ask_x_probability(self, x_number):
        return
