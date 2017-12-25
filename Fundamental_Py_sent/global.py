# local variable
x = 6

def simple():
    print(x)

simple()

# local variable, we can print and can access in function but if we do some operation then it would create the problem

x = 6

def simple():
    print(x)

simple()
# x is not global variable

x = 6

# after defining global variable

def simple():
    global x
    x += 1
    print(x)

simple()

