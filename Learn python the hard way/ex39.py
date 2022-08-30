def print_line():
    print("-" * 10)

# create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities ={
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print_line()
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])

# print some states 
print_line()
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print_line()
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

# print every state abbreviation
print_line()
for state, abbreviation in states.items():
    print("%s is abbreviated as %s." %(state, abbreviation))

# print every city in state
print_line()
for abbreviation, city in cities.items():
    print("%s has the city %s." %(abbreviation, city))

# now do both at the same time
print_line()
for state, abbreviation in states.items():
    print("%s state is abbreviated %s and has city %s." %(state, abbreviation, cities[abbreviation]))

print_line()
# safely get an abbreviation by state that might not be there
state = states.get("Texas", None)

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', "Does Not Exist")
print("The city for the state 'TX' is %s." %city)



# use collections.OrderedDict for maintaining order in dictionary
