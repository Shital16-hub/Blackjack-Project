############### Blackjack Project #####################

from art import logo
from replit import clear
import random


def deal_card():
    ''' function that uses the List below to *return* a random card.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    ''' This function takes the list of user and computer deal and calculates the score '''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    '''This function takes the input as card numbers and compares the score of user and comouter score'''
    # Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose "
    elif user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, opponent has Blackjack "
    elif user_score == 0:
        return "Win with a Blackjack "
    elif user_score > 21:
        return "You went over. You lose "
    elif computer_score > 21:
        return "Opponent went over. You win "
    elif user_score > computer_score:
        return "You win "
    else:
        return "You lose "


def play_game():
    print(logo)
    user_cards = []  # list of user cards
    computer_cards = []  # list of computer cards
    is_game_over = False

    for i in range(2):  # selects two random cards for each user and computer from list of cards
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)

    while not is_game_over:
        # Calculate user score and computer score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"user cards:{user_cards},user score :{user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to ger another card or 'n' to pass :")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:  # checks the condition computer_score<17 and updates the list of computer score
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"User cards:{user_cards},Final score of user:{user_score}")
    print(f"Final score of computer:{computer_score}")
    print(compare(user_score, computer_score))


play_game()
want_to_play = input("Do you want to play ? If yse then enter 'y' else enter 'n'.")
if want_to_play == "y":
    clear()
    play_game()
else:
    print("Thank you")
