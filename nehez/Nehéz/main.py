

from calculation import Calculation
from printa import Write
felhasznalo_neve = input("Add meg a neved: ")
a = input("Burkolandó felület mérete m2-be: ")
b = input("Csempe m2 területe: ")


if a.isnumeric() and b.isnumeric():
    a = int(a)
    b = int(b)
    fajlbair = Write(felhasznalo_neve, a, b)
    fajlbair.nyomtatos_metodus()

else:
    print("Számot adj meg!")
