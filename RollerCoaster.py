#Roller coaster ride.
print("Welcome to the Rollercoaster")
height = int(input("Please enter your height in centimetres: "))

bill = 0

if height >= 120:
  age = int(input("Please enter your age: "))

  if age < 12:
    bill = 12
    print("Child Ticket $5.00")
  elif age < 18:
    bill = 7
    print("Youth Ticket $7.00")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok, have a free ride on us!")
  elif age > 18:
    bill = 12
    print("Adult Ticket $12.00")

  wants_photo = input("Do you want a photo taken? Y or N. ").upper()

  if wants_photo == "Y":
    #Add 3 dollars to the ticket
    bill += 3

  print(f"Your Ticket total is ${bill}.00")


else:
  print("You need to grow a bit more!")
  