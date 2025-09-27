# ChauncyKent_06_01

"""Contains the NumberValidator class and the main function. The main 
function creates an instance of the NumberValidator class and calls the 
appropriate methods in the correct order to collect the user's phone 
number, social security number, and zip code, and determine if the 
format of those numbers is valid or not. Once that determination is 
made, the results are displayed.
"""

# imports the re module.
import re

# Defines the Number Validator class.
class NumberValidator:
    """The NumberValidator class is an object used to collect, store 
    and validate phone numbers, social security numbers, and zip codes. 
    This version of the class is set up to validate the format of these 
    numbers as used in America. For other regions, the patterns will 
    need to be updated.
    """
    def __init__(self):
        # Stores the collected phone numbers, social security numbers, 
        # and zip codes.
        self.phone = ''
        self.ssn = ''
        self.zip = ''

    # Defines the get_phone method.
    def get_phone(self):
        """Collects and stores a phone number from the user."""
        self.phone = input('Please enter your phone number: ')

    # Defines the get_ssn method.
    def get_ssn(self):
        """Collects and stores a social security number from the user."""
        self.ssn = input('Please enter your social security number: ')

    # Defines the get_zip method.
    def get_zip(self):
        """Collects and stores a zip code from the user."""
        self.zip = input('Please enter your zip code: ')

    # Defines the val_phone method.
    def val_phone(self):
        """Compares the format of the stored phone number against valid 
        formats and displays "Valid" is acceptable and "Invalid" 
        otherwise.
        """
        # Defines the valid phone number formats. While it is possible
        # to cover multiple formats with fewer patterns, multiple 
        # patterns were used for simplicity and readability.
        pattern1 = r'^\(\d{3}\) \d{3}-\d{4}'
        pattern2 = r'^\d{3}-\d{3}-\d{4}'
        pattern3 = r'^\d{3} \d{3} \d{4}'
        pattern4 = r'^\d{10}'

        # Checks each pattern for a match. If none is found displays 
        # "Invalid."
        if re.fullmatch(pattern1, self.phone):
            print('Phone number format: Valid')
        elif re.fullmatch(pattern2, self.phone):
            print('Phone number format: Valid')
        elif re.fullmatch(pattern3, self.phone):
            print('Phone number format: Valid')
        elif re.fullmatch(pattern4, self.phone):
            print('Phone number format: Valid')
        else:
            print('Phone number format: Invalid')

    # Defines the val_ssn method.
    def val_ssn(self):
        """Compares the format of the stored social security number 
        against valid formats and displays "Valid" is acceptable and 
        "Invalid" otherwise.
        """
        # Defines the valid social security number formats. While it is 
        # possibleto cover multiple formats with fewer patterns, 
        # multiple patterns were used for simplicity and readability.
        pattern1 = r'^\d{3}-\d{2}-\d{4}'
        pattern2 = r'^\d{9}'

        # Checks each pattern for a match. If none is found displays 
        # "Invalid."
        if re.fullmatch(pattern1, self.ssn):
            print('Social security number format: Valid')
        elif re.fullmatch(pattern2, self.ssn):
            print('Social security number format: Valid')
        else:
            print('Social security number format: Invalid')

    # Defines the val_zip method.
    def val_zip(self):
        """Compares the format of the stored zip code against valid 
        formats and displays "Valid" is acceptable and "Invalid" 
        otherwise.
        """
        # Defines the valid zip code formats. While it is possible to 
        # cover multiple formats with fewer patterns, multiple patterns 
        # were used for simplicity and readability.
        pattern1 = r'^\d{5}'
        pattern2 = r'^\d{5}-\d{4}'

        # Checks each pattern for a match. If none is found displays 
        # "Invalid."
        if re.fullmatch(pattern1, self.zip):
            print('Zip code format: Valid')
        elif re.fullmatch(pattern2, self.zip):
            print('Zip code format: Valid')
        else:
            print('Zip code format: Invalid')

# Defines the main method.
def main():
    """Creates a NumberValidator object and calls the number collection 
    and validation methods in the correct order.
    """
    # Creates an instance of the NumberValidator class.
    num_val = NumberValidator()

    # Calls the get_phone method to collect the user's phone number.
    num_val.get_phone()
    # Calls the get_ssn method to collect the user's social security 
    # number.
    num_val.get_ssn()
    # Calls the get_zip method to collect the user's zip code.
    num_val.get_zip()

    # Calls the val_phone method to validate the format of the user's 
    # phone number.
    num_val.val_phone()
    # Calls the val_ssn method to validate the format of the user's 
    # social security number.
    num_val.val_ssn()
    # Calls the val_zip method to validate the format of the user's 
    # zip code.
    num_val.val_zip()

# Calls the main method if the file is directly executed.
if __name__ == '__main__':
    main()