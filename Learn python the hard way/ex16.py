from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Truncating and opening the file...")
target = open(filename, 'w')

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to file.")

contents = "%s\n%s\n%s\n" %(line1, line2, line3)
target.write(contents)

print("And finally, we close it.")
target.close() #close operation only saves the file in write mode

print('.' * 80)
print("Now I'm reading back the file contents.")
fileToRead = open(filename)
print(fileToRead.read())
fileToRead.close()