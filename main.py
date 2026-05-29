from utils.openspace import OpenSpace
from utils.file_utils import read_names_from_csv

def main():
    """
    The function creates imports the list of names from the file assigned to input_filepath.
    An Openspace containing 6 tables with 4 empty seats each is then created.
    Organize will take our list of names above and assign random seats to each student.
    Store will save the seat distribution in the file output.csv.
    Display will show us in the terminal how seats are organized.
    """

    input_filepath = "new_colleagues.csv"
    output_filename = "output.csv"

    # Creates a list that contains all the colleagues names
    names = read_names_from_csv(input_filepath)

    # create an OpenSpace()
    open_space = OpenSpace()

    # assign a colleague randomly to a table
    open_space.organize(names)

    # save the seat assigments to a new file
    open_space.store(output_filename)

    # display assignments in the terminal
    open_space.display()

if __name__ == "__main__":
    main()