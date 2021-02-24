
import random
from replit import clear
from Hangman import hangman_words 
from Hangman import hangman_art


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6



print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()

    if guess in display:
        print(f"The letter {guess} has already been guessed")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:

       

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
        else:
            print(f"You guessed {guess}, that's not in the word, you lose a life")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])