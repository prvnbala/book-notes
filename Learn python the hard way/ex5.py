name = 'Praveen'
age = 26
height = 175 #in cms
weight = 73 #in kgs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

height_in_inches = height / 2.54;
weight_in_pounds = weight * 2;

print("Let's talk about %s." %name)
print("He's %d cms tall." %height)
print("He's %d kilograms heavy." %weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." %(eyes, hair))
print("His teeth are usually %s depending on the coffee." %teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I'd get %d." %(age, height, weight, age + height + weight))

print("Height in inches: %f" %height_in_inches)
print("Weight in pounds: %f" %weight_in_pounds)
