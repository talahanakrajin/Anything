import random

num = 0


randomNumber = random.randint(1, 101)

while num != randomNumber:
    num = int(input("Guess The Number: "))
    if num > randomNumber:
        print("hint : decrease it")
    elif num < randomNumber:
        print("hint : increase it")
    else:
        print("great, you have guessed it ;)")
        break

