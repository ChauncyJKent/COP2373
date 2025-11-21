# Imports the necessary modules for this project.
import csv
import numpy as np

# Defines the main method.
def main():
    """The main method serves as a single callable entity that 
    initializes and calls each piece of the program in the correct order 
    and also serves as a place to input any needed parameters.
    """
    # Creates an instance of the GradeBook class.
    gb = GradeBook()
    # Calls the import_csv method.
    gb.import_csv('grades.csv', True)

    # Calls the get_means method.
    gb.get_means()
    # Calls the get_medians method.
    gb.get_medians()
    # Calls the get_stds method (standard deviation, not other stds).
    gb.get_stds()
    # Calls the get_mins method.
    gb.get_mins()
    # Calls the get_max method.
    gb.get_maxs()
    # Calls the determine_passed method.
    gb.determine_passed()
    # Calls the determine_failed method.
    gb.determine_failed()
    # Calls the calc_pass_percent method.
    gb.calc_pass_percent()

    # Calls the display_all method.
    gb.display_all()

class GradeBook:
    """A class for importing grade data from a properly formatted csv 
    file. Contains everything needed to import the csv data, store it, 
    analyze it, and display it.
    """
    def __init__(self):
        # Initializes new instances of the GradeBook class with the 
        # following attributes:
        self.csv_data_array = []
        self.means = []
        self.medians = []
        self.stds = []
        self.mins = []
        self.maxs = []
        self.passed = [0, 0, 0, 0]
        self.failed = [0, 0, 0, 0]
        self.pass_percent = 0

    def import_csv(self, csv_file, print_rows=False, rows=3):
        """Imports the specified csv file and stores the data.

        args:
        csv_file = A string that is the name of the csv file to import.
        print_rows = A boolean value that indicates if you'd like to 
          print the first few rows of the csv file to see the structure. 
          Defaults to False.
        rows = An integer that represents the number of rows you'd like 
          to print. Defaults to 3.
        """
        # Opens the csv file.
        with open(csv_file, 'r', newline='') as csvfile:
            # Resets the csv file pointer to the top in case this is not 
            # the first use of import_csv.
            csvfile.seek(0)
            # Creates a csv.reader object using the open csv file.
            csvreader = csv.reader(csvfile)
            # Saves the header row to header (mostly used to skip the 
            # header row).
            header = next(csvreader)

            # Determines if printing the first few rows was requested.
            if print_rows:
                # Calls the _print_rows method.
                self._print_rows(rows, csvreader)
                # Resets the csv file point to the top.
                csvfile.seek(0)

            # Calls the _to_list method and saves the return to 
            # csv_data.
            csv_data = self._to_list(csvreader)
            # Calls the _to_array method and save the return to 
            # self.csv_data_array.
            self.csv_data_array = self._to_array(csv_data)

    def _print_rows(self, num_rows, csvreader):
        """prints the indicated number of rows from the top of the csv 
        file.

        args:
        num_rows = An integer representing the number of rows you'd like 
          to print.
        csvreader = A csv.reader object used to read the rows from the 
          csv file.
        """
        # Loops a number of times equal to num_rows.
        for i in range(num_rows):
            # Prints the next row from the csv.reader object.
            print(next(csvreader))

    def _to_list(self, csvreader):
        """Converts the csv data into a list of lists.

        args:
        csvreader = A csv.reader object used to read the rows from the 
          csv file.

        returns: 
        A list with sub-lists as elements.
        """
        # Creates the initial empty sub-lists.
        first_names = []
        last_names = []
        exam1 = []
        exam2 = []
        exam3 = []
        exams = []

        # Skips the header row.
        next(csvreader)
        # Loops through all the remaining rows in the csv.reader object.
        for row in csvreader:
            # Loops through the entries in the current row.
            for i in range(5):
                # Appends the entries to the appropriate lists depending 
                # on index number.
                if i == 0:
                    first_names.append(row[i])
                elif i == 1:
                    last_names.append(row[i])
                elif i == 2:
                    exam1.append(int(row[i]))
                    # Appends the grades to each exam and a combined 
                    # list of grades from all 3 exams.
                    exams.append(int(row[i]))
                elif i == 3:
                    exam2.append(int(row[i]))
                    exams.append(int(row[i]))
                else:
                    exam3.append(int(row[i]))
                    exams.append(int(row[i]))
        
        # Adds each sub-list as an element of the csv_data list.
        csv_data = [first_names, last_names, exam1, exam2, exam3, exams]

        # Returns the csv_data list.
        return csv_data
    
    def _to_array(self, list_of_lists):
        """Converts the list of lists to a list of numpy arrays.

        args:
        list_of_lists = A list with all list elements.

        returns:
        A list with numpy array elements.
        """
        # Creates an empty list.
        list_of_arrays = []

        # Loops through the lists in the supplied list of lists.
        for list in list_of_lists:
            # Converts each sub-list to an array.
            array = np.array(list)
            # Appends the sub-array to list_of_arrays.
            list_of_arrays.append(array)

        # Returns the list_of_arrays list.
        return list_of_arrays
    
    def get_means(self):
        """Finds the mean of each exam and all exams combined."""
        # Loops through self.csv_data_array, skipping the first two.
        for i in range(2, len(self.csv_data_array)):
            # Appends the mean of each exam and all exams to self.means.
            self.means.append(np.mean(self.csv_data_array[i]))

    def get_medians(self):
        """Finds the median of each exam and all exams combined."""
        # Loops through self.csv_data_array, skipping the first two.
        for i in range(2, len(self.csv_data_array)):
            # Appends the median of each exam and all exams to 
            # self.medians.
            self.medians.append(np.median(self.csv_data_array[i]))

    def get_stds(self):
        """Finds the standard deviation of each exam and all exams 
        combined.
        """
        # Loops through self.csv_data_array, skipping the first two.
        for i in range(2, len(self.csv_data_array)):
            # Appends the standard deviation of each exam and all exams 
            # to self.stds.
            self.stds.append(np.std(self.csv_data_array[i]))

    def get_mins(self):
        """Finds the minimum of each exam and all exams combined."""
        # Loops through self.csv_data_array, skipping the first two.
        for i in range(2, len(self.csv_data_array)):
            # Appends the minimum of each exam and all exams to 
            # self.mins.
            self.mins.append(np.min(self.csv_data_array[i]))

    def get_maxs(self):
        """Finds the maximum of each exam and all exams combined."""
        # Loops through self.csv_data_array, skipping the first two.
        for i in range(2, len(self.csv_data_array)):
            # Appends the maximum of each exam and all exams to 
            # self.maxs.
            self.maxs.append(np.max(self.csv_data_array[i]))

    def determine_passed(self):
        """Finds the number of passing grades for each exam and all 
        exams combined.
        """
        # Loops through self.csv_data_array, skipping the first two.
        for i in range(2, len(self.csv_data_array)):
            # Loops through each grade in each exam and all exams.
            for grade in self.csv_data_array[i]:
                # Checks if the grade is a passing grade.
                if grade >= 60:
                    # Increments the current element of self.passed.
                    self.passed[i-2] += 1

    def determine_failed(self):
        """Finds the number of failing grades for each exam and all 
        exams combined.
        """
        # Loops through self.csv_data_array, skipping the first two.
        for i in range(2, len(self.csv_data_array)):
            # Subtracts the number passed from the total and assigns it 
            # to the current element of self.failed.
            self.failed[i-2] = len(self.csv_data_array[i]) - self.passed[i-2]

    def calc_pass_percent(self):
        """Finds the pass percentage for all exams."""
        # Divides the total number passed by the total number of exams.
        self.pass_percent = self.passed[-1] / len(self.csv_data_array[-1])

    def display_all(self):
        """Displays the results of all the analysis."""
        # Lists the exam names to use as labels for the display.
        exam_nums = ['exam 1', 'exam 2', 'exam 3', 'all exams']

        # Loops through and prints the mean of each exam and all exams.
        for i in range(len(self.means)):
            print(f'The mean of {exam_nums[i]} is: {self.means[i]}')

        # Loops through and prints the median of each exam and all 
        # exams.
        for i in range(len(self.medians)):
            print(f'The median of {exam_nums[i]} is: {self.medians[i]}')

        # Loops through and prints the standard deviation of each exam 
        # and all exams.
        for i in range(len(self.stds)):
            print(
                f'The standard deviation of {exam_nums[i]} is: {self.stds[i]}'
                )

        # Loops through and prints the minimum of each exam and all 
        # exams.
        for i in range(len(self.mins)):
            print(f'The min of {exam_nums[i]} is: {self.mins[i]}')

        # Loops through and prints the maximum of each exam and all 
        # exams.
        for i in range(len(self.maxs)):
            print(f'The max of {exam_nums[i]} is: {self.maxs[i]}')

        # Loops through and prints the number of students who passed 
        # each exam.
        for i in range(len(self.passed) - 1):
            print(
                f'The number of students who passed {exam_nums[i]} is: '
                + f'{self.passed[i]}'
                )

        # Loops through and prints the number of students who failed 
        # each exam.
        for i in range(len(self.failed) - 1):
            print(
                f'The number of students who failed {exam_nums[i]} is: '
                + f'{self.failed[i]}'
                )

        # Prints the pass percentage of all exams.
        print(f'The pass percentage for all exams is: {self.pass_percent}')

# Calls the main method if the file is directly executed.
if __name__ == '__main__':
    main()
