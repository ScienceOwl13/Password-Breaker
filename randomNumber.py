import random

caterpilar = input("Would you like to chose the password? (y/n): ")

if caterpilar == "y":
    password = int(input("Okay, what should it be?: "))
else:
    password = random.randint(0000, 9999999)

print(f"The password is {password}")

input("are you ready kids? EYE EYE CAPTAIN")

guessLow = 0
guessHigh = 9999999
trys = 0

while guessLow != password:
    guessLow += 1
    guessHigh -= 1
    trys += 2

if guessLow == password or guessHigh == password:
    print("Congrats! The computer succesfully guessed the password")
    print(f"It took {trys}")

if guessLow == password:
    print("guessLow guessed the password")
else:
    print("guessHigh guessed the password")