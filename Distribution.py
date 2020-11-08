class Distribution:

    def __init__(self):
        self._id = "TBD"
        self._mu = 0.0
        self._sigma2 = 0.0
        self._z = 0.0
        self._a = 0.0
        self._b = 0.0
        self._lambda = 0.0
        self._k = 0.0

    @property
    def id(self):
        return self._id

    def calculate(self):
        if (self.id == "Direct"):
            self.calculate_direct()
        elif (self.id == "TLC"):
            self.calculate_TLC()
        elif (self.id == "Uniform"):
            self.calculate_uniform()
        elif (self.id == "Exponential"):
            self.calculate_exponential()
        else:
            self.calculate_kx()

    def calculate_direct(self):
        return

    def calculate_TLC(self):
        return

    def calculate_uniform(self):
        return

    def calculate_exponential(self):
        return

    def calculate_kx(self):
        return