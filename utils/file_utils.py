from csv import reader 

def read_names_from_csv(input_filepath):
    """
    Function to open a CSV file and process a list of names
    :param input_filepath: string that indicates the file to read and process
    :return: a list where each of its elements corresponds to a name
    """

    with open(input_filepath, "r", newline="") as file:
        names = reader(file)
        return [row[0] for row in names if row]