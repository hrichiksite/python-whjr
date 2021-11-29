introString = input("Enter a string: ")
wordsCount = introString
wordsCount = list(wordsCount)
wordsCount = len(wordsCount)
print(wordsCount)
charCount = 0
wordCount = 1

for i in introString:
    charCount += 1
    if i == " ":
        wordCount += 1

print("The number of words in the string is:", wordCount)
print("The number of characters in the string is:", charCount)