from printing import Printing

netto_input =input("Add meg a nettó béred: ")

if netto_input.isnumeric():
    netto = float(netto_input)
    fajlbair = Printing(netto)
    fajlbair.nyomtatas()
else:
    print("Számot adj meg!")