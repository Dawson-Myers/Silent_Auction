from art import logo
print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record: # loops through the bidding_record aka the bids dictionary from below using the bidder or 'key' aka name
        bid_amount = bidding_record[bidder] # associates the 'value' aka price of the bids dictionary with a new variable bid_amount
        if bid_amount > highest_bid: # compares the current bid with the stored highest bid 
            highest_bid = bid_amount # assigns the highest bid with the new bid amount if its larger 
            winner = bidder # assigns key aka name to the winner variable 
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price # stores the inputs data of name and price as the 'key' : 'value' pair in the bids dictionary
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids) # runs the function using the bids dictionary as the input
    elif should_continue == "yes":
        print("\n" * 20)


