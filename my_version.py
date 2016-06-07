import random


def game():

    # selects word
    word = ["impossible", "coordinate", "disgust", "mediocre", "apology", "civilization", "distinguish",
            "calculate", "horrendous", "dinosaur", "divisible", "anxiety", "millionaire", "vaccination", "possible",
            "keyboard", "coliseum", "decimate", "cleanse", "mansion", "neighborhood", "organization", "pillow",
            "doorknob", "hallway", "basket", "landscape", "symmetry", "office", "sharpen", "number", "basketball",
            "football", "baseball", "tennis", "swimming", "enchilada", "steak", "chicken", "farmer", "merchandise"
            "estate", "communicate", "internet", "application", "pharmacy", "store", "sanctuary", "program", "answer",
            "various", "reason", "lemonade", "strength", "weakness", "english", "spanish", "german", "graduate",
            "college", "badger", "animal", "human", "alien", "closet", "passage", "message",
            "chapter", "number", "letter", "abbreviate", "alphabetical", "elephant", "solve", "shorten", "establish"
            "forrest", "dessert", "summer", "vacation", "destination", "absorb", "assign", "examine", "electricity",
            "professional", "pathetic", "orange", "violet", "multiple", "occasion", "accessory", "backpack", "window",
            "anaesthesia", "doctor", "rainbow", "cactus", "shelter", "crumble", "portrait", "wooden"]
    num = random.randint(0, len(word))
    word = word[num]
    word_list = list(word)
    guess_l = []
    guesses = 0

    u_list = []
    length = len(word)
    u_list.append("_ "*length)
    start_lst = "".join(u_list)
# ______________________________________________________________________________________________________________________

    print(start_lst)

    def replace(lst, location, new_char):
        del(lst[location])
        lst.insert(location, new_char)
        return lst


    for n in range(0, 5):
        guess = input("Guess:")
        guess_l.append(guess)
        guesses += 1
        loc = word_list.index(guess)
        if loc <= 0:
            replace(u_list, loc, guess)

            print("".join(u_list))
        else:
            print(start_lst)
    if guesses == 5:
        final_guess = input("Guess Word:")


game()
