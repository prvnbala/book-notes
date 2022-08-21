cars = 100 #defines number of cars available
space_in_a_car = 4.0 #numbers of seats available in each car
drivers = 30 #defines number of drivers available 
passengers = 90 #defines number of passengers available
cars_not_driven = cars - drivers #defines number of cars not driven due to driver unavailability
cars_driven = drivers #defines number of cars driven
carpool_capacity = cars_driven * space_in_a_car #defines the number of seats available for car pooling
average_passenger_per_car = passengers // cars_driven 

print('There are', cars, 'cars available.')
print('There are only', drivers, 'drivers available.')
print('There will be', cars_not_driven, 'empty cars today.')
print('We can transport', carpool_capacity, 'people today.')
print('We have', passengers, 'to carpool today.')
print('We need to put about', average_passenger_per_car, 'in each car.')
