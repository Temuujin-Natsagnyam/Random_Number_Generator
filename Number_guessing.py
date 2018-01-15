import random
failedguesses = 0

print ("    Hallo, Wie lautet dein Name?    ")
player = input()

print ("Ich habe Spiel für dich, "+ player +", raten Sie die Zahl, die ich zwischen 1 und 20 denke.")

number = random.randint(1,20)

while failedguesses < 5:
    print("Rate mal")
    guess = input()
    guess = int(guess)

    if guess < number :
        print("etwas höher, du kannst es schaffen! ")

    if guess > number :
        print("etwas niedriger, du kannst es schaffen! ")

    if guess == number :
        break
    failedguesses = failedguesses + 1

    if failedguesses == 4:
        break

if failedguesses >= 4 :
    failedguesses = str(failedguesses)
    number = str(number)
    print("Genug! Sie hatten "+failedguesses+" Versuche, die nummer ist "+number+".")

if guess == number :
    guess = str(number)
    failedguesses = str(failedguesses)
    print("JA! Das ist gut, die nummer ist "+guess+", nur "+failedguesses+" Verusches ")