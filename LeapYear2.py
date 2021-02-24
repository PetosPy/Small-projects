# How to calculate leap year Version 2
year = int(input("Please enter year to check: "))

if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
  print("This is a leap year")
else:
  print("This is not a leap year")