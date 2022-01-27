class Calculation:

    def __init__(self, felület, csempe):
        self.a = felület
        self.b = csempe
        self.kötber = 0
        self.csempe = 0
        self.összeg = 0
    
    def kiszamol(self):
        self.csempe = self.csempe/self.a
        self.összeg = (self.a*self.csempe)
        