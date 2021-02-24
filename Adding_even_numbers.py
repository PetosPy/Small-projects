# Adding only the even numbers in the range of 1 to 100
# It must include 1 and 100

total_evens = 0

for num in range(2,101):
   if num % 2 == 0:
    total_evens += num
print(total_evens)
