# sorting
import random

# swap values

a = 1
b = 2
temp = a
a = b
b = temp
print(a, b)

# pythonic way
a, b = b, a
print(a, b)

# make a ronadom losyt f 100 n numbhers of values from 1 - 99

my_list = [random.randrange(1, 100) for x in range (100)]
my_list2 = my_list[:]
print(my_list)


for cur_pos in range(len(my_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(my_list)):
        if my_list[scan_pos] < my_list[min_pos]:
            min_pos = scan_pos
    my_list[cur_pos], my_list[min_pos] = my_list[min_pos], my_list[cur_pos]

print(my_list)

print(my_list2)

#insertion sort

for key_pos in range(1, len(my_list2)):
    key_val = my_list2[key_pos]
    scan_pos = key_pos - 1
    while scan_pos >= 0 and my_list2[scan_pos] > key_val:
        my_list2[scan_pos + 1] = my_list2[scan_pos]
        scan_pos -= 1
    my_list2[scan_pos + 1] = key_val

print(my_list2)

# moral of the story use python sort
# oprionaly function paramiters
print("hello", end="  ")
print("world", end="!\n")
print("hello", "world", sep="Big", end="!!!\n")

def hello(name, time_of_day="morning"):
    print("hello", name, "good", time_of_day)

hello("alicia")

# lambda function
# when you need a munction but don 't ant ot make one
# also called anonomous functions
#namke = lambda paremiter: returned
double_me = lambda x: x * 2
print(double_me(3))
product = lambda a, b: a * b
print(product(4,6))

# real world sorting
my_list = [random.randrange(1, 100) for x in range(100)]
print(my_list)
my_2d = [[random.randrange(1, 100),random.randrange(1, 100)]for x in range(100)]
print(my_2d)

# sort method(changes the list in place)

my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

my_2d.sort(key=lambda a: a[0])
print(my_2d)
my_2d.sort(key=lambda a: a[1])
print(my_2d)
my_2d.sort(reverse=True, key=lambda a: sum(a))
print(my_2d)

#sorted funciton
new_list = sorted(my_2d, reverse=True, key= lambda w: abs(w[0] - w[1]))
print(new_list)