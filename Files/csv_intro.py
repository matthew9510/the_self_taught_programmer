import os
import csv

"""
    Notes:
    - Need to use the csv module to convert the file Object (csv_file) to a csv Object.
    - csv module has a method called writer that accepts a file object and a delimiter
    - if we don't specify new_line="" in open(), then we will have double spaces because csv.writerow() adds newline itself
    - csv stands for comma separated values

    declaration: def open(file_path, mode, newline="\r\n")
    declaration: def csv.writer(file_object, dialect='excel', **fmtparams):
    - **fmtparams is formatting parameters
    For more details see: https://docs.python.org/3.1/library/csv.html#dialects-and-formatting-parameters
"""

def read_csv(directory, filename):
    """
    Prints a friendly version of a csv file
    :param directory: location to create csv file
    :param filename: filename not including ".csv" file format
    """
    file = open(directory + os.sep + filename + ".csv")
    for row in csv.reader(file):
        print(" ".join(row))
    file.close()

def create_csv(directory, filename, content):
    """
    After creation the csv location and contents will be printed in a friendly way
    :param directory: location to create csv file
    :param filename: filename not including ".csv" file format
    :param content: a list of lists: outer list - rows; inner list - column data separated through elements;
    """
    file_path = directory + os.sep + filename + ".csv"
    file = open(file_path, "w", newline="")
    writer = csv.writer(file, delimiter=",")
    for row in content:
        writer.writerow(row)
    file.close()
    print(file_path)
    read_csv(directory, filename)

def append_to_csv(directory, filename, new_content):
    """
    After appending to csv file contents will be printed in a friendly way
    :param directory: location to create csv file
    :param filename: filename not including ".csv" file format
    :param content: a list of lists: outer list - rows; inner list - column data separated through elements;
    """
    file_path = directory + os.sep + filename + ".csv"
    file = open(directory + os.sep + filename + ".csv", mode="a", newline="")
    writer = csv.writer(file, delimiter=",")
    for row in new_content:
        writer.writerow(row)
    file.close()
    print(file_path)
    read_csv(directory, filename)

if __name__ == "__main__":
    current_directory = os.getcwd()
    filename = "first_csv"
    content = [[x**2 for x in range(y)] for y in range(1, 10)]
    create_csv(current_directory, filename, content)

    print("\nReading:" + current_directory + os.sep + filename)
    read_csv(current_directory, filename)

    new_content = [["Testing", "Python", "out"]]
    print("\nAppending to: " + current_directory + os.sep + filename)
    append_to_csv(current_directory, filename, new_content)