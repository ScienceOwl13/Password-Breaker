# Import libraries
import string
import random
import time

# List of characters that can be in the password
characters = list(string.ascii_letters + string.digits + string.punctuation)

# Password Generator
def passwordGen():
    global password
    global passLength
    
    passLength = int(input("How many characters would you like the passcode to be: "))
    
    # Rearrange the letters from the possible character list
    random.shuffle(characters)

    # Create the password at the correct length
    password = []
    for i in range(passLength):
        password.append(random.choice(characters))

    # Rearrange the combination of letters from the password
    random.shuffle(password)

    print("The password is:", "".join(password))


# Password Guesser
def passwordGuess():

    global guess

    # Rearrange the list of characters
    random.shuffle(characters)

    # Create the guess at the correct length
    guess = []
    for i in range(passLength):
        guess.append(random.choice(characters))
    
    #Rearrange the list of shuffled characters
    random.shuffle(guess)

    print("".join(guess), end="\r")

passwordGen()

#This needs to be here for some reason, doesn't work otherwise
guess = str

#If you respond with "caterpillar", it will add an extra three seconds to the timer
wait = input("Are you ready to have the computer find your password? ")

# Mark the time that the guessing starts at
startTime = time.time()

# Keeps track of the amount of guesses
guessCount = 0

# Keep making a new guess until it is equal to the password
while guess != password:
    passwordGuess()
    guessCount += 1

# Setting for testing the decimal places
if wait == "caterpillar":
    time.sleep(3)

# Mark the time that the guessing ends at
endTime = time.time()

# Subtract the time that the guessing ends at from the time it starts at
totalTime = endTime - startTime
# Puts the formatted time into a two decimal places
formattedTotalTime = "{:.2f}".format(totalTime)
print(formattedTotalTime)

# Gets the minutes out of the total seconds
minutes = totalTime / 60
# Gets the extra seconds from the minutes
seconds = totalTime % 60

print("The password has been guessed")
print(formattedTotalTime, "totalTime")
print(f"Test {int(minutes)} minutes, {int(seconds)} seconds.")\

# Fixes issue when it is instant, the script would fail as the seconds would be 0, and division by 0 is inpossible
if formattedTotalTime == 0:
    print("It only took the computer", guessCount, "guesses in", totalTime, "seconds to guess the passcode! That's crazy! Just imagine if that is a four digit passcode!")
else:
    #Formats the guess per second to two decimal places to be consistant with other numbers
    print(guessCount, "guesses. That is", "{:.2f}".format(guessCount / totalTime), "guesses per second!")



    