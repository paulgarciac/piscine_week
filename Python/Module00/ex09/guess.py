import random

#phrase = sys.argv[1]
phrase = "A, robot?. must protect its own existence as long as such protection does not conflict with the First or Second Law"
#obot must protect its own existence as long as such protection does not conflict with the First or Second Law"

print('This is an interactive guessing game!')
print('You have to enter a number between 1 and 50 to find out the secret number.')
print("Type 'exit' to end the game.")
print('Good luck!' + f"\n")

randomInteger = random.randrange(50) + 1
i = 0

def guessing(a):
    
    guess = input("What's your guess between 1 and 50?\n")
    a = a + 1

    try:
        float(guess) == randomInteger
    except:
        print("Only numbers please")
        guessing(a)
    if float(guess) == randomInteger:
        print("Congratulations, you've got it!")
        print("You won in {} attempts !".format(a))
        exit()
    if float(guess) > randomInteger:
        print("Too high ! Try again !")
        guessing(a)
    if float(guess) < randomInteger:
        print("Too low ! Try again !")
        guessing(a)

    

guessing(i)