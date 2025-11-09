import random

# Defines the main method.
def main():
    # Initializes a Deck object.
    deck = Deck()
    # Deals an initial hand of 5 cards.
    for i in range(5):
        deck.deal()
    # Displays the current hand, and prints a blank line after it.
    print(deck.cards_in_play_list, '\n')
    # Calls the discard_and_draw method.
    deck.discard_and_draw()
    # Displays the new hand after discarding and drawing.
    print(deck.cards_in_play_list, '\n')

def str_val(input_message, error_message, valid_entry_dict):
    """Used to validate a string input from the user.
    
    input_message = a string to be used as a prompt for input from the 
      user.
    error_message = a string that is displayed if the user's input is
      invalid.
    valid_entry_dict = a dictionary of valid lowercase string responses
      keyed to expected outputs.

    Prompts the user for a specific string then checks to make sure it's
    valid. if not, informs the user the input was not valid and asks
    again for a valid entry.

    Returns a valid string.
    """
    # Initialize variables.
    valid_dict = valid_entry_dict
    # Initialize a while loop.
    while True:
        # Setup a try/except block to handle input errors.
        try:
            # Request input from the user and use it as a key in the
            # 'valid_dict' dictionary.
            entry = valid_dict[input(input_message).lower()]
            # If the input doesn't trigger the except clause, break the 
            # loop.
            break
        # Define what kind of error we're looking for.
        except KeyError:
            # Display the error message
            print(error_message)
    # Returns the now validated value of the 'entry variable.
    return entry

class Deck():
    def __init__(self, n_decks=1):
        self.card_list = [num + suit 
                          for suit in '\u2665\u2666\u2663\u2660' 
                          for num in 'A23456789TJQK' 
                          for deck in range(n_decks)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!!!')
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)

        return new_card
    
    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()

    # Defines the discard_and_draw method.
    def discard_and_draw(self):
        # Prompts the user for a number of cards they'd like to discard 
        # and replace. Validates the input and assigns it to the 
        # num_to_draw variable.
        num_to_draw = str_val(
            'How many cards would you like to replace? Enter 0-3: ', 
            'You must enter a number from 0 to 3: ', 
            {'0': 0, '1': 1, '2': 2, '3': 3}
            )
        # Initializes and empty list to store the indexes of the cards 
        # to be replaced.
        cards_to_replace = []
        # Prompts the user a number of times equal to num_to_draw to 
        # enter the position of the card they'd like to replace and 
        # appends the card to cards_to_replace.
        for i in range(num_to_draw):
            cards_to_replace.append(self.cards_in_play_list[str_val(
                'Which card would you like to replace? Enter 1-5: ', 
                'You must enter a number from 1-5: ', 
                {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4}
                )])
        # Loops a number of times equal to num_to_draw.
        for i in range(num_to_draw):
            # Removes the cards identified as the ones to replace from 
            # the cards_in_play_list and adds them to the discards_list.
            self.cards_in_play_list.remove(cards_to_replace[i])
            self.discards_list.append(cards_to_replace[i])
            # Deals a new card on each loop from those remaining in the 
            # deck.
            self.deal()

# Calls the main method if the file is directly executed.     
if __name__ == '__main__':
    main()
