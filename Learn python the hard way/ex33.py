def getListOfWholeNumbersWithCustomSpacing(upper_limit, spacing):
    numbers = []
    for i in range(0, upper_limit, spacing):
        #print("At the top i is %d" %i)
        numbers.append(i)
        #i += spacing
        #print("Numbers now:", numbers)
        #print("At the bottom i is %d" %i)
    
    return numbers


numbers = getListOfWholeNumbersWithCustomSpacing(10, 2)
print("The numbers:", numbers)

for num in numbers:
    print(num)