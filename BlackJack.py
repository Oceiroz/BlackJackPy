import random
    
def get_input(input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")
        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print("Invalid input, Please try again:\n")
    return user_input
def get_choice(input_message, choices):
    while(True):
        for x, choice in enumerate(choices):
            print(f"\n{x+1} --> {choices[x]}\n")
            
        raw_input = input(f"\n{input_message}\n")
        try:
            user_input = int(raw_input)
            if user_input > x+1 or user_input < 1:
                raise ValueError
            elif user_input <= x+1 or user_input >= 1:
                break
        except ValueError:
            print("Your input is invalid, please try again.")
    return user_input

def black_start():
    options = ["Yes", "No"]
    black_start = get_choice("Would you like to play blackjack?", options)
    cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "king", "queen"]
    card_instance = {"ace":0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "jack":0, "king":0, "queen":0}
    points = 0
    rounds = 1
    cards_amount = 0
    random_index = 0
    if black_start == 1:
        blackjack(cards, card_instance, random_index, points, cards_amount, rounds)
    elif black_start == 2:
        print("Okay Buddy")
        
def blackjack(cards, card_instance, random_index, points, cards_amount, rounds):
    # rounds
    # 13 cards
    while(True):
        print(f"rounds: {rounds}")
        print(f"points: {points}")
        random_index = random.randint(0,12)
        if rounds == 1:
            get_card2(cards, card_instance, random_index, points, cards_amount, rounds)
            if points >= 15 and points <21:
                options = ["hit", "stick"]
                hit_stick = get_choice(f"You have {points} points.\n What would you like to do?", options)
                if hit_stick == 1:
                    get_card(cards, card_instance, random_index, points, cards_amount, rounds)
                elif hit_stick == 2:
                    stick_card(cards, card_instance, random_index, points, cards_amount, rounds)
            elif points < 15:
                get_card(cards, card_instance, random_index, points, cards_amount, rounds)
            elif points == 21:
                print(f"You won with {cards_amount} cards and in {rounds} rounds")
                break
            elif points > 21:
                print(f"awhhhh, you went bust... you were {points - 21} points over, you had {cards} cards, and finished in {rounds} rounds.")
                break
            
        elif rounds > 1:
            if points >= 15 and points <21:
                options = ["hit", "stick"]
                hit_stick = get_choice(f"You have {points} points.\n What would you like to do?", options)
                if hit_stick == 1:
                    get_card(cards, card_instance, random_index, points, cards_amount, rounds)
                elif hit_stick == 2:
                    stick_card(cards, card_instance, random_index, points, cards_amount, rounds)
            elif points < 15:
                get_card(cards, card_instance, random_index, points, cards_amount, rounds)
            elif points == 21:
                print(f"You won with {cards_amount} cards and in {rounds} rounds")
                break
            elif points > 21:
                print(f"awhhhh, you went bust... you were {points - 21} points over, you had {cards_amount} cards, and finished in {rounds} rounds.")
                break
    black_start()

def ace(cards, card_instance, random_index, points, cards_amount, rounds):
    options = [1, 11]
    ace = get_choice("Would you like a value of 1 or 11", options)
    if ace == 1:
        points += 1
    elif ace == 2:
        points += 11
    cards_amount += 1
    blackjack(cards, card_instance, random_index, points, cards_amount, rounds)

def get_card(cards, card_instance, random_index, points, cards_amount, rounds):
    while(True):
        for x, card in enumerate(cards):
            if x == random_index and card_instance[cards[x]] < 4:
                
                card_instance[cards[x]] += 1
                
                print(f"The card is: {cards[x]}\n")
                
                card_limit = False
                
                if cards[x] == "ace":
                    ace(cards, card_instance, random_index, points, cards_amount, rounds)
                    
                elif cards[x] == "jack" or cards[x] == "king" or cards[x] == "queen":
                    points += 10
                    
                elif cards[x] != ace and cards[x] != "jack" and cards[x] != "king" and cards[x] != "queen":
                    points += int(cards[x])
                    
                cards_amount += 1
                rounds += 1
                break
            
            elif x == random_index and card_instance[cards[x]] >= 4:
                card_limit = True
                break
        
        if card_limit == False:
            break
    blackjack(cards, card_instance, random_index, points, cards_amount, rounds)
    
def stick_card(cards, card_instance, random_index, points, cards_amount, rounds):
    while(True):
        points += 0
        for x, card in enumerate(cards):
            if x == random_index and card_instance[cards[x]] < 4:
                
                card_instance[cards[x]] += 1
                
                print(f"The card is: {cards[x]}\n")
                
                card_limit = False
                cards_amount += 0
                rounds += 1
                break
            
            elif x == random_index and card_instance[cards[x]] >= 4:
                card_limit = True
                break
        
        if card_limit == False:
            break
    blackjack(cards, card_instance, random_index, points, cards_amount, rounds)
    
def get_card2(cards, card_instance, random_index, points, cards_amount, rounds):
    card_list = []
    while(cards_amount < 2):
        random_index = random.randint(0, 12)
        while(True): 
            
            for x, card in enumerate(cards):
                if x == random_index and card_instance[cards[x]] < 4:
                
                    card_instance[cards[x]] += 1
                
                    card_list.append(cards[x])
                
                    card_limit = False
                
                    if cards[x] == "ace":
                        ace(cards, card_instance, random_index, points, cards_amount, rounds)
                    
                    elif cards[x] == "jack" or cards[x] == "king" or cards[x] == "queen":
                        points += 10
                    
                    elif cards[x] != ace and cards[x] != "jack" and cards[x] != "king" and cards[x] != "queen":
                        points += int(cards[x])
                    
                    cards_amount += 1
                    break
            
                elif x == random_index and card_instance[cards[x]] >= 4:
                    card_limit = True
                    break
        
            if card_limit == False:
               
                break
    rounds += 1
    print(f"Your first two cards are: {card_list}\n")
    blackjack(cards, card_instance, random_index, points, cards_amount, rounds)
    
black_start()