import random
from hangmanwords import words
from hangmanstages import stages

selected_word = random.choice(words)
length = len(selected_word)
lives = 6
display = []

for a in range(length):
    display += "_"
print(f"Your word : [ {' '.join(display)} ]")
endgame = False
while not endgame:
    user_input = input("Guess a word : ").lower()

    if user_input in display:
        print(f"You have already guessed {user_input},try again! ")

    for position in range(length):
        replaced = selected_word[position]  # assigning variable to the position in word of a letter that user entered
        if replaced == user_input:
            display[position] = replaced  # replacing the letter from dash array by comparing it from selected word
            # position

    if user_input not in selected_word:
        lives -= 1
        print("You guessed a wrong word, You lose a life :(")
        if lives == 0:
            endgame = True
            print("You lose")
    print(f"{' '.join(display)}")

    if '_' not in display:
        endgame = True
        print("You win.")

    print(stages[lives])
print(f"Word is {selected_word}")
