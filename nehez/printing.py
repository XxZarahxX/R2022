from calculation import Calculation
import datetime

class Printing:
    def __init__(self, ber):
        self.netto = ber
    
    def nyomtatas(self):
        self.szamitas = Calculation(self.netto)
        self.szamitas.szamolas()

        date = datetime.datetime.now().strftime("%Y/%m/%d")

        f = open("viczjan_pal2.txt","w")
        f.write("Bérköltség lap")
        f.write("\n")
        f.write(f"Nettó bér: {self.netto} Ft")
        f.write("\n")
        f.write(f"Diák bérköltség: {self.szamitas.diak} Ft")
        f.write("\n")
        f.write(f"Rendes munkaviszony bérköltség: {self.szamitas.rendes_mv} Ft")
        f.write("\n")
        f.write(date)