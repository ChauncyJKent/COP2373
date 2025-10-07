# ChauncyKent_08_csv

"""Contains the GradeBook class and the main function. The main 
function creates an instance of the GradeBook class and calls the 
appropriate methods in the correct order to allow the user to enter the 
names and grades of a specified number of students into the grade book 
which is saved to a csv file. The final method called then opens and 
reads that information from the csv file and displays it for the user 
in a tabular format.
"""

# imports the csv module.
import csv

# Defines the GradeBook class.
class GradeBook:
    """The GradeBook class is an object designed to collect the names 
    and grades of a specified number of students and store that data in 
    a csv file to be accessed later. The GradeBook class also contains 
    a method for later reading the data from the csv file and 
    displaying it for the user in a tabular format.
    """
    def __init__(self):
        # Stores the fieldnames, the name of the csv file, and the 
        # table data to write to the csv file.
        self.fieldnames = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']
        self.csv = 'grades.csv'
        self.table = []
    
    # Defines the build_table method.
    def build_table(self):
        """Prompts the user to indicate how many student records they 
        would like to enter by entering an integer. Then prompts the 
        user for each student's first name, last name, and their exam 
        scores. The data is then saved to an internal table to be 
        written to a csv later.
        """
        # Prompts the user for an integer to indicate the number of 
        # students being entered.
        num_students = int(input('How many students would you like to enter? '))
        # Loops a number of times equal to the number of students.
        for i in range(num_students):
            # Creates a dictionary to store the student's information.
            student = {}
            # Assigns each datapoint to the appropriate key.
            student[self.fieldnames[0]] = input("What is the student's first name? ")
            student[self.fieldnames[1]] = input("What is the student's last name? ")
            student[self.fieldnames[2]] = int(input("What was the student's grade on exam 1? "))
            student[self.fieldnames[3]] = int(input("What was the student's grade on exam 2? "))
            student[self.fieldnames[4]] = int(input("What was the student's grade on exam 3? "))
            # Adds the entered student record as a row in the table.
            self.table.append(student)

    # Defines the write_csv method.
    def write_csv(self):
        """Takes the table of information gathered by the build_table 
        method and writes it to a csv.
        """
        # Opens the csv in write mode saved to the variable name grades.
        with open(self.csv, 'w', newline='') as grades:
            # Initializes a DictWriter object with grades as the file 
            # to write to and self.fieldnames as the header names.
            writer = csv.DictWriter(grades, fieldnames=self.fieldnames)
            # Writes the first row to the csv with the header names.
            writer.writeheader()
            # Writes the data rows to the csv.
            writer.writerows(self.table)

    # Defines the read_csv method.
    def read_csv(self):
        """Reads the indicated csv and displays the information in a 
        tabular format.
        """
        # Creates a blank list to store the read information.
        table = []
        # Opens the csv in read mode with the variable name grades.
        with open(self.csv, 'r', newline='') as grades:
            # Initializes a reader object to read the file saved 
            # to the grades variable.
            reader = csv.reader(grades)
            # Loops through each row appending it to table.
            for row in reader:
                table.append(row)

        # Sets an initial width of 0.
        width = 0
        # Loops through each element of each list in the table and 
        # determines the greatest character count amongst all the 
        # elements.
        for row in table:
            for element in row:
                if len(str(element)) > width:
                    width = len(str(element))
            
        # Loops through each element of each list in the table and adds
        # spaces to the start of them so they are all the same width.
        for row in table:
            for element in row:
                print('%*s' % (width, element), end='')
            # Prints a newline character at the end of each row.
            print()

# Defines the main function.
def main():
    """Creates a GradeBook object and calls the build_table, write_csv, 
    and read_csv methods.
    """
    gb = GradeBook()
    gb.build_table()
    gb.write_csv()
    gb.read_csv()

# Calls the main method if the file is directly executed.
if __name__ == '__main__':
    main()
