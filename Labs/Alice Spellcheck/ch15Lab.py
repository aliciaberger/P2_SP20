'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

line_number = 0
def binary_search(key, list, line_number):
    found = False
    lower_bound = 0
    upper_bound = len(list) - 1
    while lower_bound <= upper_bound and not found:
        middle_possition = (upper_bound + lower_bound) // 2
        if list[middle_possition] < key:
            lower_bound = middle_possition + 1
        elif list[middle_possition] > key:
            upper_bound = middle_possition - 1
        else:
            found = True
    if found == True:
        good = 0
    else:
        print(key, "was to found in the dictonary but is found in line", line_number, "of Alice")



line_number = 0
def linear_search(key, my_list, list2):
    i = 0
    while i < (len(my_list) - 1) and key.upper() != my_list[i]:
        i += 1

    if i < len(my_list) - 1:
        return True
    else:
        print(key, "was not found in the dictonary but is found in line", line_number, "of Alice")

alice_list = []
file = open("../Alice Spellcheck/AliceInWonderLand.txt")

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        alice_list.append(word)

dict_list = []
file = open("../Alice Spellcheck/dictionary.txt")

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        dict_list.append(word)

for words in alice_list:
    line_number += 1
    linear_search(words, dict_list, line_number)
    file.close()

print()
line_number = 0
print("This is the Binary seach!!:)")



for words in alice_list:
    line_number += 1
    binary_search(words, dict_list, line_number)
    file.close()

# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.
#
#
#
#
line_number = 0
def linear_search(key, my_list, list2):
    i = 0
    while i < (len(my_list) - 1) and key.upper() != my_list[i]:
        i += 1

    if i < len(my_list) - 1:
        return True
    else:
        print(key, "was not found in the Alice but is found in line", line_number, "of looking")


print("challange problem")
looking_list = []
file_1 = open("../Alice Spellcheck/AliceThroughTheLookingGlass.txt")
line_number = 0
for line in file_1:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        looking_list.append(word)
print(looking_list)


alice_list = []
file = open("../Alice Spellcheck/AliceInWonderLand.txt")


for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        alice_list.append(word)
print(alice_list)

for word in looking_list:
    line_number += 1
    linear_search(word, alice_list, line_number)
