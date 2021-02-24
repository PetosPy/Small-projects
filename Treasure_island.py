print("Welcome to Treasure Island...!") 
print("your mission is to find the treasure!")
name = input("Please enter your name player: \n")

ready = input(f"Are you ready {name}? 'Y' or 'N' \n").lower()
if ready == 'y':
  left_or_right = input("Where do you want to go 'left or right'? \n").lower()
  if left_or_right == 'right':
    swim_or_boat = input("You reached the river, do you want to swim across or wait for the boat? :Type: 'swim' or 'boat' \n").lower()
    if swim_or_boat == "boat":
      print("You have reached the beach and found a shinny gold coin in the sand!")
      coin = input("Do you want to pick it up or ignore it? Type: 'Pick' or 'Drop' \n").lower()
      if coin == "pick":
        box = input("Please choose 'red' or 'blue' \n").lower()
        if box == "red":
          print(f"Congratulations {name} you just won a huge treasure!") 
          print("Thank you for playing! ") 
        else:
          print(f"You nearly made it, try hard next time {name}")
      else:
        print("Wrong choice, you can not continue without money, GAME OVER!")
    else:
      print("You got eaten by a large shark, GAME OVER!")

  else:
    print("you chose the wrong direction and you fell into a hole! GAME OVER!")
else:
  print("Ok, Please come back when you are ready!")  







