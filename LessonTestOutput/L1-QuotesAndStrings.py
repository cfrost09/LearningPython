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
