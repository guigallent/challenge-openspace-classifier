from random import shuffle
from utils.table import Table

class OpenSpace:
    
    def __init__(self, number_of_tables = 6):
        """
        Method that creates a new space with tables. 
        :param number_of_tables: it sets the number of tables the new space will have (6 by default).
        """

        self.number_of_tables = number_of_tables
        self.tables = [Table() for i in range(number_of_tables)]

    def organize(self, names):
        """
        Method that randomly distributes names in different tables. 
        :param names: a string containing all the names of the people to sit in the tables.
        :return: a string indicating the shuffle has been done.
        """

        shuffle(names)
        table_number = 0
        for name in names:
            if self.tables[table_number].left_capacity() != 0:
                self.tables[table_number].assign_seat(name)
            else:
                table_number += 1
                self.tables[table_number].assign_seat(name)
        return("Shuffle done!")
    
    def display(self):
        """
        Method that displays the distribution of names by table. 
        """

        table_count = 1
        for table in self.tables:
            print(f"Table {table_count}:")
            for seat in table.seats:
                print(seat.occupant)
            table_count += 1
            print("\n")

    def store(self, filename):
        """
        Method that saves the distribution of names by table in a file. 
        :param filename: a string containing the name of the file the user wants to save the distribution in.
        """

        with open(filename, "w") as file:
            table_count = 1
            for table in self.tables:
                file.write(f"Table {table_count}:\n")
                for seat in table.seats:
                    file.write(f"{seat.occupant}\n")
                table_count += 1
                file.write("\n")
        print(f"File saved as {filename}")

