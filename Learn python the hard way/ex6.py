# creates a string variable with format character
types_of_people = 10
x = f"There are {types_of_people} types of people."

#creates a string variable
binary = "binary"

#creates a string variable
do_not = "don't"

#creates a string variable with format multiple characters
y = f"Those who know {binary} and those who {do_not}."

# prints the strings to console
print(x)
print(y)

# prints sentence with raw string format character 
print(f"I said: '{x}'")

# prints sentence with normal string format character
print(f"I also said: '{y}'")

# creates a boolean variable
hilarious = False

# creates a string with raw string format character
joke_evaluation = "Isn't that joke so funny?! {}"

# prints the variable with arguments
print(joke_evaluation.format(hilarious))

# create string in two parts
w = "This is the left side of..."
e = "a string with a right side."

# print two string by concatinating them
print(w + e)