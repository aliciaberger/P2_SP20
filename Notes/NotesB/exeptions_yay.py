#exeptions use sparingly

x = 2
y = 0

#divide by 0 error
try:
    print(x / y)
except:
    print("Infinity")

# conversion error
try:
    int("t")
except:
    print("number is not valid")

# hadle ith a loop

done = False

while not done:
    try:
        user_imput = int(input("enter an intager: "))
        done = True
    except:
        print("number is not valid")

#flie opening

try:
    file = open("AliceInWonderland.txt")
except:
    print("could not open")

# use built in error types

try:
    my_file = open("myfir.txt")
except FileNotFoundError:
    print("file not found")