# LISTS

import random

my_names = ["Abe", "Bev", "Cam", "Dan", "Eve", "Flo"]
my_numbers = [5, 9, 12, -3, 6, 6]

print(my_names)
print(my_names[2])
print(my_names[-1])
print(my_names[:3])
print(my_names[3:5])
print(my_names[:])


# to copy a list

my_copy = my_names # NOT LIKE THIS
my_copy.append("Gill")
print(my_copy)
print(my_names)
my_copy = my_names[:] # do it liek this
my_copy.append("Hal")
print(my_copy)
print(my_names)

# 2d list

my_2d = [["Peanut", "Butter", "Jelly"],[8, "Hello"],["Spam", "Eggs"]]
print(my_2d[1])
print(my_2d[1][1])
my_2d[1].append("BYE")
print(my_2d)
if "Hal" in my_names:
    print("Hal is in my_names")

print(len(my_names)) #not the last index buyt the number. length is 7 last index is 6

print(min(my_numbers))
print(max(my_numbers))
print(sum(my_numbers))
my_names.append("Aaron")  #careful with case
print(min(my_names))



#list methouds

print(my_names.index("Cam")) #only sees the firts instance
my_names.append("Cam")
print(my_names.index("Cam"))
print(my_names.count("Mia"))
my_names.append("Deb")
print(my_names)
del my_names[my_names.index("Aaron")]
print(my_names)
my_names.sort()
print(my_names)
my_names.reverse()
print(my_names)


# Mofifing lists

del my_names[4]
print(my_names)

my_names.pop() #pops one off the end of the list
print(my_names)



end_ofList = my_names.pop()
print(my_names)
print(end_ofList)

front_of_list = my_names.pop(0)
print(front_of_list)


#concatenation

firts = "Franmcis"
last = "Parker"

print(firts + last)

print(my_names + my_numbers)


# interating through lists

emtpy_list = []

for i in range (2, 10):
    emtpy_list.append(i * 2)

print(emtpy_list)

for item in emtpy_list:  # this gets flushed
    item += 1
    print(item)

# add one to every item in the list
# this is how we modifuy a list in a loop
for i in range(len(emtpy_list)):
    emtpy_list[i] += 1


print(emtpy_list)



emtpy_list = [x for x in range(10)]
print(emtpy_list)

my_list = []

for i in range(101):
    my_list.append(i)
print(my_list)

#[Output for item in the range of the loop]
# first x is output


my_list = [x for x in range(101)]
print(my_list)


my_list = [x ** 2 for x in range(100)]

print(my_list)

# make a list of 1 to 100 squared but filter out the odd numbers

my_list = [x ** 2 for x in range(100) if (x ** 2) % 2 == 0]

print(my_list)


# roll a silge die 100 tiems and add it top a list

my_list = [random.randrange(1,7) for x in range(100)]

print(my_list)

# roll two die and add it to a list

my_list = [[random.randrange(1,7) for x in range(100)],[random.randrange(1,7) for x in range(100)]]

print(my_list)

my_list = [[random.randrange(1,7),random.randrange(1,7)] for x in range(100)]

print(my_list)

my_sums = [sum(x) for x in my_list]
print(my_sums)


# make a list from the 100 rolls that shows only the doubles
print ("y")
my_dpubles = [x for x in my_list if x[0] == x[1]]
print(my_dpubles)


# all at once
# roll 100 pairs and only put in the doubles


my_list = [x for x in[[random.randrange(1,7),random.randrange(1,7)] for x in range(100)]if x[0] == x[1]]
print(my_list)

# working with stings is alto like working with lists

first = "francis"
last = "Parker"
print(first[0])
first = first.upper()
print(first + last)
print(last[-2:])

if "N" in first:
    print("YES")
