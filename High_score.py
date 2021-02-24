# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# 52 63 84 52 91 55 68

largest_num = 0
for num in student_scores:
  if num > largest_num:
    largest_num = num
  
  
print(f"The highest score in the class is: {largest_num}")
