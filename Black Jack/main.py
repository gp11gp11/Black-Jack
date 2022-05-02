############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.



import random
from art import logo
#from replit import clear

print(logo)

replay = True
while replay:
  dealer = []
  player = []
  
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  
  def draw():
    the_Draw = random.choice(cards)
    return the_Draw
  dealer.append(draw())
  dealer.append(draw())
  player.append(draw())
  player.append(draw())
  
  flag = True
  def dealer_decktodisplay():
    dealer_deck = []
    for things in range (len(dealer)-1):
      dealer_deck.append(dealer[things])
    print(dealer_deck)
  
  def dealer_sum():
    dealer_s=0      
    for number in dealer:#instead can use sum(),pass list into it
      dealer_s+=number
    return dealer_s
  def player_sum():
    player_s=0
    for number in player:
      player_s+=number
    return player_s
      
      
  while flag:
    if player_sum()>21:
        if 11 in player:
          player.remove(11)
          player.append(1)
    print("computer's visible cards:")
    dealer_decktodisplay()
    print("user's cards:")
    print(player)
    choice = input("Do you want other card?type 'yes' or 'no'")
    if choice == "no":
      flag=False
      sum_of_player = player_sum()
      sum_of_dealer = dealer_sum()
      if sum_of_player<21 and sum_of_player>sum_of_dealer:
        if sum_of_player==21:
          print("you win with a Blackjack")
        else:
          print("you win")
      elif sum_of_player==sum_of_dealer:
        print("draw")
      else:
        if sum_of_dealer==21:
          print("you lose,opponent has Blackjack")
        else:
          print("you lose")
  
    if choice == "yes":
      if dealer_sum()== player_sum():
        print("draw")
      elif dealer_sum()==21 or player_sum==21:
        if dealer_sum()==21:
          print("you lose,opponent has blackjack")
          flag = False
        else:
          print("you won with blackjack")
          flag = False 
      elif player_sum()>21 and  dealer_sum()>21:
        flag = False
        if player_sum()>dealer_sum():
          print("you lose")
        else:
          print("you won")
      elif player_sum()>21:
        print("you lose")
        flag = False
      elif dealer_sum()>21:
        print("you win")
        flag = False
      if flag==True:
        flag_in = True
        while flag_in:
          last_of_list=dealer.append(draw())
          if dealer_sum()<12:
            dealer.remove(last_of_list)
          else:
            flag_in = False
        player.append(draw())
      
  print(f"cards with opponent:{dealer}")
  print(f"cards with user:{player}")
      
  option_for_restart = input("Do you have to restart? type 'yes'") 
  if option_for_restart =="yes":
    replay = True
  else:
    replay = False
  
  
