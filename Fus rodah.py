def fus_rodah():
    for x in range(1, 350):
        if x % 2 == 0 and x % 11 == 0:
            print("Fus Rodah!")
        elif x % 2 == 0:
            print("Fus!")
        elif x % 11 == 0:
            print("Rodah!")
        else:
            print(x)
fus_rodah()
    