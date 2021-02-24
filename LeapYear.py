# Leap Year
# Divivsible by 4 is a leap year, by 100 and by 

year = int(input("Which year do you want to check?: "))

if year % 4 == 0 : # Only if year is divisible by 4 (YES) will i check the next condition whic is a century year.
  if year % 100 == 0: #Check Century year(Yes)
    if year % 400 == 0: #Check if divisible by 400(YES)
      print(year, "is Leap year")
    else:
      print(year, "is not leap year")  
  else:
    print(year, "is not leap year")
else: 
  print(year, "Not a leap year")
 