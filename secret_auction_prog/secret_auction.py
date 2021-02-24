logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
#HINT: You can call clear() to clear the output in the console.
bidder = {}

def find_highest_bidder(bidder_amount):
    highest_bid = 0
    winner = ""
    for person in bidder_amount:
        bidder_result = bidder_amount[person]
        if bidder_result > highest_bid:
            highest_bid = bidder_result
            winner = person
    print(f"The winner is {winner} with the amount of ${highest_bid}")    
            

bidding = True
while bidding:
    user_name = input("What is your name? ")
    bid_amount = int(input("what's your bid?: $"))
    bidder[user_name] = bid_amount
   
    more_bidders = input("Are there any other bidders? 'yes' or 'no'\n")
    if more_bidders == "no":
        find_highest_bidder(bidder)
        print(bidder)
        bidding = False
    elif more_bidders == "yes":
        continue
        #clear() 
    










