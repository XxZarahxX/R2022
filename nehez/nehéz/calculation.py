class Calculation:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.kerulet = 0
        self.terulet = 0
    
    def kiszamol(self):
        self.kerulet = (self.a + self.b + self.c)
        self.terulet = (self.a*self.b)/2
        