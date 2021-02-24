rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

option = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: \n "))

while option not in range(0,3):
  option = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: \n "))


computer = random.randint(0,2)

game_image = [rock, paper, scissors]

#PLAYER CHOICE
print(game_image[option])

#COMPUTER LOGIC
print("computer chose: ")
print(game_image[computer])

# 0 == ROCK  
# 1 == PAPER
# 2 == SCISSORS

# COMPARE THE CHOSEN OPTIONS
if option == 0 and computer == 2:                   
  print("You Win")                                  
elif option == 2 and computer == 0:
  print("You Lose")
elif option == 1 and computer == 0:  
  print("You win")                                                                     
elif option == 0 and computer == 1:
  print("You Lose")
elif option == 2 and computer == 1:
  print("You win")
elif computer == option:
  print("Its a Draw")
else:
  print("Wrong choice, you lose")











