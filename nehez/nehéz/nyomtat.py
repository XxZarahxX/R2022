from os import X_OK
from calculation import Calculation
import datetime

class Write:
    def __init__(self,felhasznalo_neve,a_oldal, b_oldal, c_oldal):
        self.user_name = felhasznalo_neve
        self.a = a_oldal
        self.b = b_oldal
        self.c = c_oldal

    def nyomtatos_metodus(self):
        self.szamolas = Calculation(self.a, self.b, self.c)
        self.szamolas.kiszamol()
         
        date = datetime.datetime.now().strftime("%Y/%m/%d")
 
        f = open ("sajat_nev.txt", "w")
        f.write ("Számításos lap")
        f.write ("\n")
        f.write (f"Felhasználó neve: {self.user_name}")
        f.write ("\n")
        f.write (f"a oldal hossza: {self.a}")
        f.write ("\n")
        f.write (f"b oldal hossza: {self.b}")
        f.write ("\n")
        f.write (f"c oldal hossza: {self.c}")
        f.write ("\n")
        f.write (f"Kerület: {self.szamolas.kerulet}")
        f.write("\n")
        f.write (f"Terület: {self.szamolas.terulet}")
        f.write("\n")
        f.write (f"Kelt: Szeged, {date}")