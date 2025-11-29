import sqlite3, random
import matplotlib.pyplot as plt

from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import MaxNLocator

def main():
    pgs = PopGrowthSim('population_CK.db')
    pgs.connect_db()
    pgs.create_cursor()
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
    pgs.add_much_data(pop_data)

    # Simulate pop growth/decline for 20 yrs.
    # Add simulated pop data
    pgs.much_sim_pop_change('population_CK', 2023, 20)

    # Display pop growth of one city (selected by user) using matplotlib.
    city_list = []
    for data in pop_data:
        city_list.append(data[0])
    pgs.display_city_change(city_list, 'population_CK')

    pgs.disconnect_db()

def comma_format(x, pos):
    return f'{int(x):,}'

class PopGrowthSim:
    def __init__(self, file_name):
        self.pop_db = file_name
        self.connection = None
        self.cursor = None

    def connect_db(self):
        self.connection = sqlite3.connect(self.pop_db) # Ex: 'file_name.db'

    def create_cursor(self):
        self.cursor = self.connection.cursor()

    def create_table(self, table_name):
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            city TEXT NOT NULL, 
            year INTEGER NOT NULL, 
            population INTEGER NOT NULL
            )
        ''')

        self.connection.commit()

    def add_data(self, data):
        self.cursor.execute('''
        INSERT INTO population_CK (city, year, population)
            VALUES (?, ?, ?)
        ''', (data[0], data[1], data[2]))

        self.connection.commit()

    def add_much_data(self, much_data):
        for data in much_data:
            self.add_data(data)

    def sim_pop_change(self, table_name, year):
        self.cursor.execute(f'''
        SELECT city, year, population FROM {table_name}
            WHERE year = {year}
        ''')
        rows = self.cursor.fetchall()

        for city, yr, pop in rows:
            pop_change = random.randint(-10, 30)

            new_year = yr + 1
            new_pop = pop + int(pop * (pop_change / 100))

            data = [city, new_year, new_pop]
            self.add_data(data)

        self.connection.commit()

    def much_sim_pop_change(self, table_name, starting_year, num_years):
        for j in range(num_years):
            self.sim_pop_change(table_name, starting_year + j)

    def display_city_change(self, city_list, table_name):
        for i in range(len(city_list)):
            print(i + 1, city_list[i])
        chosen_city = input('Please select a city from the list to display data. ')
        chosen_city = city_list[int(chosen_city) - 1]
        self.cursor.execute(f'''
        SELECT * FROM {table_name}
            WHERE city = ?
        ''', (chosen_city,))
        pops = self.cursor.fetchall()
        years = []
        for i in range(len(pops)):
            years.append(pops[i][2])
            pops[i] = pops[i][-1]

        plt.plot(years, pops)
        plt.xlabel('Years')
        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.ylabel('Population')
        plt.gca().yaxis.set_major_formatter(FuncFormatter(comma_format))
        plt.title(f'{chosen_city} Population over 20 Years')
        plt.show()

    def disconnect_db(self):
        self.connection.close()

if __name__ == '__main__':
    main()
