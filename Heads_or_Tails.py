import random
#print("Welcome to the game of Heads and Tails!")

#user = int(input("Please choose between Heads and Tails: 0--> Heads and 1--> Tails: "))

random_side = random.randint(0,1)

if random_side == 0:
  print("Heads")
else:
  print("Tails")

