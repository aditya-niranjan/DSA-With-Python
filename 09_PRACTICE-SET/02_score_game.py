


import random

def game():
    print("welcome in the game!!")
    print("")

    score = random.randint(1, 100)

    with open("hiscore.txt") as f:
        # fetch hiscore from the file if not then add and check where the file is blank or not
        hiscore = f.read()

        if hiscore != " " and hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score: {score}")

    # write this high score to the file
    if score > hiscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    
    return score

# run the game
game()
