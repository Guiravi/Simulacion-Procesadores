from os import system, name 

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
        

class Interface:


    def ask_number_of_runs(self):
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
            b = input("Digite el valor del parámetro b que sea mayor que a (%f): " % a)
            clear()
            try:
                b = float(b)
                if(b <= a):
                    print("Por favor digite un número mayor que a (%f)" % a)
                    b = None
            except ValueError:
                print("Por favor digite un número válido\n")
                b = None
        return (a, b)

    def ask_exponential(self):
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
            b = input("Digite el valor del parámetro b que sea mayor que a (%f): " % a)
            clear()
            try:
                b = float(b)
                if(b <= a):
                    print("Por favor digite un número mayor que a (%f)" % a)
                    b = None
            except ValueError:
                print("Por favor digite un número válido\n")
                b = None

        return (k, a, b)

    def ask_x_probability(self, x_number):
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