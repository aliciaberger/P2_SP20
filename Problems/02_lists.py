# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
my_list = [x for x in range(101)]
print(my_list)
# b) Make a list of even numbers from 20 to 40
my_list = [x for x in range(20, 41)if x % 2 == 0]
print(my_list)
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list = [x ** 2 for x in range(101)]
print(my_list)
# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]

my_copy = [x for x in my_list if x > 0]
print(my_copy)


# PROBLEM 2 (Import the number list - 3pts)


# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list
from Problems.number_list import *
print(num_list[-6:-1])

# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
# Find and print the lowest number in num_list (1pt)
# Find and print the average of num_list (2pts)
# Remove the lowest number from num_list (2pt)
# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)
print(max(num_list))
print(min(num_list))
print((sum(num_list))/len(num_list))
num_list.sort()
num_list.pop(0)
top_ten = num_list[-10:]
print(top_ten)
# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?
new_list = num_list
num_mode = new_list[0]
pre_freq = 0
for num in new_list:
    frequ1 = new_list.count(num)
    if frequ1 > pre_freq:
        num_mode = num
        pre_freq = frequ1

print(num_mode)


# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't

pri_num_list = num_list[:]
primes = []
# its not perfect but i tired :)

for num in pri_num_list:
    for x in range(2, num, 1):
        if num % x == 0 or num % (x + 1) == 0 or num % (x + 3) == 0 or num % (x + 5) == 0 or num % (x + 9) == 0:
            break
        else:
            if num not in primes:
                primes.append(num)

print("there are ", len(primes), "prime numbers")

# Find the number of palindromes
# Hint: This may be easier to do with strings

pal = 0

for num in num_list:
    num = str(num)
    if num[0] == num[3] and num[1] == num[2]:
        pal += 1

print("There are", pal, "palindromes")


#project Euler