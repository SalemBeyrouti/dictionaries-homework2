sentence = input("Enter a sentence: ")

words = sentence.split()

print(words)

wordsappeared = {}

for word in words:
    if word in wordsappeared:
        wordsappeared[word] += 1 
    else:
        wordsappeared[word] = 1

print (wordsappeared)
