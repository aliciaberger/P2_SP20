'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re

def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
file = open("../Searching/dictionary.txt")
dict_list = []
long_word = ""
longer_word = ""
for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        dict_list.append(word)
print(dict_list)

for word in dict_list:
    long_word = word
    if len(long_word) > len(longer_word):
        longer_word = long_word
print(longer_word)

# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"

alice_list = []
file = open("../Searching/AliceInWonderland.txt")
for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        alice_list.append(word)

print(len(alice_list))

total = 0
for word in alice_list:
    total += len(word)
total = total / len(alice_list)
print(total)



# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?
alice_list = []
file = open("../Searching/AliceInWonderland.txt")

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        alice_list.append(word)

alice = 0
for word in alice_list:
    if word.upper() == "ALICE":
        alice += 1
print(alice)




# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
alice_list = []
file = open("../Searching/AliceInWonderland.txt")

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        alice_list.append(word)

long_word = ""
seven_list = []
for word in alice_list:
    long_word = word
    if len(long_word) == 7:
        seven_list.append(word)
print(seven_list)

num_mode = seven_list[0]
pre_freq = 0
for word in seven_list:
    frequ1 = seven_list.count(word)
    if frequ1 > pre_freq:
        num_mode = word
        pre_freq = frequ1

print(num_mode)



# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?



alice_list = []
file = open("../Searching/AliceInWonderland.txt")

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        alice_list.append(word)

chishire = 0
for word in alice_list:
    if word.upper() == "CHESHIRE":
        chishire += 1
print(chishire)


cat = 0
for word in alice_list:
    if word.upper() == "CAT":
        cat += 1
print(cat)

chishire = 0
for word in alice_list:
    if word.upper() == "CHESHIRE" and next.word.upper() == "CAT":
        chishire += 1
print(chishire)
