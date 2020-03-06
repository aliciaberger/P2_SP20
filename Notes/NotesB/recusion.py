def f():
    print("F")
def g():
    print("G")
    f()
   # g()

g() # error comented out

# control recusion with depth

def controlled(depth):
    print("recursion depth", depth)
    if depth  > 0:
        controlled(depth - 1)
        print("recusion depth", depth, "has  closed")


controlled(10)