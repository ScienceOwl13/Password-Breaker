import random
import string
import time

customPassword = input("Would you like to chose a password? y/n: ")

if customPassword == "y":
    password = input("Please input a four digit, lowercase password: ")
    startTime = time.time()
else:
    number1 = random.choice(string.ascii_lowercase)
    number2 = random.choice(string.ascii_lowercase)
    number3 = random.choice(string.ascii_lowercase)
    number4 = random.choice(string.ascii_lowercase)
    password = f"{number1}{number2}{number3}{number4}"
    startTime = time.time()

print(f"The password is {password}")

digit1 = "a"
digit2 = "a"
digit3 = "a"
digit4 = "a"
guess = f"{digit1}{digit2}{digit3}{digit4}"

trys= 1

while password != guess:
    digit1 = random.choice(string.ascii_lowercase)
    digit2 = random.choice(string.ascii_lowercase)
    digit3 = random.choice(string.ascii_lowercase)
    digit4 = random.choice(string.ascii_lowercase)
    guess = f"{digit1}{digit2}{digit3}{digit4}"
    print(guess, end="\r")
    trys += 1

endTime = time.time()

totalTime = int(endTime) - int(startTime)

print("\nThe password has been succesfully guessed. It took", trys, "trys and",totalTime, "seconds to guess the password.")
print("That means the computer tested", int(trys/totalTime), "passwords per second!")