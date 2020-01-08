from random import randint

#creates a list of dice
dice = ["d4", "d6", "d8", "d10", "d12", "d20", "d100", "recall"]

roll_history = []

player = False

print("I'm the Dice Goblin, would you like to roll some dice?")

while player == False:
    player = input("I roll a ")
    if player == "d4":
        result = randint(1, 4)
        roll_history.append(result)
        print(result)
    elif player == "d6":
        result = randint(1, 6)
        roll_history.append(result)
        print(result)
    elif player == "d8":
        result = randint(1, 8)
        roll_history.append(result)
        print(result)
    elif player == "d10":
        result = randint(1, 10)
        roll_history.append(result)
        print(result)
    elif player == "d12":
        result = randint(1, 12)
        roll_history.append(result)
        print(result)
    elif player == "d20":
        result = randint(1, 20)
        roll_history.append(result)
        if result == 20:
            print("That's a natural 20!")
        elif result == 1:
            print("Ouch... Natural 1...")
        else:
            print(result)
    elif player == "d100":
        result = randint(1, 100)
        roll_history.append(result)
        if result == 69:
            print("69")
            print("Hehe, nice!")
        else:
            print(result)
    elif player == "recall":
        print(f"Your last five rolls were {roll_history[-5:]}")
    else:
        print("I don't have that die yet... But soon!")
    print("Another?")

    player = False