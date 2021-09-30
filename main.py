from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
import operator
bidders = {}
while True:
  print(art.logo)
  name = input("What is your name?\n")
  bid = input("How much do you wish to bid?\n$ ")
  bidders[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

  if other_bidders == "yes":
     clear()
  
  else:
    winner = max(bidders.items(), key=operator.itemgetter(1))[0]
    win_bid = bidders[winner]
    clear()
    print(art.logo)
    print(f"\nThe highest bidder is {winner} with a bid of $ {win_bid}")
    break

