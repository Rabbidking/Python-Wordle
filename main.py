import random

def play_game():
    words = ['apple', 'table', 'chair', 'horse', 'house', 'bunny', 'happy', 'swift', 'lucas', 'storm']
    word = random.choice(words)
    tries = 0

    while True:
        remaining_tries = 5 - tries
        input_word = input("\033[0mEnter your guess ({} tries remaining): ".format(remaining_tries))
        if input_word == word:
            print("You won the game! The word was", word + '\n')
            return True
        if len(input_word) != len(word):
            print("Length of the words does not match. Try again.")
            continue
        found = False
        for i in range(len(word)):
            if input_word[i] == word[i]:
                print("\033[1;32m" + input_word[i], end="")
                found = True
            elif input_word[i] != word[i] and input_word[i] in word:
                print("\033[1;33m" + input_word[i], end="")
                found = True
            else:
                print("\033[1;31m" + input_word[i], end="")
        print('\033[0m\n')
        tries += 1
        if tries >= 5:
            print("You lose the game. The word was", word + '\n')
            return False

while True:
    print("Welcome to the Wordle game!")
    if play_game():
        new_game = ""
        while new_game.lower() not in ["yes", "no"]:
            new_game = input("\033[0mDo you want to play a new game? (yes/no) ")
        if new_game.lower() != "yes":
            break
    else:
        new_game = ""
        while new_game.lower() not in ["yes", "no"]:
            new_game = input("\033[0mDo you want to play again? (yes/no) ")
        if new_game.lower() != "yes":
            break
print("\033[0mThank you for playing the Wordle game. Goodbye!")
