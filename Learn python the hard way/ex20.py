# import argv into the script from the sys module
from sys import argv

# assign the two values in argv list to script and input_file
script, input_file = argv

# function to print all the line in the passed file
def print_all(f):
    # prints the contents of the file by reading it
    print(f.read())
    

# function to move the cursor on file to the beginning of the file
def rewind(f):
    # seek(0) returns the cursor to the beginning of the file to read it again
    f.seek(0)

# function to print the line where the cursor is present
def print_a_line(line_count, f):
    # prints the line number passed with the a single line from the file.
    print(line_count, f.readline(), end = '')


# opens the file and assigns an file object to current_file variable.
current_file = open(input_file)

# print a simple message for the user.
print("First let's print the whole file: \n")

# print all the contents of the file.
print_all(current_file)

# print a simple message for the user.
print("Now let's rewind, kind of like a tape.")

# rewind the cursor to the beginning of the file.
rewind(current_file)

# print a simple message to the user. 
print("Let's print three lines.")

# initialize a current_line variable with value 1.
current_line = 1
# call the function to print 1st line
print_a_line(current_line, current_file)

# increment the current_line variable value
current_line += 1
# call the function to print the 2nd line
print_a_line(current_line, current_file)

# increment the current_line variable value
current_line += 1
# call the function to print the 3rd line
print_a_line(current_line, current_file)