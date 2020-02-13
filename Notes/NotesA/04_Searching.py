# Searching

# use forward slashes to go into folders and .. to go "up" a folder
file = open('../resources/super_villains.txt', 'r')  # open to read
print(file)

print("1")
for line in file:
    print(line.strip())

file.close()
print("1")
# .strip() method removes the extra characters at end of text
print("    Hello ".strip())
print("World\n".strip())
print("!")

# 'w' opens to write and overwrites the file
# 'a' opens to append
file = open('../resources/super_villains.txt', 'a')
file.write('Lee the Merciless\n')
file.write('Rohan the Destroyer\n')
file.close()

# open to write can create a new file
file = open('../resources/heroes.txt', 'w')
file.write('Owen the Valiant\n')
file.close()

#  Better way to open close a file (syntactic sugar)
# file automatically closes after execution of with  ##what is f?
with open('../resources/super_villains.txt') as f:
    for line in f:
        print(line.strip())


# .read() method just imports whole file as a string
with open('../resources/super_villains.txt') as f:
    read_data = f.read()  # big string

print("\n\nRead method")
print(read_data)

# Reading data into an array (list)
with open('../resources/super_villains.txt', 'r') as f:
    villains = [x.strip().upper() for x in f]

print(villains)

# Linear Search (not very efficient but easy)

key = "Vidar the Manic".upper()

i = 0
while i < (len(villains)) and key != villains[i]:
    i += 1

if i < len(villains):
    print("Found it at position", i)
else:
    print(key, "is not in the list")

# try to make this into a function

def linear_search(key, list):
    """
    :param key: what you are looking for
    :param list: where you are looking
    :return: bool did you find it?
    """



# Binary list
villains.sort()
key = "THEODORA THE WICKED"
lower_bound = 0
upper_bound = len(villains)-1
found = False

while lower_bound <= upper_bound and not found:
    middle_possition = (upper_bound + lower_bound) // 2
    if villains[middle_possition] < key:
        lower_bound = middle_possition + 1
    elif villains[middle_possition] > key:
        upper_bound = middle_possition - 1
    else:
        found = True
if found:
    print(key, " found at position", middle_possition)
else:
    print(key,"was not found")



import re

def split_line(line):
    return re.findall('[A-Za-z] + (?:\'[A-Za-z]+)?', line)
my_text = "Hello, ! I am ! Alicia berger"

print(split_line(my_text))