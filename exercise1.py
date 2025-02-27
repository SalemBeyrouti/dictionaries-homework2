dict1 = {}

print("Enter a key-value pair in the 1st dictionary: ")

while True:
    key1 = input("Enter a key for the 1st dictionary (type done when you wanna stop): ")
#thought it was nice adding the comment done when the user wanna stops
    if key1 == 'done':
        break
    value = int(input(f"Enter a value for '{key1}: "))

    dict1[key1]=value

# print (dict1)

dict2 = {}

print("Enter a value-key pair for the 2nd dictionary: ")

while True:
    key2 = input("Enter a key for the 2nd dictionary (type done when you wanna stop): ")

    if key2 == 'done':
        break
    value = int(input(f"Enter a value for '{key2}': "))

    dict2[key2]=value

# print (dict2)

mergeddictionaries = {**dict1, **dict2}

#after several searches i thought this was the optimal formula and the easiest to mnemorise

print ("The merged dictionary is: ", mergeddictionaries)
