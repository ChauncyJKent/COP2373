class SpamFilter:
    def __init__(self):
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
        self.message = ''
        self.spam_score = 0
        self.found_spam_words = {}
        self.likelyhood = ''

    def get_message(self):
        self.message = input('Please enter the suspicious message: ').lower()

    def scan_message(self):
        for phrase in self.spam_words:
            if phrase in self.message:
                self.spam_score += 1
                self.found_spam_words[phrase] = self.found_spam_words.get(
                    phrase, 0) + 1

    def spam_likelyhood(self):
        if self.spam_score >= 10:
            self.likelyhood = 'Definitely Spam'
        elif self.spam_score >= 8:
            self.likelyhood = 'Probably Spam'
        elif self.spam_score >= 6:
            self.likelyhood = 'Maybe Spam'
        elif self.spam_score >= 4:
            self.likelyhood = 'Potentially Spam'
        else:
            self.likelyhood = 'Probably Not Spam'

    def display_results(self):
        print('Below are the results from the scan of your message:')
        print(f'Spam Score: {self.spam_score}')
        print(f'Likelyhood message is spam: {self.likelyhood}')
        print(f'Words and phrases that prompted these results:')
        for phrase, occurances in self.found_spam_words.items():
            print(f'{occurances} occurance(s) of {phrase}.')

def main():
    filter = SpamFilter()
    filter.get_message()
    filter.scan_message()
    filter.spam_likelyhood()
    filter.display_results()

if __name__ == '__main__':
    main()
    