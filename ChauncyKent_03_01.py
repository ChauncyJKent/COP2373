from functools import reduce

class ExpenseAnalyzer:
    def __init__(self):
        self.expenses = {}
        self.total_expense = 0
        self.highest_expense = 0
        self.highest_type = ''
        self.lowest_expense = float('inf')
        self.lowest_type = ''

    def _get_expense(self):
        invalid = True
        expense = 0

        while invalid:
            try:
                expense = float(input('Please enter the amount of your expense: '))
                invalid = False
            except ValueError:
                print('Please enter a number.')
                continue

        return expense
    
    def _get_type(self):
        invalid = True
        expense_type = ''

        while invalid:
            try:
                expense_type = input('Please enter the name of the expense: ')
                if expense_type in self.expenses.keys():
                    raise Exception()
                else:
                    invalid = False
            except:
                print('Please enter a unique expense name.')
                continue

        return expense_type
    
    def _update_records(self):
        expense = self._get_expense()
        expense_type = self._get_type()

        self.expenses[expense_type] = expense

    def collect_expenses(self):
        more = True
        while more:
            self._update_records()
            answer = ''
            invalid = True
            while invalid:
                answer = input('Are there more expenses? Y/N: ')
                if answer.lower() == 'y' or answer.lower() == 'n':
                    invalid = False
                else:
                    print('Please enter "Y" or "N".')
            if answer.lower() == 'n':
                more = False
            else:
                continue

    def analyze_expenses(self):
        self.total_expense = reduce(lambda x, y: x + y, self.expenses.values())

        self.highest_expense = reduce(lambda x, y: x if x > y else y, self.expenses.values())
        for key, value in self.expenses.items():
            if value == self.highest_expense:
                self.highest_type = key

        self.lowest_expense = reduce(lambda x, y: x if x < y else y, self.expenses.values())
        for key, value in self.expenses.items():
            if value == self.lowest_expense:
                self.lowest_type = key
    
    def display_analysis(self):
        print()
        print(f'The total of the expenses is: {self.total_expense}')
        print(f'The highest expense at {self.highest_expense} was: {self.highest_type}')
        print(f'The lowest expense at {self.lowest_expense} was: {self.lowest_type}')
        print()

def main():
    expenses = ExpenseAnalyzer()
    expenses.collect_expenses()
    expenses.analyze_expenses()
    expenses.display_analysis()

if __name__ == '__main__':
    main()
