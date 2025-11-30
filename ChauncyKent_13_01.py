# ChauncyKent_13_01

# Creates a database and populates it the names and populations from 10 
# citites in 2023, then simulates population growth/decline over the 
# next 20 years by applying randomly generated positive and negative 
# percentages within the bounds of recent growth/decline trends. This 
# simulated data is added to the database and the user is prompted to 
# select a city from the list of 10 resulting in the generation and 
# display of a line graph showing the simulated population growth over 
# the 20 year period.

# Imports the necessary modules to complete the project.
import sqlite3, random
import matplotlib.pyplot as plt

from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import MaxNLocator

# Defines the main function.
def main():
    # The main function executes the program code in the correct order
    # so that the program runs correctly.

    # Creates a PopGrowthSim object with the name population_CK.db.
    pgs = PopGrowthSim('population_CK.db')
    # Creates the database if it doesn't exist and connects to it.
    pgs.connect_db()
    # Creates a cursor object to allow execution of SQL commands.
    pgs.create_cursor()
    # Creates the table where the initial and simulated data will be 
    # saved.
    pgs.create_table('population_CK')

    # Add pop data.
    pop_data = [
        ['Jacksonville', 2023, 985843], 
        ['Miami', 2023, 455924], 
        ['Tampa', 2023, 403364], 
        ['Orlando', 2023, 320742], 
        ['St. Petersburg', 2023, 263553], 
        ['Hialeah', 2023, 221300], 
        ['Tallahassee', 2023, 202221], 
        ['Port St. Lucie', 2023, 245021], 
        ['Cape Coral', 2023, 224455], 
        ['Fort Lauderdale', 2023, 184255]
    ]
    pgs.add_much_data('population_CK', pop_data)

    # Simulate pop growth/decline for 20 years and add simulated data.
    pgs.much_sim_pop_change('population_CK', 2023, 20)

    # Create an empty list called city_list.
    city_list = []
    # Populate that list with the names of the 10 cities.
    for data in pop_data:
        city_list.append(data[0])
    # Display pop growth of one city (selected by user) with matplotlib.
    pgs.display_city_change(city_list, 'population_CK')

    # Close the connection to the database.
    pgs.disconnect_db()

# Defines the comma_format function.
def comma_format(x, pos):
    """Format numbers with comma separators for use as Matplotlib axis 
    labels.

    This function is intended to be used with 
    matplotlib.ticker.FuncFormatter. Matplotlib will supply two 
    arguments: the numeric tick value (x) and the tick position index 
    (pos). Only the value is used here; the position is accepted for 
    compatibility with FuncFormatter.

    args:
    x = A number representing the numeric tick value to format with 
      commas.
    pos = An int representing the tick position index along the axis. 
      (Not used in this function but required by FuncFormatter.)

    Returns:
    A string that is the comma-formatted string representation of the 
    number.
    """
    return f'{int(x):,}'

# Define the function and function arguments.
def str_val(input_message, error_message, valid_entry_dict):
    """Used to validate a string input from the user.
    
    input_message = a string to be used as a prompt for input from the 
      user.
    error_message = a string that is displayed if the user's input is
      invalid.
    valid_entry_dict = a dictionary of valid lowercase string responses
      keyed to expected outputs.

    Prompts the user for a specific string then checks to make sure it's
    valid. if not, informs the user the input was not valid and asks
    again for a valid entry.

    Returns a valid string.
    """
    # Initialize variables.
    valid_dict = valid_entry_dict
    # Initialize a while loop.
    while True:
        # Setup a try/except block to handle input errors.
        try:
            # Request input from the user and use it as a key in the
            # 'valid_dict' dictionary.
            entry = valid_dict[input(input_message).lower()]
            # If the input doesn't trigger the except clause, break the 
            # loop.
            break
        # Define what kind of error we're looking for.
        except KeyError:
            # Display the error message
            print(error_message)
    # Returns the now validated value of the 'entry variable.
    return entry

# Defines the PopGrowthSim class.
class PopGrowthSim:
    """This class is used to store population data from a number of 
    cities in an SQL database, simulate population growth/decline in 
    those cities, and display the simulated results as a line graph one 
    city at a time.
    """
    # Defines the __init__ method.
    def __init__(self, file_name):
        # Initializes an instance of the PopGrowthSim class with the 
        # following attributes.
        self.pop_db = file_name
        self.connection = None
        self.cursor = None

    # Defines the connect_db method.
    def connect_db(self):
        """Creates a database using self.pop_db as the name if it does 
        not yet exist and creates va connection object for the database.
        """
        self.connection = sqlite3.connect(self.pop_db) # Ex: 'file_name.db'

    # Defines the create_cursor method.
    def create_cursor(self):
        """Creates a cursor object for the connected database."""
        self.cursor = self.connection.cursor()

    # Defines the create_table method.
    def create_table(self, table_name):
        """Creates a table with the provided table name to store city 
        population data.

        args:
        table_name = A string to be used as the table name.            
        """
        # Creates the table with id, city, year, and population columns.
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            city TEXT NOT NULL, 
            year INTEGER NOT NULL, 
            population INTEGER NOT NULL
            )
        ''')

        # Saves your changes.
        self.connection.commit()

    # Defines the add_data method.
    def add_data(self, table_name, data):
        """Adds a list of preformatted data to the indicated table.

        args:
        table_name = A string that is the name of the table to be edited.
        data = A list of preformated data (city name, year, population) 
          to insert into the table.
        """
        # Adds the data to the table.
        self.cursor.execute(f'''
        INSERT INTO {table_name} (city, year, population)
            VALUES (?, ?, ?)
        ''', (data[0], data[1], data[2]))

        # Saves your changes.
        self.connection.commit()

    # Defines the add_much_data method.
    def add_much_data(self, table_name, much_data):
        """Takes in a list of lists and feeds it, a list at a time to 
        the add_data method.

        args:
        table_name = A string that is the name of the table to be edited.
        data = A list of lists of preformated data (city name, year, 
          population) to insert into the table.
        """
        for data in much_data:
            self.add_data(table_name, data)

    # Defines the sim_pop_change method.
    def sim_pop_change(self, table_name, year):
        """Pulls the population data for all the cities in the indicated 
        table, generates simulated population changes for each, updates 
        them, and adds the new data to the table.

        args:
        table_name = A string that is the name of the table to be edited.
        year = An int representing the year you want pop data for.
        """
        # Querries the table for the population data.
        self.cursor.execute(f'''
        SELECT city, year, population FROM {table_name}
            WHERE year = {year}
        ''')
        # Collects the querried data into a list.
        rows = self.cursor.fetchall()

        # Loops through the list of data to update it.
        for city, yr, pop in rows:
            # generates a random population change percentage.
            pop_change = random.randint(-10, 30)

            # Updates the year for the new data.
            new_year = yr + 1
            # Updates the population for the new data.
            new_pop = pop + int(pop * (pop_change / 100))

            # Collects the new data into a preformatted list.
            data = [city, new_year, new_pop]
            # Adds the new data to the table.
            self.add_data(table_name, data)

        # Saves your changes.
        self.connection.commit()

    # Defines the much_sim_pop_change method.
    def much_sim_pop_change(self, table_name, starting_year, num_years):
        """Loops a number of times equal to num_years calling 
        sim_pop_change on each run.

        args:
        table_name = A string that is the name of the table to be edited.
        starting_year = An int representing the first year you want pop 
          data for.
        num_years = An integer indicating the number of years to 
          simulate population changes for.
        """
        for j in range(num_years):
            self.sim_pop_change(table_name, starting_year + j)

    # Defines the display_city_change method.
    def display_city_change(self, city_list, table_name):
        """Prompts the user to select a city from those in the table, 
        and displays the simulated population change over a 20 year 
        period.

        args:
        city_list = A list of the cities in the table.
        table_name = A string that is the name of the table to be edited.
        """
        # Prints the city list for the user to make a selection.
        for i in range(len(city_list)):
            print(i + 1, city_list[i])
        # Uses the str_val function to validate the user's response and 
        # save it as the value of chosen_city.
        chosen_city = str_val(
            'Please select a city from the list to display data. ', 
            "That's not an option. Please enter a for one of the cities.", 
            {
            '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, 
            '6': 6, '7': 7, '8': 8, '9': 9, '10': 10
            }
            )
        # Uses the int value of chosen_city to convert it to a city name.
        chosen_city = city_list[chosen_city - 1]

        # Querries the table for all data for the chosen city.
        self.cursor.execute(f'''
        SELECT * FROM {table_name}
            WHERE city = ?
        ''', (chosen_city,))
        # Collects the querried data into a list.
        pops = self.cursor.fetchall()

        # Creates an empty list to collect years.
        years = []
        # Loops through pops, adding the years to years and redefining 
        # each element of pops to just the city's population.
        for i in range(len(pops)):
            years.append(pops[i][2])
            pops[i] = pops[i][-1]

        # Creates a line graph using years as the x-axis labels and pops 
        # as the y-axis labels.
        plt.plot(years, pops)
        # Labels the x-axis as Years.
        plt.xlabel('Years')
        # Enforces only integer years as labels (no 2022.5).
        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        # Labels the y-axis as Population.
        plt.ylabel('Population')
        # Formats the population numbers with comma seperators.
        plt.gca().yaxis.set_major_formatter(FuncFormatter(comma_format))
        # Sets the graph title as chosen_city Population Over 20 Years.
        plt.title(f'{chosen_city} Population Over 20 Years')
        # Displays the graph.
        plt.show()

    # Defines the disconnect_db method.
    def disconnect_db(self):
        """Closes the connection to the database."""
        self.connection.close()

# Calls the main method if the file is directly executed.
if __name__ == '__main__':
    main()
