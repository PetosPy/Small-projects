#Write your code below this line 👇
def paint_calc(height, width, cover):
    result = height * width / cover
    print(f"first: You'll need {result:.0f} cans of paint.")


#Write your code above this line 👆
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width= test_w, cover=coverage)



import math
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = (area/cover)
    print(f"Second: You'll need {math.ceil(num_of_cans)} cans of paint.")


#Write your code above this line 👆
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width= test_w, cover=coverage)