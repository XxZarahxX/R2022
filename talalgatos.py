Today we are going to make an interactive guessing game in Python.

This is going to be a simple guessing game where the computer will generate a random number between 1 to 10, and the user has to guess it in 5 attempts.

Based on the user’s guess computer will give various hints if the number is high or low. 
When the user guess matches the number computer will print the answer along with the number of attempts.

This is how the game looks in action,

Hello, What's your name?

Abhijeet

okay! Abhijeet I am Guessing a number between 1 and 10:

2
Your guess is too low
4
Your guess is too low
6
You guessed the number in 3 tries!
In this article, we will guide you through each step of making this interactive guessing game in Python.

Now, open your favorite text editor and start coding.

First, we will create a file a new file named game.py from our text editor.

To generate a random number we will use a Python module named random to use this module in our program, we first need to import it.

 import random
Next, we will use the random module to generate a number between 1 to 10 and store it in a variable named number.
number = random.randint(1, 10)
Now we will prompt the user to enter his name and store it to a variable named player_name.

player_name = input("Hello, What's your name?")
In the next step, we will create a variable named number_of_guesses and assign 0 to it. Later we will increase this value on each iteration of the while loop.

Finally, before constructing the while loop, we will print a string which includes the player name.

 print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')
Now let’s design the while loop.

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
In the first line, we are defining the controlling expression of the while loop. Our game will give user 5 attempts to guess the number, 
hence less than 5 because we have already assigned the number_of_guesses variable to 0.

Within the loop, we are taking the input from the user and storing it in the guess variable. However, 
the user input we are getting from the user is a string object and to perform mathematical operations on it we first need to convert 
it to an integer which can be done by the Python’s inbuilt int() method.

In the next line, we are incrementing the value of number_of_guesses variable by 1.

Below it, we have 3 conditional statements.

In the first, if statement we are comparing if the guess is less than the generated number if this statement evaluates to true, we print the corresponding Guess.
Similarly, we are checking if the guess is greater than the generated number.
The final if statement has the break keyword, which will terminate the loop entirely, So when the guess is equal to the generated number loop gets terminated.
Below the while loop, we need to add another pair of condition statements,

#x#x#x#x#x#x#x#x#x#x#x#x##x#x#x#x#x#x#x#x#x#x###x#x#x#x#x#x#x#x#x#x#x#x##x#x#x#x#x#x#x#x#x#x##
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
