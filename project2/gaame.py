from random import randint
def guess():
    p = 5
    n = randint(0,100)
    ui=eval(input("What is your guess?"))
    while (p-1):
        if ui < n and p > 0:
            print("Choose a higher number")
            p=p-1
        elif ui > n and p > 0:
            print ("Choose a lower number")
            p=p-1
        elif ui == n:
            print ("You guessed right")
            break
        ui=eval(input("What is your guess?"))
    print ("Game over, the number to guess was ", n)

guess()
