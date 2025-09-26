import re

class NumberValidator:
    def __init__(self):
        self.phone = ''
        self.ssn = ''
        self.zip = ''

    def get_phone(self):
        self.phone = input('Please enter your phone number: ')

    def get_ssn(self):
        self.ssn = input('Please enter your social security number: ')

    def get_zip(self):
        self.zip = input('Please enter your zip code: ')

    def val_phone(self):
        pattern1 = r'[(]?\d\d\d[)]?[ -]?\d\d\d[ -]?\d\d\d\d'
        pattern2 = r''

        if re.fullmatch(pattern1, self.phone):
            print('Phone number format: Valid')
        else:
            print('Phone number format: Invalid')

    def val_ssn(self):
        pattern1 = r'\d\d\d-\d\d-\d\d\d\d'

        if re.fullmatch(pattern1, self.ssn):
            pass
        else:
            pass

    def val_zip(self):
        pattern1 = r'/d/d/d/d/d'

        if re.fullmatch(pattern1, self.zip):
            pass
        else:
            pass

def main():
    num_val = NumberValidator()

    num_val.get_phone()
    num_val.get_ssn()
    num_val.get_zip()

    num_val.val_phone()
    num_val.val_ssn()
    num_val.val_zip()

if __name__ == '__main__':
    # main()
    num_val = NumberValidator()
    num_val.get_phone()
    num_val.val_phone()