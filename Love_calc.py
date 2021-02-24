print("Welcome to the Love Calculator")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

name = name1 + name2

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

true = t + r + u + e
love = l + o + v + e

love_score = int(str(true) + str(love))
#int_score = int(love_score)

# Give the user an interpretation
if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}%, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}%, you are alright together")
else:
  print(f"Your score is {love_score}%")