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
