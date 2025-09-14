# Imports the reduce methode from functools.
from functools import reduce

class ExpenseAnalyzer:
    """A class object that collects expense information and analyzes it 
    by determining and displaying the total of all expenses, the 
    highest expense, and the lowest expense.
    """
    # Defines the __init__ method for the ExpenseAnalyzer class.
    def __init__(self):
        # Initializes a dictionary as an attribute to store the expense 
        # information.
        self._expenses = {}
        # Initializes an attribute to store the total of all expenses.
        self._total_expense = 0
        # Initializes an attribute to store the highest expense.
        self._highest_expense = 0
        # Initializes an attribute to store the type of the highest 
        # expense.
        self._highest_type = ''
        # Initializes an attribute to store the lowest expense.
        self._lowest_expense = float('inf')
        # Initializes an attribute to store the type of the lowest 
        # expense.
        self._lowest_type = ''

    # Defines the _get_expense method.
    def _get_expense(self):
        """Handles the collection and storage of an expense. Includes 
        data validation to ensure the entered value is a number. 
        Returns expense.
        """
        # Initializes a loop control variable and sets it to True.
        invalid = True
        # Initializes a variable to store the gathered expense.
        expense = 0

        # Initializes an input validation loop.
        while invalid:
            # Initializes a try/except block.
            try:
                # Collects input from the user and attempts to convert 
                # it to a float.
                expense = float(
                    input('Please enter the amount of your expense: ')
                    )
                # If no error is raised, the loop control variable is 
                # set to False.
                invalid = False
            except ValueError:
                # If an error is raised, prints a message for the user 
                # to enter a number.
                print('Please enter a number.')
                continue
        # Returns the validated expense.
        return expense
    
    # Defines the _get_type method.
    def _get_type(self):
        """Handles the collection and storage of an expense type. 
        Includes data validation to ensure unique types are gathered 
        for each expense. Returns expense_type.
        """
        # Initializes a loop control variable and sets it to True.
        invalid = True
        # Initializes a variable to store the gathered expense.
        expense_type = ''

        # Initializes an input validation loop.
        while invalid:
            # Initializes a try/except block.
            try:
                # Collects input from the user and checks to see if it 
                # is unique among previous entries. If it's unique, 
                # it sets the loop control variable to False, otherwise 
                # raises and exception.
                expense_type = input('Please enter the name of the expense: ')
                if expense_type in self._expenses.keys():
                    raise Exception()
                else:
                    invalid = False
            except:
                # If an error is raised, prints a message for the user 
                # to enter a unique type.
                print('Please enter a unique expense name.')
                continue

        # Returns expense_type.
        return expense_type
    
    # Defines the _update_records method.
    def _update_records(self):
        """Takes the collected expense and expense type and adds them 
        to the expenses dictionary.
        """
        # Calls the _get_expense method to get an expense.
        expense = self._get_expense()
        # Calls the _get_type method to get the type of the expense.
        expense_type = self._get_type()

        # Adds the expnese and the expense type to the dictionary.
        self._expenses[expense_type] = expense

    # Defines the collect_expenses method.
    def collect_expenses(self):
        """Creates a loop adding the entered expenses and expense types 
        to the dictionary on each loop, then asks if there are more 
        expenses to be entered. Includes input validation to make sure 
        the user enters either "Y" or "N".
        """
        # Initializes a loop control variable and sets it to True.
        more = True
        # Initializes a loop.
        while more:
            # Calls the _update_records method.
            self._update_records()
            # Initializes a variable to store the user's answer.
            answer = ''
            # Initializes a loop control variable and sets it to True.
            invalid = True
            # Initializes an input validation loop.
            while invalid:
                # Requests an input from the user.
                answer = input('Are there more expenses? Y/N: ')
                # Determines if the entered answer is either "Y" or 
                # "N". If so, sets the loop control variable to False, 
                # otherwise displays a message to the user to enter 
                # either "Y" or "N".
                if answer.lower() == 'y' or answer.lower() == 'n':
                    invalid = False
                else:
                    print('Please enter "Y" or "N".')
            # Checks if answer was "N". If so, sets the loop control 
            # variable to False, otherwise starts the next loop.
            if answer.lower() == 'n':
                more = False
            else:
                continue

    # Defines the analyze_expenses method.
    def analyze_expenses(self):
        """Makes use of the reduce function to analyze the entered 
        expenses, calculating the expense total, the highest expense, 
        and the lowest expense.
        """
        # Calculates the total of the entered expenses.
        self._total_expense = reduce(lambda x, y: x + y, self._expenses.values())

        # Determines the highest expense of those entered.
        self._highest_expense = reduce(
            lambda x, y: x if x > y else y, self._expenses.values()
            )
        # Uses the value to determine the name of the expense.
        for key, value in self._expenses.items():
            if value == self._highest_expense:
                self._highest_type = key

        # Determines the lowest expense of those entered.
        self._lowest_expense = reduce(
            lambda x, y: x if x < y else y, self._expenses.values()
            )
        # Uses the value to determine the name of the expense.
        for key, value in self._expenses.items():
            if value == self._lowest_expense:
                self._lowest_type = key
    
    # Defines the display_analysis method.
    def display_analysis(self):
        """Displays the results of the analysis of the entered expenses
        including the total of all expenses, the highest expense, and 
        the lowest expense.
        """
        # Prints a blank line.
        print()
        # Displays the total of the entered expenses.
        print(f'The total of the expenses is: {self._total_expense}')
        # Displays the highest expense.
        print(
            f'The highest expense at {self._highest_expense} was: '
            + f'{self._highest_type}'
            )
        # Displays the lowest expense.
        print(
            f'The lowest expense at {self._lowest_expense} was: '
            + f'{self._lowest_type}'
            )
        # Prints a blank line.
        print()

# Defines the main function.
def main():
    # Creates an ExpenseAnalyzer Object.
    expenses = ExpenseAnalyzer()
    # Calls the collect_expenses method.
    expenses.collect_expenses()
    # Calls the analyze_expenses method.
    expenses.analyze_expenses()
    # Calls the display_analysis method.
    expenses.display_analysis()

# Calls the main function if the file is executed directly.
if __name__ == '__main__':
    main()
