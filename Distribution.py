class Distribution:

    def __init__(self):
        self._id = "TBD"
        self._miu = 0.0
        self._sigma2 = 0.0
        self._a = 0.0
        self._b = 0.0
        self._lambda = 0.0
        self._k = 0.0

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
    def a(self,value):
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