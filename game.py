import random
num=random.randint(1,15)
attept=0
guess=int(input("Can you guess the number I am thinking? its less than 15:"))
while num!=guess:
    if guess>=num:
        print("you guess in higher number")
    else:
        print("Your guess in lower number")
        guess=int(input("Guess again:"))
        print("You Won")
