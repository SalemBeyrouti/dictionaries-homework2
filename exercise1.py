dict1 = {}

print("Enter a key-value pair in the 1st dictionary: ")

while "true":
    key1 = input("Enter a key for the 1st dictionary: (type done when you wanna stop)")
#thought it was nice adding the comment done when the user wanna stops
    if key1 == 'done':
        break
    value = int(input(f"Enter a value for '{key1}: "))

dict2 = {}

print("Enter a value-key pair for the 2nd dictionary: ")

while "true":
    key2 = input("Enter a key for the 2nd dictionary: (type done when you wanna stop)")

    if key2 == 'done':
        break
    value = int(input(f"Enter a value for '{key2}': "))
    