name = "Slawek"
number = len(name) * 8
print("Hello "  + name + ". Your lucky number is " + str(number))

# The same code but this time function had been used
def lucky_number(name):
    number = len(name) * 9
    print("Hello "  + name + ". Your lucky number is " + str(number))

lucky_number("Mike")    
