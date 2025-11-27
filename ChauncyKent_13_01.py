import sqlite3
import matplotlib.pyplot as plt

class PopGrowthSim:
    def __init__(self, file_name):
        self.pop_db = file_name
        self.connection = None
        self.cursor = None

    def connect_db(self):
        self.connection = sqlite3.connect(self.pop_db) # Ex: 'file_name.db'

    def create_cursor(self):
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS population_CK (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            city TEXT NOT NULL, 
            year INTEGER NOT NULL, 
            population INTEGER NOT NULL
            )
        ''')

        self.connection.commit()

    def disconnect_db(self):
        self.connection.close()
