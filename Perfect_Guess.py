from random import randint
n = randint(1,100)

print('''Rules of the game :- 
Try to match the number picked by the computer between 1 to 100
Guess the first number and follow computer instruction to keep on guessing
if you end up at the correct number, number of guesses will be calculated ''')

print("Computer has picked up the number now it's your turn")
i = int(input("To continue pick 1 else 0 : "))
if(i == 1):
    a = -1
    guess = 0
    while(a != n):
        guess += 1
        a = int(input("Guess any number between 1 to 100 : "))

        if(a > n):
            print("Lower number please")
        elif(a < n):
            print("Higher number please")
        else:
            break

    print(f"You have guessed the number {n} correctly in {guess} attempts")
else:
    print("Game terminated")