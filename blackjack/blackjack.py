# Blackjack

import random
import time
import sys

def create_deck():
    # Creates the deck
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = []
    for suit in suits:
        for rank in ranks:
            card = f'{rank} of {suit}'
            deck.append(card)
    return deck

def deposit(player_amounts):
    # This function will iterate over every player and ask for a deposit amount, it will store it in a nested dictionary
    for player, player_data in player_amounts.items():
        while True:
            try:
                amount = float(input(f"{player}, enter deposit amount: "))
                if amount < 100:
                    print("Min Deposit amount is $100.\n")
                    continue
                else:
                    player_data["balance"] += amount
                    print(f"{player}, your deposit of ${amount:.2f} has been successful.\n")
                    break
            except ValueError:
                print("Enter a number.\n")

def start_game(players, dealer, deck):
    # Give every player one card and remove it from the deck
    for _ in range(2):
        for player in players:
            # Make sure the deck is not empty
            if deck:
                random_card_index = random.randint(0, len(deck) - 1)
                drawn_card = deck.pop(random_card_index)
                players[player]["cards"].append(drawn_card)
            if drawn_card in ["Ace of Hearts", "Ace of Diamonds", "Ace of Spades", "Ace of Clubs"]:
                players[player]["ace_count"] += 1
        # Give dealer a card and remove it from the deck
        random_card_index = random.randint(0, len(deck) - 1)
        drawn_card = deck.pop(random_card_index)
        dealer["cards"].append(drawn_card)
        if drawn_card in ["Ace of Hearts", "Ace of Diamonds", "Ace of Spades", "Ace of Clubs"]:
            dealer["ace_count"] += 1
        
    
def place_bets(player_amounts):
    for player, player_data in player_amounts.items():
        while True:
            try:
                bet_amount = float(input(f"{player}, enter your bet: "))
                if 0 <= bet_amount <= player_data["balance"] and bet_amount > 49:
                    player_data["balance"] -= bet_amount
                    player_data["bet"] += bet_amount
                    print(f"{player}, your bet of ${bet_amount:.2f} has been placed.\n")
                    break
                elif bet_amount < 50:
                    print("Minimum bet amount is $50")
                else:
                    print("Invalid bet amount. Please enter a valid amount within your available balance.\n")
            except ValueError:
                print("Enter a Valid Amount.\n")

def hit(players, player, deck):
    if deck:
        random_card_index = random.randint(0, len(deck) - 1)
        drawn_card = deck.pop(random_card_index)
        players[player]['cards'].append(drawn_card)
    # Update ace count
    if drawn_card in ["Ace of Hearts", "Ace of Diamonds", "Ace of Spades", "Ace of Clubs"]:
        players[player]["ace_count"] += 1
    # UPDATE TOTAL_VALUE AFTER HIT
    card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    new_card = players[player]["cards"][-1]
    value = new_card.split()
    players[player]["total_value"] += card_values[value[0]]
         
def dealer_hit(dealer, deck):
    random_card_index = random.randint(0, len(deck) - 1)
    drawn_card = deck.pop(random_card_index)
    dealer["cards"].append(drawn_card)
    # Update ace count
    if drawn_card in ["Ace of Hearts", "Ace of Diamonds", "Ace of Spades", "Ace of Clubs"]:
        dealer["ace_count"] += 1
    # UPDATE TOTAL_VALUE AFTER HIT
    card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    new_card = dealer["cards"][-1]
    value = new_card.split()
    dealer["total_value"] += card_values[value[0]]


def print_cards(players):
    for player, player_data in players.items():
        formatted_cards = ", ".join(player_data["cards"])
        print(f"{player}'s cards: {formatted_cards}\n")
    
def card_values(players, dealer):
    card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    for player, player_data in players.items():
        for card in player_data["cards"]:
            value = card.split()
            player_data["total_value"] += card_values[value[0]]
    # Get the value for the dealer's card
    for card in dealer["cards"]:
        value = card.split()
        dealer["total_value"] += card_values[value[0]]
    
    
   
def main():
    print("\nWelcome to Blackjack\n")
    # Get player count
    while True:
        try:
            player_count = int(input("Enter Player Count(5 MAX): "))
            if player_count <= 0:
                print("Enter a number greater than 0.\n")
                continue
            elif player_count > 5:
                print("Max player count is 5.\n")
                continue
            else:
                break
        except ValueError:
            print("Enter a number.\n")

    players = {}
    dealer = {"cards": [], "total_value": 0, "ace_count": 0, "blackjack": False}
    
    # Creates all the players in a dict and creates a another dict inside with cards, total_value, and blackjack boolean
    for i in range(1, player_count + 1):
        player_name = f"Player {i}"
        # players[player_name] = []
        players[player_name] = {"cards": [], "total_value": 0, "blackjack": False, "ace_count": 0}

    # Create a nested dictionary to store each player's balance and bets
    player_amounts = {}
    for player in players:
        player_amounts[player] = {"balance": 0.0, "bet": 0.0}
    deposit(player_amounts)


    #   GAME LOGIC

    while True:
        if not players:
            print("All players have been removed to due lack of balance.\n")
            sys.exit()
        user_input = input("Press enter to play or enter q to exit and cash out: ")
        if user_input == '':
            # Print Player Balances
            for player in player_amounts:
                print(f"{player}'s balance: ${player_amounts[player]['balance']}")
            print()


            # Create the deck
            deck = create_deck()

            # Make each player place a bet (MIN $50)
            place_bets(player_amounts)

            # Start game will give everyone two cards in the right order, then the card_values() will give values to all the cards
            start_game(players, dealer, deck)
            card_values(players, dealer)

            #Print cards for players and for dealer leaving out one of the dealer's cards
            print_cards(players)
            print(f"Dealer's cards: {dealer['cards'][0]}, (HIDDEN CARD)\n")
            time.sleep(1)

            # Check for player blackjack
            for player in players:
                if players[player]['total_value'] == 21:
                    players[player]["blackjack"] = True

            # Check for dealer blackjack
            if dealer["total_value"] == 21:
                dealer['blackjack'] = True

            # If dealer has blackjack, hand ends and every player that didn't get blackjack loses
            if dealer['blackjack'] == True:
                print("Hand is over, dealer has blackjack.\n")
                for player in players:
                    if players[player]["blackjack"] == True:
                        player_amounts[player]["balance"] += player_amounts[player]["bet"]
                        player_amounts[player]["bet"] = 0
                        print(f"{player} also has blackjack, bet amount has been returned, balance: ${player_amounts[player]['balance']}\n")
                    else:
                        player_amounts[player]["bet"] = 0
                        print(f"{player} has lost the bet, balance: ${player_amounts[player]['balance']}\n")
                # Remove players that have less balance than min bet amount
                players_to_remove = []
                for player in player_amounts:
                    if player_amounts[player]['balance'] < 50:
                        print(f"{player}'s balance is below the min bet, therefor they are out.\n")
                        players_to_remove.append(player)
                for player in players_to_remove:
                    del players[player]
                    del player_amounts[player]
                

            # Dealer didn't have blackjack, game goes on
            else:
                # Hit or Stay
                # Loop ends when all players have either opted to stay or busted
                for player in players:
                    # The first while loop checks if current player has blackjack, 21, or if player busted
                    while True:
                        # Check if player has blackjack, or if he has 21 before hitting again
                        if players[player]['total_value'] == 21 and players[player]["blackjack"] == True:
                            print(f"{player} has blackjack!\n")
                            time.sleep(1.5)
                            break
                        elif players[player]['total_value'] == 21 and players[player]["blackjack"] == False:
                            print(f"{player}'s total card value is 21.\n")
                            time.sleep(1.5)
                            break
                        # If player busted, check if he has ace in hand
                        elif players[player]['total_value'] > 21: 
                            if players[player]['ace_count'] > 0:
                                players[player]['total_value'] -= 10
                                players[player]['ace_count'] -= 1
                            else:
                                print(f"{player} busted, better luck next time.\n")
                                time.sleep(1.5)
                                break
                        # If player has less than 21, then continue with the loop
                        # Loop that runs until user enters either h or s
                        while True:
                            answer = input(f"{player}'s cards: {', '.join(players[player]['cards'])}\n{player}, would you like to hit or stay? (h/s): ")
                            if answer not in ['h', 's']:
                                print("Enter either 'h' or 's'.")
                            else:
                                break
                        if answer == 'h':
                            hit(players, player, deck)
                            time.sleep(1)
                            print(f"{player}'s cards: {', '.join(players[player]['cards'])}\n")
                        elif answer == 's':
                            print()
                            break

                # Check if game is still going by looping through the players and checking if at least one player is still in
                game_still_going = False
                for player in players:
                    if players[player]['total_value'] <= 21:
                        game_still_going = True

                # Do everything at the bottom only if game is still going meaning there is at least one player with 21 or less
                if game_still_going:
                    # If dealer's total_value is 17 or above he stays, else he hits
                    print(f"Dealer's Cards: {', '.join(dealer['cards'])}\n")
                    while True: 
                        if dealer['total_value'] >= 17:
                            break
                        elif dealer['total_value'] <= 16:
                            dealer_hit(dealer, deck)
                            print("Dealer hit...\n")
                            time.sleep(2)
                            print(f"Dealer's Cards: {', '.join(dealer['cards'])}\n")
                            if dealer['total_value'] == 21:
                                print("Dealer's total card value is 21.\n")
                                break
                            elif dealer['total_value'] > 21:
                                if dealer['ace_count'] > 0:
                                    dealer['total_value'] -= 10
                                    dealer['ace_count'] -= 1
                                else:
                                    print("Dealer busted.\n")
                                    break

                # Compare scores to see who wins their bet
                dealer_final_value = dealer['total_value']
                for player in players:
                    time.sleep(1)
                    # If player has blackjack
                    if players[player]["blackjack"] == True:
                        player_amounts[player]["balance"] += player_amounts[player]["bet"] + (player_amounts[player]["bet"] * 1.5)
                        player_amounts[player]["bet"] = 0
                        print(f"{player} hit blackjack, balance: ${player_amounts[player]['balance']}\n")
                    # If dealer busted
                    elif dealer_final_value > 21 and players[player]["total_value"] <= 21:
                        player_amounts[player]["balance"] += player_amounts[player]["bet"] * 2
                        player_amounts[player]["bet"] = 0
                        print(f"Dealer busted, {player}'s balance: ${player_amounts[player]['balance']}\n")
                    # If player busted
                    elif players[player]["total_value"] > 21:
                        player_amounts[player]["bet"] = 0
                        print(f"{player} busted, balance: ${player_amounts[player]['balance']}\n")
                    # If player beats dealer
                    elif players[player]["total_value"] > dealer_final_value:
                        player_amounts[player]["balance"] += player_amounts[player]["bet"] * 2
                        player_amounts[player]["bet"] = 0
                        print(f"{player} beat dealer, balance: ${player_amounts[player]['balance']}\n")
                    # If dealer beats player
                    elif players[player]["total_value"] < dealer_final_value:
                        player_amounts[player]["bet"] = 0
                        print(f"Dealer beat {player}, balance: ${player_amounts[player]['balance']}\n")
                    # If dealer and player tie
                    elif players[player]["total_value"] == dealer_final_value:
                        player_amounts[player]["balance"] += player_amounts[player]["bet"]
                        player_amounts[player]["bet"] = 0
                        print(f"{player} and dealer tied, balance: ${player_amounts[player]['balance']}\n")
                
                    
                

                # Reset players and dealer dicts back to default
                for player in players:
                    players[player] = {"cards": [], "total_value": 0, "blackjack": False, "ace_count": 0}
                dealer = {"cards": [], "total_value": 0, "ace_count": 0, "blackjack": False}
                # Check if anyone's balance is less than the min bet ($50) and remove them from players dict
                players_to_remove = []
                for player in player_amounts:
                    if player_amounts[player]['balance'] < 50:
                        print(f"{player}'s balance is below the min bet, therefor they are out.\n")
                        players_to_remove.append(player)
                for player in players_to_remove:
                    del players[player]
                    del player_amounts[player]
                

        elif user_input == 'q':
            for player in player_amounts:
                print(f"{player} has cashed out ${player_amounts[player]['balance']}")
            print()
            break
            

if __name__ == "__main__":
    main()
