DAY 11 BLACKJACK CAPSTONE PROJECT



import random


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#function to return a random card from the deck
def deal_card():   
    return cards[random.choice(cards)]
    
def calculate_score(cards):
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    
    
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
      return "It's a draw!"
      
    elif user_score == 0:
       return "It's a Blackjack. You win!"
   
    elif computer_score == 0:
        return "You lose! Computer has Blackjack"
        
    elif user_score > 21:
        return "You went over. You lose!"
        
    elif computer_score > 21:
       return "Computer went over. You win!"
        
    elif user_score > computer_score:
        return "You win!"
        
    else:
       return "You lose!" 
    
def play_game():
    
    print(logo)
    
    user_cards = []
    computer_cards = []
    
    #we declare a boolean variable to track if the game is over
    is_game_over = False
    
    #deal the user and the compu  two cards each using deal_card()
    for i in range(2):
        x = deal_card()
        user_cards.append(x) 
        y = deal_card()
        computer_cards.append(y)
    
    #till is_game_over is ----
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards = {user_cards}, Your current score = {user_score}")
        print(f"Computer's first card: {computer_cards[0]}\n")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True    
        
        else:    
            user_should_deal = input("\nType 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                
            else:
                is_game_over = True
    
    while computer_score != 17 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"\nYour final hand is = {user_cards} and your final score is = {user_score}")
    print(f"Computer final hand is = {computer_cards} and Computer final score is = {computer_score}\n")    
    print(compare(user_score, computer_score))
    print("\n\n")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()












