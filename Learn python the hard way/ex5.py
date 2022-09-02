name = 'Praveen'
age = 26
height = 175 #in cms
weight = 73 #in kgs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

height_in_inches = height / 2.54;
weight_in_pounds = weight * 2;

print(f"Let's talk about {name}.")
print(f"He's {height} cms tall.")
print(f"He's {weight} kilograms heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
print(f"If I add {age}, {height}, and {weight} I'd get {age + height + weight}.")

print(f"Height in inches: {height_in_inches}")
print(f"Weight in pounds: {weight_in_pounds}")
