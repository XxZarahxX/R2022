from calculation import Calculation
from nyomtat import Write
felhasznalo_neve = input("Add meg a neved: ")
a = input("a oldal hossza: ")
b = input("b oldal hossza: ")
c = input("c oldal hossza: ")

if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a_oldal = int(a)
    b_oldal = int(b)
    c_oldal = int(c)
    fajlbair = Write(felhasznalo_neve, a_oldal, b_oldal, c_oldal)
    fajlbair.nyomtatos_metodus()

else:
    print("Számot adj meg!")
