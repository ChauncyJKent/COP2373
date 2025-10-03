import csv

class ClassGradeBook:
    def __init__(self):
        self.fieldnames = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']
        self.table = []
        self.csv = 'grades.csv'
        self.db = ''
    
    def build_table(self):
        num_students = int(input('How many students would you like to enter? '))
        for i in range(num_students):
            student = {}
            student[self.fieldnames[0]] = input("What is the student's first name? ")
            student[self.fieldnames[1]] = input("What is the student's last name? ")
            student[self.fieldnames[2]] = int(input("What was the student's grade on exam 1? "))
            student[self.fieldnames[3]] = int(input("What was the student's grade on exam 2? "))
            student[self.fieldnames[4]] = int(input("What was the student's grade on exam 3? "))
            self.table.append(student)

    def write_csv(self):
        with open(self.csv, 'w', newline='') as grades:
            writer = csv.DictWriter(grades, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.table)

    def read_csv(self):
        table = []
        with open(self.csv, 'r', newline='') as grades:
            reader = csv.reader(grades)
            for row in reader:
                table.append(row)

        width = 0
        for row in table:
            for element in row:
                if len(str(element)) > width:
                    width = len(str(element))
            
        for row in table:
            for element in row:
                print('%*s' % (width, element), end='')
            print()

def main():
    gb = ClassGradeBook()
    gb.build_table()
    gb.write_csv()
    gb.read_csv()

if __name__ == '__main__':
    main()
