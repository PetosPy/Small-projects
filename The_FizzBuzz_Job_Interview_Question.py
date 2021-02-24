# number divisible 3 print: "Fizz"
# number divisible 5 print: "Buzz"
# number divisible 3 and 5 print: "FizzBuzz"

for num in range(1,101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz") 
  else:
    print(num)