sentence = input("Enter a sentence: ")

if not sentence:
    print("You didnt enter a sentence try again")

#Tried adding an empty sentence didnt work

words = sentence.split()

print(words)

wordsappeared = {}

for word in words:
    if word in wordsappeared:
        wordsappeared[word] += 1 
    else:
        wordsappeared[word] = 1

print (wordsappeared)
