from random import randint
import art_guess_game

def easy_level():
    counter = 10
    game_not_end = True
    while game_not_end:
        print(f"You have {counter} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        counter += -1
        if counter == 0:
            game_not_end = False
            print("Game over")
            print("You ran out of attempts")
            print(f"The chosen number was {selected_number}")
            break 
        if guess > selected_number:
            print("Too high")
            print("Try again: ")
        elif guess < selected_number:
            print("Too low")
            print("Try again: ") 
        else:
            print(f"You got it! The answer was {selected_number}.")
            game_not_end = False

def hard_level():
    counter = 5
    game_not_end = True
    while game_not_end:
        print(f"You have {counter} attempts remaining to guess the number.")  
        guess = int(input("Make a guess: "))
        counter += -1
        if counter == 0:
            game_not_end = False
            print("Game over")
            print("You ran out of attempts")
            print(f"The chosen number was {selected_number}")
            break
        
        elif guess > selected_number:
            print("Too high")
            print("Guess again: ")
        elif guess < selected_number:
            print("Too low")
            print("Try again: ")
        else:
            print(f"You got it! The answer was {selected_number}.")
            game_not_end = False

selected_number = randint(0,101)
print(art_guess_game.logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
print(f"Pssst... the correct answer is {selected_number}")

level = input("choose the difficulty, 'easy' or 'hard': ")
if level == "easy":
    easy_level()
elif level == "hard":
    hard_level()








