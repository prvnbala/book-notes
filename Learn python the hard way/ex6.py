# creates a string variable with format character
x = "There are %d types of people." % 10

#creates a string variable
binary = "binary"

#creates a string variable
do_not = "don't"

#creates a string variable with format multiple characters
y = "Those who know %s and those who %s." %(binary, do_not)

# prints the strings to console
print(x)
print(y)

# prints sentence with raw string format character 
print("I said: %r." %x)

# prints sentence with normal string format character
print("I also said: '%s'." %y)

# creates a boolean variable
hilarious = False

# creates a string with raw string format character
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the variable with arguments
print(joke_evaluation % hilarious)

# create string in two parts
w = "This is the left side of..."
e = "a string with a right side."

# print two string by concatinating them
print(w + e)