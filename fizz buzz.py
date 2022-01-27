So the first thing we are going to need is 100 numbers:

for i in range(100):
    print(i+1)# (i+1) Should print 1 to 100 inclusive (i) by itself would print from 0 to 99. # Perhaps better, you could also write it as range (1,101) and avoid adding the 1, so that's what we will use:for i in range(1,100):
    print(i)

⚠️ You might have noticed that I am not using the words fizz and buzz yet, this is intentional, we want to make things as explicit and clear as possible while we are investigating solutions.

The trick here is to use the modulo operator which according to the documentation :

The % (modulo) operator yields the remainder from the division of the first argument by the second.So 3 % 3 is equal to zero and 4 % 3 is not (it yields 1)

Armed with this knowledge, we can now write a conditional to differentiate between multiples of 3 and multiples of 5 :

for i in range(1, 100):
    if i % 3 == 0:
        print ( str(i) + ' is a multiple of 3')
    elif i % 5 == 0:
        print ( str(i) + ' is a multiple of 5')
    else:
        print ( str(i) )# PARTIAL OUTPUT:8
9 is a multiple of 3
10 is a multiple of 5
11
12 is a multiple of 3
13
14
15 is a multiple of 3

The only thing left to do is to catch the situation where i is multiple of both 3 and 5 :

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print ( str(i) + ' is Multiple of 3 AND 5')
    else:
        print ( str(i) )# PARTIAL OUTPUT:14
15 is Multiple of 3 AND 5
16...
44
45 is Multiple of 3 AND 5
46...

So we seem to have everything we need, the last thing to do is check for all the cases ( 4 if you count them ) and finally replace our explicit readouts with fizz,buzz and fizzbuzz:

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print ( str(i) + ' is Multiple of 3 AND 5')
    elif i % 3 == 0:
        print ( str(i) + ' is a multiple of 3')
    elif i % 5 == 0:
        print ( str(i) + ' is a multiple of 5')
    else:
        print ( str(i) )# PARTIAL OUTPUT:15 is Multiple of 3 AND 5
16
17
18 is a multiple of 3
19
20 is a multiple of 5...Note that you could also try for a modulo of 15 test since this is the earliest number divisible by 3 and 5:if i % 15== 0:

⚠️ Note where the conditional for both cases is placed ( First if ), if you were to place it somewhere else it wouldn’t work because one of the other conditionals would trigger first, that’s also why we are still printing explicit readouts, it is easier to catch mistakes.
    
  
#x#x#x#x#x#x#x#x#x#x#x#x##x#x#x#x#x#x#x#x#x#x##
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz!")
    elif n % 3 == 0:
        print("Fizz!")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
