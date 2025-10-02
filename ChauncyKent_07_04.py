# ChauncyKent_07_04

"""Contains the ParagraphAnalyzer class and the main function. The main 
function creates an instance of the ParagraphAnalyzer class and calls 
the appropriate methods in the correct order to save a paragraph from 
the user, where each sentence starts with a number, divide it into a 
list of sentences, count the number of sentences, and display each 
identified sentence as well as the total number of sentences counted.
"""

# imports the re module.
import re

# Defines the ParagraphAnalyzer class.
class ParagraphAnalyzer:
    """The ParagraphAnalyzer class is an object designed to collect a 
    paragraph from the user where each sentence begins with a number, 
    identify and add to a list each sentence in the paragraph, count 
    the number of sentences in the paragraph, and display the 
    identified sentences along with the total number of sentences.
    """
    def __init__(self):
        # Stores the collected paragraph and the results of its 
        # analysis.
        self.paragraph = ''
        self.sentence_list = []
        self.sentence_count = 0
    
    # Defines the get_paragraph method.
    def get_paragraph(self):
        """Prompts the user for a paragraph where each sentence begins 
        with a number and saves it to the self.paragraph attribute.
        """
        self.paragraph = input(
            'Please enter a paragraph where each sentence begins with a'
            + ' number: '
            )

    # Defines the analyze_paragraph method.
    def analyze_paragraph(self):
        """Defines a pattern that recognizes a sentence as starting 
        with a number and ending with a '.', '!', or '?' followed by 
        either a space and a number, or the end of the string. Then 
        searches the paragraph to find all qualifying substrings and 
        adds them to a list, saving the list as the value of 
        self.sentence_list.
        """
        pattern = r'[0-9].*?[.!?](?= [0-9]|$)'

        self.sentence_list = re.findall(
            pattern, self.paragraph, flags=re.DOTALL | re.MULTILINE
            )

    # Defines the count_sentences method.
    def count_sentences(self):
        """Finds the length of self.sentence_list and assigns it as the 
        value of self.sentence_count.
        """
        self.sentence_count = len(self.sentence_list)

    # Defines the _clean_sentences internal helper method.
    def _clean_sentences(self):
        # Loops through the sentences in self.sentence_list and 
        # 'cleans' them, removing extra white space, new line 
        # characters, and other 'junk'.
        for i in range(len(self.sentence_list)):
            self.sentence_list[i] = self.sentence_list[i].strip()

    # Defines the display_results method.
    def display_results(self):
        """Calls a helper method to 'clean' the formatting of the 
        sentences in self.sentence_list then loops through the list,
        printing each sentence. Finally, prints a blank line followed 
        by the total number of sentences.
        """
        self._clean_sentences()

        print()
        print('The sentences in the paragraph are: ')
        for sentence in self.sentence_list:
            print(sentence)

        print()
        print(
            'The number of sentences in the paragraph is:', 
            self.sentence_count
            )

# Defines the main function.
def main():
    """Creates a ParagraphAnalyzer object and calls the paragraph 
    collection, analysis, and display methods in the correct order.
    """
    pa = ParagraphAnalyzer()
    pa.get_paragraph()
    pa.analyze_paragraph()
    pa.count_sentences()
    pa.display_results()

# Calls the main method if the file is directly executed.
if __name__ == '__main__':
    main()
