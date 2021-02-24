#Pizza order
print("Welcome to Python Pizza Deliveries!")
order = input("Do you want ot order a pizza? Y or N ").upper()

bill = 0
if order == "Y":
  size = input("What size pizza do you want? S,M or L ").upper()
  #extra_cheese = input("Do you want extra cheese? Y or N").upper()

  if size == "S":
    bill += 15
    print("Small pizza is $15")
    add_pepperoni = input("Do you want Pepperoni? Y or N ").upper()
    if add_pepperoni == "Y":
      bill += 2
      extra_cheese = input("Do you want extra cheese? Y or N ").upper()
      if extra_cheese == "Y":
        bill += 1
        print(f"Your bill is ${bill} ")
      else:
        print(f"Your bill is ${bill}")
    else:
      print(f"Your bill is ${bill}")
  
  if size == "M":
    bill +=20
    print("Medium pizza is $20")
    add_pepperoni = input("Do you want Pepperoni? Y or N ").upper()
    if add_pepperoni == "Y":
      bill += 3
      extra_cheese = input("Do you want extra cheese? Y or N ").upper()
      if extra_cheese == "Y":
        bill += 1
        print(f"Your bill is ${bill} ")
      else:
        print(f"Your bill is ${bill}")
    else:
      print(f"Your bill is ${bill}")  

  if size == "L":
    bill +=25
    print("Large pizza is $25")
    add_pepperoni = input("Do you want Pepperoni? Y or N ").upper()
    if add_pepperoni == "Y":
      bill += 3
      extra_cheese = input("Do you want extra cheese? Y or N ").upper()
      if extra_cheese == "Y":
        bill += 1
        print(f"Your bill is ${bill} ")
      else:
        print(f"Your bill is ${bill}")
    else:
      print(f"Your bill is ${bill}")


else:
  print("Thank you for your visit, come back soon!")
