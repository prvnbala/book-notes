# import argv from sys module
from sys import argv

# assigns the two values in argv to script and filename variable
script, filename = argv

# resolve the filename is file system and assign it as a file to txt variable
txt = open(filename)

# prints the file on terminal
print("Here's your file %r:" %filename)
print(txt.read())

# prompts the user to type the file name again
print("Type the filename again:")
file_again = input("> ")

# loads the text file in memory and assigns it to txt_again variable as file
txt_again = open(file_again)

# print the contents of the file by reading it
print(txt_again.read())

txt.close()
txt_again.close()