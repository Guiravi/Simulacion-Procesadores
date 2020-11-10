import math
import random


class Distribution:

    def __init__(self):
        self._id = "TBD"
        self._miu = 0.0
        self._sigma2 = 0.0
        self._a = 0.0
        self._b = 0.0
        self._lambda = 0.0
        self._k = 0.0

    # --------------- Definición de Métodos Get y Set para atributos de clase Processor --------------- #

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def miu(self):
        return self._miu

    @miu.setter
    def miu(self, value):
        self._miu = value

    @property
    def sigma2(self):
        return self._sigma2

    @sigma2.setter
    def sigma2(self, value):
        self._sigma2 = value

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    @property
    def lambd(self):
        return self._lambda

    @lambd.setter
    def lambd(self, value):
        self._lambda = value

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, value):
        self._k = value
    
    # --------------- FIN Definición de Métodos Get y Set para atributos de clase Processor --------------- #

    def calculate(self):
        """
        Método de clase
        Se envía a calcular la distribución correspondiente y se retorna el valor obtenido 
        """
        result = 0.0
        if (self.id == "Direct"):
            result = self.calculate_direct()
        elif (self.id == "TLC"):
            result = self.calculate_TLC()
        elif (self.id == "Uniform"):
            result = self.calculate_uniform()
        elif (self.id == "Exponential"):
            result = self.calculate_exponential()
        else:
            result = self.calculate_kx()
        return result

    def calculate_direct(self):
        """
        Método de clase
        Se realiza el calculo de distribución normal método directo
        """
        x = -1
        while x < 0:  # Se verifica que el valor de x no sea negativo
            z = (math.sqrt(-2*math.log(random.random()))*math.cos(2*math.pi*random.random()))
            x = self.miu + math.sqrt(self.sigma2)*z
        return x

    def calculate_TLC(self):
        """
        Método de clase
        Se realiza el calculo de distribución normal convolución
        """
        x = -1
        while x < 0:  # Se verifica que el valor de x no sea negativo
            R = 0.0
            for i in range(12):
                R = R + random.random()
            z = R - 6
            x = self.miu + math.sqrt(self.sigma2)*z
        return x

    def calculate_uniform(self):
        """
        Método de clase
        Se realiza el calculo de distribución uniforme
        """
        return self.a + (self.b - self.a)*random.random()


    def calculate_exponential(self):
        """
        Método de clase
        Se realiza el calculo de distribución exponencial
        """
        rand = 0.0
        while rand == 0.0:  # Se verifica que el aleatorio no sea 0
            rand = random.random()
        return ((-1)/(self.lambd))*math.log(rand)


    def calculate_kx(self):
        """
        Método de clase
        Se realiza el calculo de distribución de función de densidad
        """
        x = self.a - 1
        while not (self.a <= x <= self.b):  # Se verifica que x esté en el rango
            x = math.sqrt(((2*random.random())/(self.k)) + self.a**2)
        return x

def calculate_uniform(a, b):
    """
    Método general
    Se realiza el calculo de distribución uniforme para obtener rangos entre [a,b]
    Los parámetros a y b los recibe de otros métodos de la simulación. 
    Este método no se utiliza para la entrada de usuario, para esto existe el Método de Clase
    """
    return a + (b - a)*random.random()
