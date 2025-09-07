import functools

class ExpenseAnalyzer:
    def __init__(self):
        self.expenses = {}
        self.amount_list = []

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
            except:
                print('Please enter a unique expense name.')
                continue

        return expense_type
    
    def update_records(self):
        expense = self._get_expense()
        expense_type = self._get_type()

        self.expenses[expense_type] = expense
        self.amount_list.append(expense)

