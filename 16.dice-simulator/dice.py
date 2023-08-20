import random

input_1 = input("Do you want to Generate a number (y- Yes , n- No)")

while True:
    if (input_1 == "y"):
        print(random.randint(1,6))
        input_1  = input("Do you want to Generate a number (y- Yes , n- No)")

    elif (input_1=="n"):
        print("Ok bye bye")
        quit()
    else:
        print("invalid input")
        quit()

