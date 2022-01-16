import random

in_game = True
tippek = 11
random_num = random.randint(1,40)

def guessing_game(input_szam):
    global in_game
    global tippek

    if input_szam == random_num:
        print("Nyerő")
        in_game = False
    elif input_szam > random_num:
        print("A random szám kevesebb")
        tippek -=1
    elif input_szam < random_num:
        print("A random szám nagyobb")
        tippek -=1

while in_game:
    if tippek > 0:
        input_num = input("Találd ki a számot(1-40):")
        if input_num.isnumeric():
            input_to_num = int(input_num)
            if input_to_num > 0 and input_to_num < 41:
                guessing_game(input_to_num)
            else:
                print("Nincs tartományban a bekért szám!")
                tippek -=1
        else:
            print("Számot adj meg!")
            tippek -= 1
    else:
        print(f"Lúzer, a helyes szám {random_num}")
        in_game = False