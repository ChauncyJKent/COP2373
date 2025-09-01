class SpamFilter:
    """A class for handling the analysis of text messages to determine 
    the likelihood that they are spam.
    """
    # Defines the __init__ method for the SpamFilter class.
    def __init__(self):
        # Initializes a list of 40 of the most common words and phrases
        # commonly associated with spam messages.
        self.spam_words = [
            '#1', '100% more', '100% free', '100% satisfied', 
            'additional income', 'be your own boss', 'best price', 
            'big bucks', 'billion', 'cash bonus', 'act now', 
            'apply now', 'become a member', 'call now', 'click below', 
            'click here', 'get it now', 'do it today', 'don\'t delete', 
            'exclusive deal', 'bulk email', 'buy direct', 
            'cancel at any time', 'check or money order', 
            'congratulations', 'confidentiality', 'cures', 
            'dear friend', 'direct email', 'direct marketing', 
            'accept credit cards', 'ad', 'all new', 'as seen on', 
            'bargain', 'beneficiary', 'billing', 'bonus', 
            'cards accepted', 'cash'
            ]
        # Initializes an attribute to store the suspicious message.
        self.message = ''
        # Initializes an attribute to accumulate the message's spam 
        # score.
        self.spam_score = 0
        # Initializes a dictionary to count the number of instances of 
        # each 'spam word' identified within the message.
        self.found_spam_words = {}
        # Initializes an attribute to store the likelihood the message 
        # is spam.
        self.likelihood = ''
    
    # Defines the get_message method.
    def get_message(self):
        """Prompts the user to enter the contents of a suspicious 
        message for analysis. Stores the message in the self.message 
        attribute.
        """
        # Prompts the user for the message, converts it all to lowercase 
        # to match the case of the spam words list, and assigns it to 
        # the self.message attribute.
        self.message = input('Please enter the suspicious message: ').lower()

    def scan_message(self):
        """Takes each word or phrase from the spam_words list and checks 
        to see if it's in self.message. If so, it increments 
        self.spam_score by 1 and adds the identified word to the
        self.found_spam_words dictionary, or if already present, 
        increments its entry by 1.
        """
        # Loops through the spam_words list, checking to see if any of 
        # the words are in self.message.
        for phrase in self.spam_words:
            # If the word or phrase is in the message increments 
            # self.spam_score by 1 and adds the occurance of the word or 
            # phrase to self.found_spam_words.
            if phrase in self.message:
                self.spam_score += 1
                self.found_spam_words[phrase] = self.found_spam_words.get(
                    phrase, 0) + 1

    def spam_likelihood(self):
        """Checks self.spam_score and determines from that the 
        likelihood that self.message is a spam message.
        """
        # Checks the spam_score to determine the likelihood the message 
        # is spam. Starts at the upper end to avoid accidental miss-
        # categorization.
        if self.spam_score >= 10:
            self.likelihood = 'Definitely Spam'
        elif self.spam_score >= 8:
            self.likelihood = 'Probably Spam'
        elif self.spam_score >= 6:
            self.likelihood = 'Maybe Spam'
        elif self.spam_score >= 4:
            self.likelihood = 'Potentially Spam'
        else:
            self.likelihood = 'Probably Not Spam'

    def display_results(self):
        """Displays the results from the analysis of self.message."""
        # Prints a message identifying what's being printed next.
        print('Below are the results from the scan of your message:')
        # Prints self.spam_score.
        print(f'Spam Score: {self.spam_score}')
        # Prints self.likelihood.
        print(f'Likelihood message is spam: {self.likelihood}')
        # Prints a message identifying the following prints as the words 
        # or phrases that triggered the above ratings.
        print(f'Words and phrases that prompted these results:')
        # loops through the key, value pairs in self.found_spam_words 
        # printing each word or phrase along with its number of 
        # occurances.
        for phrase, occurances in self.found_spam_words.items():
            print(f'{occurances} occurance(s) of {phrase}.')

# Defines the main function.
def main():
    # Creates an instance of the SpamFilter class.
    filter = SpamFilter()
    # Calls the get_message method of this instance of the SpamFilter 
    # class.
    filter.get_message()
    # Calls the scan_message method of this instance of the SpamFilter
    # class.
    filter.scan_message()
    # Calls the spam_likelihood method of this instance of the 
    # SpamFilter class.
    filter.spam_likelihood()
    # Calls the display_results method of this instance of the 
    # SpamFilter class.
    filter.display_results()

# In the event that this file is executed directly, calls the main 
# method to start the program.
if __name__ == '__main__':
    main()
    