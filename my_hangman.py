import os

def hangman():
    print("Welcome to hangman")
    word = input("Player 1 what is your word? ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')  # note 'cls' is for windows

    win = False
    board = ['_'] * len(word)
    stages = [
        "--------       ",
        "|      |       ",
        "|      O       ",
        "|    / | \     ",
        "|     / \      ",
        "|              "]  # 0-5 ; wrong would be 6
    wrong = 0
    # remaining_letters = list(word)  # I don't actually want to remove items from the word
    letters = list(word)  # separates each letter as a element in the list
    wrongly_guessed = []

    #while wrong != len(stages) - 1 and not win:  # -1 would be incorrect
    #while wrong != len(stages) + 1 and not win:  # this would also be in correct, handle loosing outside this loop
    while wrong != len(stages) and not win:
        if wrong == 0:
            print("Hints: " + ", ".join(board))
            guess = input("Player 2 please guess a letter: ").lower()
            if len(guess) > 1:
                guess = input("Please enter a single letter: ")
        else:
            for i in range(wrong):
                print(stages[i])
            print("\nWrongly guessed: " + ", ".join(wrongly_guessed))
            print("Hints: " + ", ".join(board))
            guess = input("Player 2 please guess a letter: ").lower()

        if guess in letters:
            indices_to_change = []
            for i in range(len(letters)):
                if letters[i] == guess:
                    indices_to_change.append(i)
            for index in indices_to_change:
                board[index] = guess
             # board[indices_to_change] = guess
            if "".join(board) == word:
                win = True
                print("\nPlayer 1 looses...")
                print("Player 2 you win, the word was " + word + "!")
        else:
            wrong += 1
            wrongly_guessed.append(guess)

        print("\n" * 2)

    # Below would only execute if player 2 looses
    if win is False:
        print("\n")
        for i in range(wrong):
            print(stages[i])
        print("Player 2 looses...")
        print("Player 1 wins!")

if __name__ == "__main__":
    hangman()