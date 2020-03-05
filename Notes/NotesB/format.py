import random

print(round(33.987009, 2))

a = 245678
b = 987623.4326
print("My Numebr is {}".format(a))
print("My Numebr is {:.3f}".format(b))
print("My Numebr is {} and {}".format(a, b))

print("My Numebr is {1:.2f} and {0: ,}".format(a, b))


for i in range(20):
    c = random.randrange(10000)
    print("{:5}".format(c))
# justification ^ cenetr < left >right
for i in range(20):
    c = random.randrange(10000, -10000)
    print("{:^12}".format(c))

#precision
for i in range(20):
    c = random.randrange()
    print("{:11.5f}".format(c))
