from Higher_lower_game import art
from Higher_lower_game import game_data
import random
from replit import clear

def get_random_account():
    """This func gets random data from my game_data list"""
    return random.choice(game_data.data)
data1 = get_random_account


def format_data(account):
   name = account["name"]
   description = account["description"]
   country = account["country"]
   return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """check followers against the users guess and returns True  if they got it right. Or False if they got it wrong"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(art.logo)
    score = 0
    game_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()
    
        print(f"Compare A: {format_data(account_a)}.")
        print(art.vs)
        print(f"Against B: {format_data(account_b)}.")


        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(art.logo)
        if is_correct:
            score += 1   
            print(f"You're right! Current score: {score}.")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()







    








# source_data = game_data.data

# def score_check(item1,item2):
#     """ Brings back the highest of the result"""
#     difference = max(item1,item2)
#     return difference

# ########## Big while loop starts here############   
# counter = 0
# not_lose = True
# while not_lose:
#     name = ""
#     description = ""
#     country = ""
#     followers = ""

# ########## For loop for first player values #############
#     dictionary_choice_1 = random.choice(source_data)
#     for item in dictionary_choice_1:
#         if item == "name":
#             name = dictionary_choice_1[item]   
#         elif item == "description":
#             description = dictionary_choice_1[item]
#         elif item == "country":
#             country = dictionary_choice_1[item]
#         elif item == "follower_count":
#             followers = dictionary_choice_1[item]
#                     ###### End ######

#     name_2 = ""
#     description_2 = ""
#     country_2 = ""
#     followers_2 = ""
# ########## For loop for second player values ############
#     dictionary_choice_2 = random.choice(source_data)
#     for item in dictionary_choice_2:
#         if item == "name":
#             name_2 = dictionary_choice_2[item]
#         elif item == "description":
#             description_2 = dictionary_choice_2[item]
#         elif item == "country":
#             country_2 = dictionary_choice_2[item]
#         elif item == "follower_count":
#             followers_2 = dictionary_choice_2[item]
#                      ###### End ######


#     opponent_1 = (f"Compare A: {name}, {description}, {country}" )
#     score_of_opponent_1 = followers
#     opponent_2 = (f"Against B: {name_2}, {description_2}, {country_2}")
#     score_of_opponent_2 = followers_2
#     print(art.logo)
#     print(opponent_1)
#     print(art.vs)
#     print(opponent_2)
#     print("\n")
    
    
#     ############ User decision ##########
#     user_decision = input("Who has more followers? Type 'A' or 'B': ").lower()
#     for letters in user_decision:
#         if letters == "a":
#             user_a = letters
#         elif letters == "b":
#             user_b = letters
            
            

#     user_a = score_of_opponent_1 # Number of followers
#     user_b = score_of_opponent_2 # Number of followers
#     output = score_check(user_a, user_b)

#     if user_a == user_b:
#         print("Draw.... Continue")
#     elif user_a == output and user_decision == "a":
#         print(f"You are correct {output}")
#         counter += 1
#     elif user_b == output and user_decision == "b":
#         print(f"You are correct {output}")
#         counter += 1 
#         clear()
#     else:
#         print(f"Sorry, that's wrong. Final score: {counter}")
#         not_lose = False
        
        


















