def hangman(word):
    print("Welcome to hangman")

    win = False
    board = ['_'] * len(word)
    stages = [
        "--------       ",
        "|      |       ",
        "|      O       ",
        "|    / | \     ",
        "|     / \      ",
        "|              "]
    wrong = 0
    rletters = list(word)  # I don't actually want to remove items from the word

    while wrong < len(stages) - 1:
        """
        You have to subtract 1 from the length of stages to compensate for the fact that the stages list starts
        counting from 0, and wrong starts counting at 1 
        """
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)  # note: .index() locates the first occurrence
            board[cind] = char
            rletters[cind] = '$'  # this needed since .index() locates the first occurrence and word might have multiple occurances of the char
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0: e]))  # note: end index is exclusive not inclusive
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if win is False:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}".format(word))


if __name__ == "__main__":
    hangman("cat")