import string
import random
import time

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
guessCount = 0

# Password Generator
def passwordGen():
    global password
    global passLength
    
    passLength = int(input("How many characters would you like the passcode to be: "))
    
    random.shuffle(characters)

    password = []
    for i in range(passLength):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("The password is:", "".join(password))


# Password Guesser
def passwordGuess():

    global guess

    random.shuffle(characters)
    guess = []
    for i in range(passLength):
        guess.append(random.choice(characters))
    
    random.shuffle(guess)

    print("".join(guess), end="\r")

passwordGen()

guess = str

input("Are you ready to have the computer find your password? ")

startTime = time.time()

while guess != password:
    passwordGuess()
    guessCount += 1

# Calculate the time it takes (s)
endTime = time.time()
totalTime = int(endTime) - int(startTime)

minutes = totalTime / 60

seconds = totalTime % 60

print("The password has been guessed")
print(totalTime, "totalTime")
print(f"Test {int(minutes)} minutes, {int(seconds)} seconds.")
print(guessCount, "guesses. That is", guessCount / totalTime, "guesses per second!")