from os import X_OK
from calculation import Calculation
import datetime

class Write:
    def __init__(self,felhasznalo_neve, felület, csempe):
        self.user_name = felhasznalo_neve
        self.a = felület
        self.b = csempe

    def nyomtatos_metodus(self):
        self.szamolas = Calculation(self.a, self.b)
        self.szamolas.kiszamol()
         
        date = datetime.datetime.now().strftime("%Y/%m/%d")
 
        f = open ("sajat_nev.txt", "w")
        f.write ("Számításos lap")
        f.write ("\n")
        f.write (f"Megrendelő neve: {self.user_name}")
        f.write ("\n")
        f.write (f"Burkolamdó felület: {self.a}")
        f.write ("\n")
        f.write (f"Fizetendő összeg: {self.b}")
        f.write ("\n")
        f.write (f"Csempe ára: {self.szamolas.csempe}")
        f.write("\n")
        f.write (f"Kelt: Szeged, {date}")