# Type-casting is the process of converting the type of a variable
# The following are the current types of the variables we've created above
# python LessonTestOutput/L1-ViewNewTypes.py
x = 1
newFloat = 2.5
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
