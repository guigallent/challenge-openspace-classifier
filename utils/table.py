class Seat:
    
    def __init__(self, occupant = "", free = True):
        """
        Method that creates a new seat. 
        :param occupant: A string that contains the name of the person sitting. By default it is empty.
        :param free: A boolean that displays whether the seat is free (True, by default) or not (False).
                     If the user introduces a name, it will change to False automatically.
        """

        self.occupant = occupant
        self.free = free
        if self.occupant != "":
            self.free = False

    def set_occupant(self, name):
        """
        Method that sits an occupant to the seat only if the seat is free. 
        :param name: A string that contains the name of the person that will seat.
        If the seat is already taken, the method will return a warning message. 
        """

        if self.free:
            self.occupant = name
            self.free = False
        else:
            return("Seat occupied!")

    def remove_occupant(self, occupant):
        """
        Method that removes an occupant from their seat. 
        :param occupant: A string that contains the name of the person that you want to remove from their seat.
        If the seat is already free, the method will return a warning message. 
        """
        if self.free:
            return("The seat is already free!")
        else:
            leaving_occupant = self.occupant
            self.occupant = ""
            self.free = True
            return leaving_occupant

class Table:
    def __init__(self, capacity = 4):
        """
        Method that creates a new table with a number of seats. 
        :param capacity: it sets the number of sits at the table (by default 4)
        """
        
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]

    def has_free_spot(self):
        """
        Method that detects whether there is a free sit at the table. 
        :return: a boolean that is True if there is a free seat and False if there is not.
        """
        is_free = False
        for seat in self.seats:
            if seat.free:
                is_free = True
        return is_free
    
    def assign_seat(self, name):
        """
        Method that assigns a free sit at the table. 
        :param name: a string with the name that will occupy the seat
        :return: a string that returns the name of the occupant.
        """
        for seat in self.seats:
            if seat.free:
                return seat.set_occupant(name)
    
    def left_capacity(self):
        """
        Method that counts the number of free seats at a table. 
        :return: an int with the number of free sits left.
        """
        free_seats = 0
        for seat in self.seats:
            if seat.free:
                free_seats += 1
        return free_seats