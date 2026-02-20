import random
import time

num = random.randint(1,100)


def intro():
    print("may i ask your name")

    global name 
    name = input(" ")
    print(name+ "we will play a game,i will think of a number 1-100 and you have to guess")

    if num% 2 == 0:
        x= "even"
    else:
        x = "odd"
    print(f"the number is {x}")
    time.sleep(0.5)
    print("go ahead take your guess")

def pick():
    guesstaken = 0
    
    while guesstaken < 6:
        
        enter = input("take a guess: ")

        try:
            guess = int(enter)

            if guess <= 100 and guess >= 1:
                guesstaken = guesstaken + 1
                if guesstaken > 6:
                    if guess < num:
                        print("guess is too low")
                    if guess > num:
                        print("guess is too high")
                    if guess != num:
                        time.sleep(0.6)
                        print("try again")
                    if guess == num:
                        break
            if guess>100 or guess < 1:
                print("thats not in range try again")
                time.sleep("enter a number between 1-100")
        except:
            print("thats is not a number")
    if guesstaken==num:
        guesstaken = str(guesstaken)
        print(f"good job {name}, you guessed my number in {guesstaken} guesses")

    if guess != num:
        print("nope the number i was thinking was",str(num))


playagain = "yes"
while playagain == "yes" or playagain == "y" or playagain =="Yes":
    intro()
    pick()
    print("do you want to play again")
    playagain = input()
