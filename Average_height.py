# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆
# 180 124 165 173 189 169 146

#Write your code below this row 👇

total = 0  # sum of all the heights.
counter = 0 # counts the number of students

for nums in student_heights:
  total = total + nums
  counter = counter + 1


average = total / counter

print(f"The total of all heights is: {total} cm")
print(f"Number of students is: {counter}")
print(f'The Average height of a student is: {average:.0f} cm')






  
  
