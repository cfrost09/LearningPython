# This is a single line comment
# Comments are used to make notes on the next lines of code but where possible, code should be self-commenting by using proper variable names
# For the sake of these lessons we'll use lots of comments

'''
Multiline comment
Not sure why it isn't using the same color for syntax hylighting
'''

"""
Double quotes may also be
used for multiline comments
"""

# Creating and assigning a new variable
x = 1

# Testing our new variable
print(x)

# Wrong way to test new variable
print("x")

# Run above code from terminal using: python LessonTestOutput/L1-Int.py

# Mathematical operations can be run on numbers and sent to a function or stored in a new variable
a = 4
b = 2
add = a + b
divide = a / b
multiply = a * b
subtract = a - b

print(a)
print(b)
print(add)
print(divide)
print(multiply)
print(subtract)

# print() is actually a function taking 1 variable so we can do the math right in the function call
# python LessonTestOutput/L1-PrintMathOperations.py
print(a * b)

# The above is of type int, short for integer
# Other types include:
# float (basically a number which includes a decimal)

myFloat = 2.0

# string (a string of characters)

myString = "Bacon Pancakes"

print (myFloat)
print (myString)

# Run above code from terminal using: python LessonTestOutput/L1-FloatAndString.py

# We can view the type of a variable like so:
# python LessonTestOutput/L1-PrintVarTypes.py

newFloat = 2.5
print (type(x))
print (type(newFloat))
print (type(myString))

# Type-casting is the process of converting the type of a variable
# The following are the current types of the variables we've created above
# python LessonTestOutput/L1-ViewNewTypes.py

floatToInt = int(newFloat)
intToFloat = float(x)
y = "235"
stringToInt = int(y)

# Types before conversion
print(type(newFloat))
print(type(x))
print(type(y))

# Types after conversion
# python LessonTestOutput/L1-CastedTypes.py
print(type(floatToInt))
print(type(intToFloat))
print(type(stringToInt))

# Floats converted to ints with be rounded down or floored
print(floatToInt)

# Some functions are built to handle inputs of different types
# For example the previous code we ran , print(a * b), automatically converted a number to a string
# The + function will do mathematical operations if all variables are numbers
# In the case of both an int and a float being supplied the result will be a float

d = 3
e = 2.5

print(d + e)

# If 1 variable is a string and another is a number we will need to cast the number to a string
# python LessonTestOutput/L1-AutoCastingInFunctions.py

print("I like " + str(d) + " slices of bacon in my Brandon soup")

# Both types of quotes can be used to define strings

singleQuoteString = 'Hi there.'
doubleQuoteString = "What you doing in my waters?"

print(singleQuoteString)
print(doubleQuoteString)

# We sometimes might want to print a quotation however

quoteInString = "I couldn't define this string in single quotes or it wouldn't work."

print(quoteInString)

# If we need to use both types of quotes in a string or we just prefer to stay
# consistent in which we use we can warn the compiler of a special character with
# an escape character \
# python LessonTestOutput/L1-QuotesAndStrings.py

escapeQuoteString = "Mike's furnace once told me, \"It's too damn cold in here for me to turn on\"."

print escapeQuoteString

# A list is another type which stores a list of other variables
# Types within a list don't need to match and other lists can even be stored in lists

# Define an empty list
emptyList = []

# Define a prepopulated list
populatedList = [1,2.5,"tickle me elmo"]

# Accessing list elements starting with 0
print(populatedList[0])
print(populatedList[1])
print(populatedList[2])

# The last list element is located at len()-1
# len() is a length function that is available with every list
# We use -1 because the length doesn't account for the fact that lists start storing at location 0
# python LessonTestOutput/L1-Lists.py
print(populatedList[len(populatedList) - 1])

# Each step in the above line can also be done separately
populatedListLength = len(populatedList)
populatedListLastElementLocation = populatedListLength -1
populatedListLastElement = populatedList[populatedListLastElementLocation]
print populatedListLastElement
