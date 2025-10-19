# ChauncyKent_09_01

"""Contains the BankAcct class and the test_bank_acct function, as well 
as the yes_no_val function. The test_bank_acct function creates an 
instance of the BankAcct class and calls the appropriate methods in the 
correct order to test the functionality of each method associated with 
the BankAcct class.
"""

# Imports the random module.
import random

# Defines the BankAcct class.
class BankAcct:
    """A class for tracking and modifying your bank account.

    Allows the user to track their balance, calculate interest, apply 
    interest, display their name, account number, or balance, and print 
    their balance and total interest earned. Generates a random account 
    number upon account creation.
    """
    def __init__(self, name):
        # Assigns initial values to the class attributes.
        self.name = name
        # Generates a random account number.
        self.acct_num = random.randint(10000, 99999)
        self.balance = 0
        self.interest = 0
        self.apr = 0.0

    # Defines the __str__ dunder method, defining what is displayed when 
    # a BankAcct object is printed.
    def __str__(self):
        return (f'Current Principal Balance: ${self.balance:,.2f} \n'
                + f'Earned Interest: ${self.interest:,.2f}')
    
    # Defines the update_name method.
    def update_name(self, name):
        """Overwrite the account holder's name with a new name.

        args:
        name = A string representing the name of the account holder.
        """
        self.name = name

    # Defines the display_name method.
    def display_name(self):
        """Displays the name attached to the account."""
        print(f'The name on the account is: {self.name}')

    # Defines the display_acct_num method.
    def display_acct_num(self):
        """Displays the account number attached to the account."""
        print(f'The account number is: {self.acct_num}')

    # Defines the set_apr method.
    def set_apr(self, apr):
        """Overwrites the current APR with a new one.

        args:
        apr = a number representing the interest rate for the account.
        """
        self.apr = apr

    # Defines the withdrawl method.
    def withdrawl(self, amount):
        """Handles withdrawl transactions initiated by the user.

        First checks to see if the account has sufficient funds for the 
        withdrawl. If so, removes the indicated amount from the 
        account, if not, displays an error message and does not execute 
        the withdrawl.

        args:
        amount = a number representing the amount of money to be 
          withdrawn.
        """
        # Checks to make sure there's enough money in the account to 
        # withdrawl the indicated amount.
        if self.balance - amount < 0:
            print(f"You don't have enough money in your account to "
                  + f"withdrawl that amount. The most you can withdrawl"
                  + f" is ${self.balance:,.2f}.")
        else:
            # If there's enough money to cover the withdrawl, removes 
            # the indicated amount from the account balance.
            self.balance -= amount

    # Defines the deposit method.
    def deposit(self, amount):
        """Handles deposit transactions initiated by the user.
        
        Adds the indicated amount to the account balance.

        args:
        amount = a number representing the amount of money to be 
          withdrawn.
        """
        self.balance += amount

    # Defines the get_balance method.
    def get_balance(self):
        """Displays the current account balance."""
        print(f'Your balance is: ${self.balance:,.2f}')

    # Defines the calc_interest method.
    def calc_interest(self, days):
        """Calculates how much interest will be earned over the 
        indicated number of days.

        Assumes interest is compounded daily. Calculates interest and 
        adds it to balance one day at a time, repeating this opperation 
        for a number of days equal to the indicated time period. Then 
        displays the interest that would be earned over that time period 
        and checks with the user if the calculation was merely 
        hypothetical or if they'd like to apply the calculated interest 
        to the account balance. If they give an affirmative response, 
        the calculated interest is added to the account balance.

        args:
        days = an integer representing the number of days over which to 
          calculate interest.
        """
        # Creates a local balance to calculate compound interest without 
        # altering the actual account balance.
        balance = self.balance
        # An accumulator that tracks the total interest earned.
        total_interest = 0
        for i in range(days):
            # Calculates the interest for the day.
            interest = balance * self.apr
            # Adds the daily interest to the local balance.
            balance += interest
            # Adds the daily interest to the total interest.
            total_interest += interest

        # Displays the interest earned over the indicated number of days.
        print(f'Interest after {days} days will be: ${total_interest:,.2f}')
        # Asks the user if they want to apply the calculated interest to 
        # the actual account balance.
        answer = yes_no_val(
            'Would you like to execute this opperation and update your '
            + 'balance? ', 
            'Invalid response. Please enter Yes or No.'
            )
        # If they answer yes, the total interest accumulated is added to 
        # the actual balance and the interest attribute.
        if answer == 'y':
            self.balance += total_interest
            self.interest += total_interest

def test_bank_acct():
    """Creates a BankAcct object and tests the associated methods."""
    # Creates a BankAcct object with an intentionally mispelled name.
    test_acct = BankAcct('John Smth')
    # Sets the interest rate to 10%.
    test_acct.set_apr(0.1)
    # Deposits $200 into the account.
    test_acct.deposit(200)
    # Attempts to withdrawl $300 from the account, should give an error.
    test_acct.withdrawl(300)
    # Withdrawls $100 from the account.
    test_acct.withdrawl(100)
    # Calculates interest over a 2 day period. then asks for user input.
    test_acct.calc_interest(2)
    # Corrects the spelling of the account holder's name.
    test_acct.update_name('John Smith')
    # Displays the account holder's name.
    test_acct.display_name()
    # Displays the account number.
    test_acct.display_acct_num()
    # Displays the account balance.
    test_acct.get_balance()
    # Tests the __str__ method. Should display the balance and interest.
    print(test_acct)

# Define the function and function arguments.
def yes_no_val(input_message, error_message):
    """Used to validate a yes or no response from the user.
    
    input_message = a string to be used as a prompt for input from the 
      user.
    error_message = a string that is displayed if the user's input is
      invalid.

    Prompts the user for an affirmative or negative response then checks 
    to make sure it's valid. if not, informs the user the input was not 
    valid and asksagain for a valid entry.

    Returns 'y' or 'n'.
    """
    # Initialize variables.
    entry = ''
    # Initialize a while loop.
    while True:
        # Request input from the user.
        entry = input(input_message)
        # Assigns the lowercase first letter of entry as the new value 
        # of answer.
        entry = entry[0].lower()
        # Evaluates if answer is 'y' or 'n' and if so breaks the loop.
        if entry == 'y' or entry == 'n':
            break
        else:
            # Display the error message
            print(error_message)
    # Returns the now validated value of the 'entry variable.
    return entry

# Calls the main method if the file is directly executed.
if __name__ == '__main__':
    test_bank_acct()
