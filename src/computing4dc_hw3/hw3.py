# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

def car_at_light(light):
    if light.casefold() == "red":
        return "stop"
    elif light.casefold() == "green":
        return "go"
    elif light.casefold() == "yellow":
        return "wait"
    else:
        return "Undefined instruction for color: " + str(light)
# test car_at_light    
print(car_at_light("RED"))

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

def safe_subtract(a, b):
    try:
        return a - b
    except TypeError:
        return None
    except Exception as error:
        return f"Error: {error}"
    
# Test safe_subtract   
print(safe_subtract(3,1))


# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that return the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that takes the path to the file as an argument
# and reads the file making sure to use to handle the fact
# that it might not exist. 
#


# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them

### (a)
# The code block seems to be interested in the "Double sum" but the variable elem is being added to "total_double_sum" instead of the variable "double"

total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double

### (b)
# In the original version strings is being reassigned to the value of string + string, i.e., "I I" when it should append each new string onto the variable "strings"
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = strings+"_"+string

### (c) Careful!
#J will always be >0 so this while loop will never end.
j=10
while j > 0:
   j -= 1

### (d)
#Since we are working with multiplication, the initialized value for productory should be 1. If it is zero, the product will always be 0
productory = 1
for elem in [1, 5, 25]:
    productory *= elem

